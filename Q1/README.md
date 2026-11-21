# Q1 – Spot the Invalid Addresses

## Address analysis

| Device | Given address | Network | Broadcast | Usable range | Host valid? |
|---|---|---|---|---|---|
| Admission PC | 172.16.45.200/20 | 172.16.32.0 | 172.16.47.255 | 172.16.32.1–172.16.47.254 | Yes |
| Lab printer | 10.0.15.255/21 | 10.0.8.0 | 10.0.15.255 | 10.0.8.1–10.0.15.254 | No: broadcast |
| X-ray server | 192.168.4.0/23 | 192.168.4.0 | 192.168.5.255 | 192.168.4.1–192.168.5.254 | No: network |
| Clinic router | 203.0.113.10/29 | 203.0.113.8 | 203.0.113.15 | 203.0.113.9–203.0.113.14 | Yes |

The two invalid host assignments are the lab printer address (subnet broadcast) and X-ray server address (subnet network identifier).

## NAT/PAT example

Both internal hosts can use source port 50000 because PAT translates their sessions to distinct public-side ports.

| Inside local | Inside source port | Inside global | Translated port |
|---|---:|---|---:|
| 192.168.1.10 | 50000 | 203.0.113.10 | 40001 |
| 192.168.1.11 | 50000 | 203.0.113.10 | 40002 |

This is an illustrative translation table, not a captured router output. The router tracks the protocol and port mapping to deliver replies to the correct internal host.

A /29 contains 8 addresses, normally 6 usable host addresses. The 18 clinic devices can share a public address through NAT/PAT; the public /29 block is not being assigned one address per device.

## Datagram and virtual-circuit switching

In datagram switching, packets are routed independently and can take different paths, so they may arrive out of order. In virtual-circuit switching, a logical path is established first and packets generally follow that path in sequence. The receiving transport/application layer may still need sequencing and retransmission mechanisms depending on the protocol.

## Alternative: public /27

A /27 has 32 total addresses and 30 usable host addresses. Eighteen devices require 18 usable addresses, leaving 12 usable addresses. This is sufficient by address count. The exact monetary cost cannot be calculated without the ISP's pricing. Publicly addressed devices have greater direct exposure and need appropriate firewall controls. NAT-specific inbound reachability and some peer-to-peer/application traversal issues may be reduced, but security is still required.

## Conclusion

The printer and X-ray server addresses are invalid host addresses. PAT permits multiple internal devices to share a public address by translating ports. A /27 provides enough usable public addresses for 18 devices, but cost and exposure must be considered.
