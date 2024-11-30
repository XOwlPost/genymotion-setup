from fabric import task

@task
def install_genymotion(c):
    """Install Genymotion."""
    c.run("echo 'Installing Genymotion...'")

    # Download the installer if not already downloaded
    genymotion_bin = "/tmp/genymotion.bin"
    genymotion_url = "https://dl.genymotion.com/releases/genymotion-3.3.0/genymotion-3.3.0-linux_x64.bin"

    # Check if the file already exists, if not download it
    c.run(f"if [ ! -f {genymotion_bin} ]; then wget {genymotion_url} -O {genymotion_bin}; fi")

    # Make the installer executable
    c.run(f"chmod +x {genymotion_bin}")

    # Install Genymotion with the -y flag
    c.run(f"sudo {genymotion_bin} --yes --destination /opt/genymobile")

    # Cleanup after installation
    c.run(f"rm -f {genymotion_bin}")
    c.run("echo 'Genymotion installation completed.'")

@task
def setup_genymotion(c):
    """Set up Genymotion."""
    install_genymotion(c)
    c.run("echo 'Configuring Genymotion ports and permissions...'")
    
    # Firewall rules for UFW
    c.run("sudo ufw allow 5554/tcp")
    c.run("sudo ufw allow 5555/tcp")
    c.run("sudo ufw allow 5900/tcp")
    c.run("sudo ufw allow 6080/tcp")
    
    # If using iptables instead of ufw
    c.run("iptables -A INPUT -p tcp --dport 5554 -j ACCEPT || true")
    c.run("iptables -A INPUT -p tcp --dport 5555 -j ACCEPT || true")
    c.run("iptables -A INPUT -p tcp --dport 5900 -j ACCEPT || true")
    c.run("iptables -A INPUT -p tcp --dport 6080 -j ACCEPT || true")
    
    c.run("echo 'Genymotion setup completed.'")
