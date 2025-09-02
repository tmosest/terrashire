from scapy.all import ARP, Ether, srp
import socket

def scan_network(target_ip_range="192.168.1.1/24"):
    """
    Scans the local network for connected devices.

    Args:
        target_ip_range (str): The IP address range to scan (e.g., "192.168.1.1/24").

    Returns:
        list: A list of dictionaries, each containing 'ip' and 'mac' of discovered devices.
    """
    arp_request = ARP(pdst=target_ip_range)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether_frame / arp_request

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        ip_address = received.psrc
        try:
            # Perform a reverse DNS lookup for the hostname
            hostname = socket.gethostbyaddr(ip_address)[0]
        except (socket.herror, socket.gaierror):
            # Handle cases where a hostname cannot be resolved
            hostname = ""
        devices.append({'ip': ip_address, 'mac': received.hwsrc, "hostname": hostname})
    return devices
