#!/bin/bash

# Function to check if a port is available
check_port() {
    local port=$1
    if lsof -i :$port > /dev/null; then
        echo "Port $port is already in use. Please choose another port."
        return 1
    else
        echo "Port $port is available."
        return 0
    fi
}

# Function to assign ports dynamically
assign_port() {
    local service_name=$1
    local default_port=$2
    local new_port=$3

    echo "Assigning port for $service_name..."
    if check_port $default_port; then
        echo "Assigning default port $default_port to $service_name."
    elif check_port $new_port; then
        echo "Default port in use. Assigning alternate port $new_port to $service_name."
    else
        echo "Both default and alternate ports are in use for $service_name. Manual intervention required."
        exit 1
    fi
}

# Function to manage ADB-connected devices
assign_adb_ports() {
    local adb_ports=("5554" "5555")
    local device_list=$(adb devices | grep -w "device" | awk '{print $1}')

    if [ -z "$device_list" ]; then
        echo "No ADB devices connected."
        return
    fi

    echo "Connected ADB devices:"
    echo "$device_list"

    for device in $device_list; do
        for port in "${adb_ports[@]}"; do
            if ! check_port $port; then
                echo "Assigning port $port to device $device."
                adb forward tcp:$port tcp:$port
            else
                echo "Port $port is in use. Skipping for device $device."
            fi
        done
    done
}

# Assign ports for core services
assign_port "NGINX Proxy" 80 8080
assign_port "Android Emulator 1" 5554 5556
assign_port "Genymotion Emulator" 6080 8081

# Assign ports for ADB-connected devices
assign_adb_ports

echo "Port assignment completed."
