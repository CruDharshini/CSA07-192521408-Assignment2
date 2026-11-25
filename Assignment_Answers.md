# Assignment 2 – Worked Answers (CO2)

**Student:** Dharshini  
**Register number:** 192521408  
**Department:** Information Technology  
**Academic year:** 2026–2027

## Q1 – Spot the Invalid Addresses

| Device | Address | Network | Broadcast | Usable host range | Valid host? |
|---|---|---|---|---|---|
| Admission PC | 172.16.45.200/20 | 172.16.32.0 | 172.16.47.255 | 172.16.32.1–172.16.47.254 | Yes |
| Lab printer | 10.0.15.255/21 | 10.0.8.0 | 10.0.15.255 | 10.0.8.1–10.0.15.254 | No – broadcast |
| X-ray server | 192.168.4.0/23 | 192.168.4.0 | 192.168.5.255 | 192.168.4.1–192.168.5.254 | No – network address |
| Clinic router | 203.0.113.10/29 | 203.0.113.8 | 203.0.113.15 | 203.0.113.9–203.0.113.14 | Yes |

PAT allows two private devices using source port 50000 to share one public IP by assigning different translated ports, for example 40001 and 40002. Datagram packets are routed independently and can arrive out of order. Virtual-circuit switching establishes a logical path first, and packets generally follow that path.

A /27 contains 30 usable addresses, enough for 18 devices. It needs more public addresses and may cost more; the ISP pricing is not given, so an exact cost cannot be calculated. Directly addressed devices also need firewall protection.

## Q2 – Subnet a Campus That Keeps Growing

### Equal-size subnetting

The largest requirement is 100 hosts, so each equal-size subnet must be /25 (126 usable hosts). A /24 contains only two /25 subnets, so it cannot provide four separate equal-size subnets.

### VLSM plan

| Department | Network/prefix | Mask | First host | Last host | Broadcast |
|---|---|---|---|---|---|
| Labs | 192.168.10.0/25 | 255.255.255.128 | 192.168.10.1 | 192.168.10.126 | 192.168.10.127 |
| Staff | 192.168.10.128/26 | 255.255.255.192 | 192.168.10.129 | 192.168.10.190 | 192.168.10.191 |
| Library | 192.168.10.192/27 | 255.255.255.224 | 192.168.10.193 | 192.168.10.222 | 192.168.10.223 |
| WAN | 192.168.10.224/30 | 255.255.255.252 | 192.168.10.225 | 192.168.10.226 | 192.168.10.227 |

The next free address is 192.168.10.228. A 60-host hostel needs a /26 (62 usable hosts), which cannot fit in the remaining part of the /24. Expanding the allocation to 192.168.10.0/23 allows the hostel to use 192.168.11.0/26 without changing the existing subnet addresses.

The four city-campus networks 172.16.8.0/24 through 172.16.11.0/24 summarize to 172.16.8.0/22. A /21 summary would also cover 172.16.12.0/24 through 172.16.15.0/24 and could attract traffic for networks not reachable through that router.

VLSM assigns the largest blocks first to avoid fragmenting the address space and leaving no correctly aligned block for a larger network.

## Q3 – Which Way Will the Packet Go?

| Destination | Longest matching route | Next hop |
|---|---|---|
| 10.1.2.200 | 10.1.2.128/25 | 192.0.2.13 |
| 10.1.2.100 | 10.1.2.0/24 | 192.0.2.9 |
| 10.1.9.9 | 10.1.0.0/16 | 192.0.2.5 |
| 10.7.7.7 | 10.0.0.0/8 | 192.0.2.1 |
| 8.8.8.8 | 0.0.0.0/0 | 198.51.100.1 |

The router uses longest-prefix match: among matching routes, it selects the most specific prefix. The R1 and R2 configuration files provide the primary serial link and reciprocal static routes. The floating route uses administrative distance 200, so it is less preferred than the primary static route (default AD 1). It requires a separately addressed backup link and a matching return route at the other router.

Static routing is simple for a small network. OSPF requires more initial configuration but is easier to maintain as the number of campuses and changing links increases.

## Q4 – Watch Distance-Vector Routing Count to Infinity

The final distance vectors for the original five-router topology are:

| Router | A | B | C | D | E |
|---|---:|---:|---:|---:|---:|
| A | 0 | 2 | 5 | 6 | 10 |
| B | 2 | 0 | 3 | 4 | 8 |
| C | 5 | 3 | 0 | 1 | 5 |
| D | 6 | 4 | 1 | 0 | 4 |
| E | 10 | 8 | 5 | 4 | 0 |

The supplied synchronous Bellman-Ford program converges after four rounds. A reaches C through B at cost 2 + 3 = 5, which is less than the direct link cost 7.

