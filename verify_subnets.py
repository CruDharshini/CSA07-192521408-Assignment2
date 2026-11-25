"""Verify the VLSM plan and the later hostel requirement."""
import ipaddress

subnets = [
    ipaddress.ip_network("192.168.10.0/25"),
    ipaddress.ip_network("192.168.10.128/26"),
    ipaddress.ip_network("192.168.10.192/27"),
    ipaddress.ip_network("192.168.10.224/30"),
]

for subnet in subnets:
    print(subnet, "usable hosts:", subnet.num_addresses - 2)

for index, first in enumerate(subnets):
    for second in subnets[index + 1:]:
        assert not first.overlaps(second), f"Overlap: {first} and {second}"

hostel = ipaddress.ip_network("192.168.11.0/26")
expanded = ipaddress.ip_network("192.168.10.0/23")
assert hostel.subnet_of(expanded)
assert all(not hostel.overlaps(net) for net in subnets)

print("No overlaps. Hostel subnet fits in expanded", expanded)
print("Hostel usable hosts:", hostel.num_addresses - 2)
