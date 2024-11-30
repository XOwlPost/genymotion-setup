from fabric import task

@task
def setup_proxmox_vm(c):
    """Automate Proxmox VM setup."""
    c.run("echo 'Installing Proxmox dependencies...'")
    c.run("sudo apt update && sudo apt install -y qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils virtinst virt-manager")
    c.run("echo 'Creating Proxmox VM for Genymotion...'")
    # Add the commands for VM setup, e.g., proxmox-ctl commands or ansible playbooks
    c.run("echo 'Proxmox VM setup complete.'")
