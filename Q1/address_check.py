from ipaddress import ip_interface

devices = {
    "Admission PC": "172.16.45.200/20",
    "Lab printer": "10.0.15.255/21",
    "X-ray server": "192.168.4.0/23",
    "Clinic router": "203.0.113.10/29",
}

for name, value in devices.items():
    interface = ip_interface(value)
    network = interface.network
    valid = interface.ip in network.hosts()
    print(f"{name}: {interface.ip}/{network.prefixlen}")
    print(f"  Network: {network.network_address}")
    print(f"  Broadcast: {network.broadcast_address}")
    print(f"  Usable: {network.network_address + 1} - {network.broadcast_address - 1}")
    print(f"  Valid host: {'Yes' if valid else 'No'}")