After the C–D link fails, the expected final vectors are A (0, 2, 5, 10, 14), B (2, 0, 3, 8, 12), C (5, 3, 0, 11, 15), D (10, 8, 11, 0, 4), and E (14, 12, 15, 4, 0). In a count-to-infinity situation, routers can keep advertising stale routes to one another after a failure. Split horizon with poison reverse advertises a route back to the neighbour from which it was learned as unreachable, helping prevent a two-router loop. Link-state routing instead distributes link-state information and uses Dijkstra's algorithm to calculate shortest paths.

## Q5 – Why Does OSPF Treat 1 Gbps and 10 Gbps the Same?

With the default 100 Mbps reference bandwidth, the OSPF costs are:

| Link speed | Cost |
|---|---:|
| 10 Mbps | 10 |
| 100 Mbps | 1 |
| 1 Gbps | 1 |
| 10 Gbps | 1 |

With a 10,000 Mbps reference bandwidth:

| Link speed | Cost |
|---|---:|
| 10 Mbps | 1000 |
| 100 Mbps | 100 |
| 1 Gbps | 10 |
| 10 Gbps | 1 |

The reference bandwidth must be configured consistently across the OSPF domain. In the six-router example, Dijkstra selects R1–R2–R6 at total cost 2 instead of R1–R3–R4–R6 at cost 30. Area 0 is reasonable for the small example; larger provider networks may use multiple areas for manageability.

EIGRP metric calculation needs actual bandwidth and delay inputs. IS-IS needs configured link metrics. The assignment does not provide enough values to calculate unique numeric comparisons, so none are invented here.

## Q6 – IPv6, ICMP, Multicast and SDN

- Shortest form of the IPv6 address: **2001:db8::ff00:42:8329**.
- EUI-64 from MAC 00:1A:2B:3C:4D:5E: insert FF:FE and invert the U/L bit in the first octet, giving **021A:2BFF:FE3C:4D5E**.
- Traceroute increases TTL (IPv4) or Hop Limit (IPv6). A router that reduces the value to zero discards the probe and normally sends an ICMP Time Exceeded message, revealing that hop.
- IPv4 multicast group 239.1.2.3 maps to Ethernet multicast MAC **01:00:5E:01:02:03**. The network replicates the stream toward group members where paths branch.
- For the OpenFlow rules, HTTP to 10.5.1.1 matches both the destination /16 and TCP port 80 rules. Priority 200 wins, so it is sent to port 3. SSH to 10.6.1.1 matches neither specific rule and is dropped by the priority-0 rule.
- A 6in4 tunnel adds a 20-byte outer IPv4 header. A 100-byte inner packet therefore becomes 120 bytes before link-layer overhead. Dual-stack is a practical transition where IPv4 must continue to work during IPv6 deployment.

SDN offers centralized policy control, but the controller needs suitable security, availability and capacity planning.

## Q7 – Find the Weak Point, Redesign and Validate

The original campus allocation uses 192.168.10.0/24. After assigning Labs /25, Staff /26, Library /27 and WAN /30, the next free address is 192.168.10.228. A 60-host hostel needs a /26, so it cannot fit into the remaining address space.

**Objective:** add a subnet for 60 hostel devices without overlap or changing the four existing subnet network addresses.

Expand the aggregate allocation to 192.168.10.0/23 and place the hostel in 192.168.11.0/26:

| Segment | Network/prefix | First host | Last host | Broadcast |
|---|---|---|---|---|
| Labs | 192.168.10.0/25 | 192.168.10.1 | 192.168.10.126 | 192.168.10.127 |
| Staff | 192.168.10.128/26 | 192.168.10.129 | 192.168.10.190 | 192.168.10.191 |
| Library | 192.168.10.192/27 | 192.168.10.193 | 192.168.10.222 | 192.168.10.223 |
| WAN | 192.168.10.224/30 | 192.168.10.225 | 192.168.10.226 | 192.168.10.227 |
| Hostel | 192.168.11.0/26 | 192.168.11.1 | 192.168.11.62 | 192.168.11.63 |

Use a central router with five routed LAN interfaces, or router-on-a-stick with VLANs and a trunk. Each segment needs its own gateway. The prediction is that all five subnets will be non-overlapping and the hostel will support 60 devices because /26 provides 62 usable addresses.

To validate, build the original and revised designs in Packet Tracer, test inter-segment pings, inspect interface and routing tables, and save the actual project and screenshots. The /23 plan meets the addressing objective but reserves a larger block; the original /24 is preferable if no expansion is expected.

## Evidence still to collect

The Python programs and router configuration templates are provided as working files. Packet Tracer project files, screenshots, actual ping/routing outputs, and local software-version details must be collected by running the simulations on the student's computer. The templates are not proof that a simulation has been completed.
