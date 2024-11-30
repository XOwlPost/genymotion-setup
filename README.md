
# Genie Automation Project

## Overview
Automates the setup of:
- **Proxmox VM**
- **Genymotion Emulators**
- **Nginx Reverse Proxy**

## Usage

1. **Activate Virtual Environment**:
   ```bash
   source fab_env/bin/activate
   ```

2. **Run Setup**:
   ```bash
   fab setup
   ```

3. **Customize**:
   Modify the tasks and scripts as needed.

## Directory Structure
- `fabfile.py`: Main Fabric entry point.
- `tasks/`: Modular Fabric tasks.
- `scripts/`: Utility scripts for setup.
