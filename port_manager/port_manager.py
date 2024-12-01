import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PORT_PLAN_FILE = os.path.join(BASE_DIR, "port_plan.md")

# File paths
PORT_PLAN_FILE = "port_manager/port_plan.md"
PORT_MAP_FILE = "port_manager/port_map.json"

def load_port_plan():
    try:
        with open(PORT_PLAN_FILE, "r") as f:
            return f.read()
    except FileNotFoundError:
        with open(PORT_PLAN_FILE, "w") as f:
            f.write("")  # Create a blank file
        print(f"Created missing port plan file: {PORT_PLAN_FILE}")
        return ""

def load_port_map():
    """Load the current port map."""
    if not os.path.exists(PORT_MAP_FILE):
        return {}
    with open(PORT_MAP_FILE, "r") as f:
        return json.load(f)

def save_port_map(port_map):
    """Save the updated port map."""
    with open(PORT_MAP_FILE, "w") as f:
        json.dump(port_map, f, indent=4)

def find_next_available_port(start_port, reserved_ports):
    """Find the next available port."""
    while start_port in reserved_ports:
        start_port += 1
    return start_port

def assign_ports():
    """Assign ports dynamically based on the port plan."""
    port_plan = load_port_plan()
    port_map = load_port_map()
    reserved_ports = set(port_map.values())

    for entry in port_plan:
        service, default_port = entry.split(":")
        default_port = int(default_port)

        if default_port not in reserved_ports:
            port_map[service] = default_port
            reserved_ports.add(default_port)
        else:
            next_port = find_next_available_port(default_port + 1, reserved_ports)
            port_map[service] = next_port
            reserved_ports.add(next_port)

    save_port_map(port_map)
    print("Port assignment completed.")
    print(json.dumps(port_map, indent=4))

if __name__ == "__main__":
    assign_ports()
