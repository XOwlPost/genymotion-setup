from shutil import copyfile
import os

def configure_nginx(c):
    """Configure Nginx for Genymotion."""
    c.run("echo 'Installing and configuring Nginx...'")
    local_path = "config/nginx/genymotion.conf"
    remote_path = "/etc/nginx/sites-available/genymotion"
    
    # Copy file locally
    if os.path.exists(local_path):
        c.sudo(f"cp {local_path} {remote_path}")
        c.sudo("ln -sf /etc/nginx/sites-available/genymotion /etc/nginx/sites-enabled/genymotion")
        c.sudo("systemctl restart nginx")
        c.run("echo 'Nginx configuration applied successfully.'")
    else:
        c.run("echo 'Nginx configuration file not found. Skipping.'")
