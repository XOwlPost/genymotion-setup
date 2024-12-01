
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

## Port Management Module

### Overview
The `port_manager` module dynamically manages ports for emulators, devices, and services, ensuring no conflicts arise.

### Features
- Automatically resolves port conflicts.
- Tracks assignments in `port_map.json`.

### Usage
Run the port manager manually:
```bash
python3 port_manager/port_manager.py
