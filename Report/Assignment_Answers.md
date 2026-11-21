# CSA07 – Computer Networks Assignment 2 (CO2)
## Addressing, Subnetting and Routing

**Student:** Dharshini  
**Register Number:** 192521408  
**Department:** Information Technology  
**Academic Year:** 2026–2027

This report consolidates the task answers. Supporting runnable programs and router configuration templates are stored in the corresponding Q1–Q7 folders.

## Q1 – Spot the Invalid Addresses

Admission PC 172.16.45.200/20 belongs to 172.16.32.0/20, with broadcast 172.16.47.255 and usable range 172.16.32.1–172.16.47.254; it is a valid host. Lab printer 10.0.15.255/21 belongs to 10.0.8.0/21 and is the broadcast address, so it is invalid. X-ray server 192.168.4.0/23 is the network address of 192.168.4.0/23 and is invalid as a host. Clinic router 203.0.113.10/29 belongs to 203.0.113.8/29, whose usable range is 203.0.113.9–203.0.113.14; it is valid.

PAT permits two private hosts using source port 50000 to share a public IP by translating their sessions to different public-side ports. Datagram packets may take different paths and arrive out of order; virtual-circuit packets generally follow an established logical path. A /27 has 30 usable addresses, enough for 18 devices, but ISP pricing is not supplied and cannot be calculated.

## Q2 – Subnet a Campus That Keeps Growing

Equal-size subnetting based on the largest 100-host requirement needs /25 subnets. A /24 supplies only two /25 subnets, so four separate equal-size subnets cannot be created. VLSM uses Labs 192.168.10.0/25, Staff 192.168.10.128/26, Library 192.168.10.192/27 and WAN 192.168.10.224/30. The next free address is 192.168.10.228.

A 60-host hostel requires /26, which cannot fit into the remaining 28 addresses. Expanding the aggregate allocation to 192.168.10.0/23 allows the hostel to use 192.168.11.0/26 while preserving the original subnet addresses. The four city-campus /24 networks summarize to 172.16.8.0/22. A 172.16.8.0/21 summary would also cover 172.16.12.0/24 through 172.16.15.0/24, which may attract traffic for networks not reachable through that router.

## Q3 – Which Way Will the Packet Go?

Using longest-prefix match: 10.1.2.200 uses next hop 192.0.2.13; 10.1.2.100 uses 192.0.2.9; 10.1.9.9 uses 192.0.2.5; 10.7.7.7 uses 192.0.2.1; and 8.8.8.8 uses default next hop 198.51.100.1.

R1 uses 10.0.0.1/30 on its serial link and routes 192.168.20.0/24 through 10.0.0.2. R2 uses 10.0.0.2/30 and the reverse route through 10.0.0.1. A floating static route with administrative distance 200 is less preferred than the primary static route (default AD 1). It requires a separately configured backup link at both ends. Static routes are straightforward for small networks; OSPF is easier to maintain as the number of campuses grows and can recalculate routes after topology changes.

## Q4 – Distance-Vector Routing

The five-router network uses A–B 2, A–C 7, B–C 3, B–D 8, C–D 1 and D–E 4. The final distance vectors are:
- A: 0, 2, 5, 6, 10
- B: 2, 0, 3, 4, 8
- C: 5, 3, 0, 1, 5
- D: 6, 4, 1, 0, 4
- E: 10, 8, 5, 4, 0

The supplied synchronous Python implementation converges after four rounds. A reaches C through B at cost 2+3=5, cheaper than direct cost 7. If C–D fails, the recalculated vectors are A (0,2,5,10,14), B (2,0,3,8,12), C (5,3,0,11,15), D (10,8,11,0,4), and E (14,12,15,4,0). Count-to-infinity can occur when routers exchange stale routes after a failure. Split horizon with poison reverse advertises the route back to the neighbour as unreachable, helping prevent a two-router loop. Link-state routing distributes link-state information and independently calculates shortest paths using Dijkstra.

## Q5 – OSPF Reference Bandwidth

With the default 100 Mbps reference bandwidth, 10 Mbps has cost 10, while 100 Mbps, 1 Gbps and 10 Gbps all have minimum cost 1. With a 10,000 Mbps reference bandwidth, the costs become 1000, 100, 10 and 1 respectively.

For the six-router example in Q5/README.md, Dijkstra selects R1–R2–R6 at cost 2 instead of R1–R3–R4–R6 at cost 30. A single Area 0 is appropriate for the small example. EIGRP metric calculations require actual bandwidth and delay inputs; IS-IS requires configured metrics. Those values are not provided in the assignment, so no unsupported numeric comparison is claimed.

## Q6 – IPv6, ICMP, Multicast and SDN

The shortened IPv6 address is 2001:db8::ff00:42:8329. The EUI-64 identifier derived from 00:1A:2B:3C:4D:5E is 021A:2BFF:FE3C:4D5E. Traceroute sends probes with increasing TTL/Hop Limit and uses ICMP Time Exceeded replies to discover routers. IPv4 multicast group 239.1.2.3 maps to Ethernet multicast MAC 01:00:5E:01:02:03.

For the supplied OpenFlow rules, an HTTP packet to 10.5.1.1 matches both the destination /16 rule and TCP/80 rule; priority 200 wins and sends it to port 3. SSH to 10.6.1.1 matches neither and is dropped by the default rule. A 6in4 tunnel adds a 20-byte outer IPv4 header to a 100-byte packet, producing 120 bytes before link-layer overhead. Dual-stack is a practical transition strategy when IPv4 must continue to operate.

## Q7 – Redesign and Validate

The original 192.168.10.0/24 plan cannot fit a 60-host hostel subnet after the original VLSM allocations. Expanding the aggregate to 192.168.10.0/23 allows a hostel subnet at 192.168.11.0/26, with 62 usable addresses, while preserving the original four subnet assignments. The measurable objective is to support all five segments without overlap or renumbering. Packet Tracer ping tests, topology screenshots and the saved .pkt file must be added after local execution.

## Overall conclusion

VLSM makes better use of address space for differently sized departments. Longest-prefix match selects the most specific route, floating static routes provide a backup when correctly configured, and routing protocols support changing network topologies. The revised /23 campus allocation accommodates the hostel while preserving existing subnet assignments.

## Evidence status

The Python source files and router configuration templates are provided in this repository. Packet Tracer .pkt files, screenshots, actual command outputs, and local software-version details remain to be generated and checked by running the simulations on the student's computer.
