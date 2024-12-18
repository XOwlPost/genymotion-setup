#!/bin/bash

echo "Running Port Manager..."
python3 port_manager/port_manager.py || {
    echo "Port Manager failed. Check the logs above."
    exit 1
}

echo "Port Manager completed successfully."

# Enable strict error handling
set -e

# Ensure idx/default.nix exists
if [ ! -f "idx/default.nix" ]; then
    echo "Creating default.nix..."
    mkdir -p idx
    cat <<EOF > idx/default.nix
{ pkgs ? import <nixpkgs> { config = { allowUnfree = true; }; } }:

pkgs.mkShell {
  name = "genymotion-env";

  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.virtualenv
    pkgs.docker
    pkgs.python3Packages.fabric
    pkgs.iptables
    pkgs.qemu
    pkgs.libvirt
    pkgs.nginx
    pkgs.genymotion
  ];

  shellHook = ''
    echo "Environment configured for Genymotion."
  '';
}
EOF
fi

# Initialize Nix environment
if ! nix-shell idx/default.nix; then
    echo "Failed to initialize Nix environment."
    exit 1
fi

# Set up Python virtual environment
echo "Setting up Python virtual environment..."
if [ ! -d "fab_env" ]; then
    virtualenv fab_env
fi
source fab_env/bin/activate
pip install -r requirements.txt

# Generate Docker Compose YAML
echo "Generating Docker Compose YAML..."
if ! python3 scripts/gen_yaml.py; then
    echo "Failed to generate Docker Compose YAML."
    exit 1
fi

# Run Fabric setup tasks
echo "Running Fabric setup tasks..."
if ! fab setup; then
    echo "Fabric setup tasks failed."
    exit 1
fi

echo "Reloading Nginx..."
sudo systemctl restart nginx

echo "Testing Nginx configuration..."
if ! curl http://127.0.0.1:6080; then
    echo "Genymotion setup may have encountered an issue. Check logs for details."
    exit 1
fi

echo "Bootstrap completed successfully!"
