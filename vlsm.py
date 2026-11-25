"""VLSM allocation for the college's 192.168.10.0/24 block."""
import ipaddress


def allocate_vlsm(base, needs):
    current = int(ipaddress.ip_address(base))

    for name, hosts in sorted(needs, key=lambda item: item[1], reverse=True):
        block_size = 1
        while block_size < hosts + 2:
            block_size *= 2

        prefix = 32 - (block_size.bit_length() - 1)
        current = ((current + block_size - 1) // block_size) * block_size
        network = ipaddress.ip_network((current, prefix))

        print(
            f"{name:10} {network.network_address}/{prefix} "
            f"hosts {network.network_address + 1} - {network.broadcast_address - 1} "
            f"bcast {network.broadcast_address}"
        )
        current = int(network.broadcast_address) + 1

    return ipaddress.ip_address(current)


needs = [("Labs", 100), ("Staff", 50), ("Library", 25), ("WAN link", 2)]
print("next free address:", allocate_vlsm("192.168.10.0", needs))
