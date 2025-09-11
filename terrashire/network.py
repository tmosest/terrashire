from scapy.all import ARP, Ether, srp
import socket
import time

from .config import Config

def scan_network(ip_range):
    """Scans the network for active devices using ARP requests."""
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Try to read the config file in this repo
    config = Config.loadConfig()

    devices = []
    for element in answered_list:
        mac = element[1].hwsrc
        ip = element[1].psrc
        info = {"ip": ip, "mac": mac}
        if config is not None and mac in config.servers_map:
            print(f"Found known server %s", mac)
            info = config.servers_map[mac]
            if ip != info.ip:
                print(f"Notice ip has changed from %s to %s for %s", info.ip, ip, mac)
            info = info.to_json_str()
        devices.append(info)
    return devices

def detect_new_devices(ip_range):
    """Detects new devices joining the network."""
    print("Performing initial scan...")
    # Try to read the config file in this repo
    config = Config.loadConfig()

    known_devices = {device.mac: device.ip for device in config.servers}
    
    current_devices = scan_network(ip_range)
    known_devices = {device["mac"]: device["ip"] for device in current_devices}
    print(f"Known devices: {len(known_devices)}")

    while True:
        time.sleep(10)  # Scan every 10 seconds
        print("Rescanning network...")
        new_scan_devices = scan_network(ip_range)
        
        for device in new_scan_devices:
            if device["mac"] not in known_devices:
                print(f"NEW DEVICE DETECTED: IP: {device['ip']}, MAC: {device['mac']}")
                known_devices[device["mac"]] = device["ip"] # Add to known devices

        # Optional: Remove devices that have left the network
        # This requires more complex logic to avoid false positives from temporary disconnections
        # For simplicity, this example focuses on new device detection.