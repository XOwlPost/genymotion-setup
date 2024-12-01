from invoke import task
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

@task
def check_services(c):
    """Check if necessary services are running."""
    print("Checking Nginx status...")
    result = c.run("sudo systemctl is-active nginx", warn=True)
    if result.failed:
        print("Nginx is not running. Starting it now...")
        c.run("sudo systemctl start nginx")
    else:
        print("Nginx is active.")

    print("Checking Docker status...")
    result = c.run("sudo systemctl is-active docker", warn=True)
    if result.failed:
        print("Docker is not running. Starting it now...")
        c.run("sudo systemctl start docker")
    else:
        print("Docker is active.")

@task
def manage_ports(ctx):
    """Run the port manager script."""
    script_path = os.path.join("port_manager", "port_manager.py")
    ctx.run(f"python3 {script_path}", pty=True)
