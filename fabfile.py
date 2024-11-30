from fabric import task
from tasks.genymotion import setup_genymotion, install_genymotion
from tasks.nginx import configure_nginx
from tasks.proxmox import setup_proxmox_vm
import os
import sys

# Debugging
print("Python path:", sys.path)
print("Current directory:", sys.modules[__name__].__file__)
print("Genymotion task loaded:", setup_genymotion)

def is_idx_environment():
    """Check if running in an IDX environment."""
    return os.path.exists("/home/user/.idx") or os.getenv("NIX_SHELL")

@task
def setup(c):
    """Main setup task."""
    if is_idx_environment():
        c.run("echo 'Adapting for IDX environment...'")
        c.run("nix-shell idx/default.nix --run 'fab setup'")
    else:
        setup_proxmox_vm(c)
        setup_genymotion(c)
        configure_nginx(c)

@task
def lint(c):
    """Lint YAML files."""
    c.run("yq eval . config/*.yaml")

@task
def cleanup(c):
    """Remove temporary files and reset the environment."""
    c.run("rm -rf /tmp/genymotion.bin fab_env")
    c.run("docker-compose down")
    c.run("echo 'Cleanup complete.'")
