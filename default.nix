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
    echo "Environment configured for Genymotion development."
  '';
}
