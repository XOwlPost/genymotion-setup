{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "genymotion-env";

  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.virtualenv
    pkgs.docker
    pkgs.fabric
    pkgs.iptables
    pkgs.qemu
    pkgs.libvirt
    pkgs.nginx
    pkgs.genymotion
    pkgs.ufw
  ];

  shellHook = ''
    echo "Environment configured for Genymotion development."
  '';
}
