# Q7 – Redesign and Validate

## Selected limitation

The original Q2 campus allocation uses 192.168.10.0/24. After assigning Labs /25, Staff /26, Library /27 and WAN /30, the next free address is 192.168.10.228. A 60-host hostel needs a /26 (64 addresses, 62 usable), so it cannot fit into the remaining space.

## Objective

Add a separate subnet for 60 hostel devices while preserving all four existing subnet network addresses and avoiding overlap.

## Revised address plan

Expand the allocated block to 192.168.10.0/23 (512 total addresses, 510 usable across the aggregate). Keep the original allocations and add the hostel subnet in the second /24.

| Segment | Network/prefix | First host | Last host | Broadcast |
|---|---|---|---|---|
| Labs | 192.168.10.0/25 | 192.168.10.1 | 192.168.10.126 | 192.168.10.127 |
| Staff | 192.168.10.128/26 | 192.168.10.129 | 192.168.10.190 | 192.168.10.191 |
| Library | 192.168.10.192/27 | 192.168.10.193 | 192.168.10.222 | 192.168.10.223 |
| WAN | 192.168.10.224/30 | 192.168.10.225 | 192.168.10.226 | 192.168.10.227 |
| Hostel | 192.168.11.0/26 | 192.168.11.1 | 192.168.11.62 | 192.168.11.63 |

## Topology

Use one central router with five routed LAN interfaces (or router-on-a-stick with VLANs and a trunk) connected to the department switches. Each segment uses its own subnet and default gateway. The WAN link remains a point-to-point subnet.

## Prediction

All five networks should have non-overlapping address ranges. The hostel should support 60 devices because /26 provides 62 usable host addresses.

## Validation procedure

1. Build the original design in Packet Tracer and record the failed attempt to fit a /26 hostel subnet into the remaining /24 space.
2. Expand the address allocation to /23 and configure the hostel subnet.
3. Assign gateways and configure inter-VLAN routing or router interfaces.
4. Ping between a host in each department and the hostel.
5. Inspect interface and routing tables; confirm no overlapping networks.
6. Save the actual Packet Tracer file and screenshots under this folder.

## Evaluation

The /23 redesign meets the address objective and preserves existing subnet assignments. It reserves a larger aggregate block, so the original /24 remains preferable for a small campus with no expected expansion. Actual implementation and ping evidence must be added after testing.
