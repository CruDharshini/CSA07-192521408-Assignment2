# Q5 – OSPF Reference Bandwidth

OSPF interface cost is reference bandwidth divided by interface bandwidth, with a minimum cost of 1 in the common Cisco implementation.

With the default 100 Mbps reference bandwidth:

| Link | Cost |
|---|---:|
| 10 Mbps | 10 |
| 100 Mbps | 1 |
| 1 Gbps | 1 |
| 10 Gbps | 1 |

With a reference bandwidth of 10,000 Mbps:

| Link | Cost |
|---|---:|
| 10 Mbps | 1000 |
| 100 Mbps | 100 |
| 1 Gbps | 10 |
| 10 Gbps | 1 |

The reference bandwidth must be configured consistently on all routers in the OSPF domain.

## Six-router example

Links and costs:
- R1–R2: 10 Gbps, cost 1
- R2–R6: 10 Gbps, cost 1
- R1–R3: 1 Gbps, cost 10
- R3–R4: 1 Gbps, cost 10
- R4–R6: 1 Gbps, cost 10
- R2–R5: 100 Mbps, cost 100
- R5–R6: 100 Mbps, cost 100

From R1, Dijkstra selects R1–R2–R6 with total cost 2. The alternative R1–R3–R4–R6 has cost 30.

## Example Cisco IOS commands

Apply on each router, adjusting the network statement to match its actual interface subnets:

```
router ospf 1
 auto-cost reference-bandwidth 10000
 network <connected-network> <wildcard-mask> area 0
```

For the six-router exercise, one area (Area 0) is reasonable. Larger provider networks may use multiple areas to limit topology information and improve manageability.

## EIGRP and IS-IS

EIGRP's composite metric can use bandwidth and delay (with default K values); its exact metric requires the configured bandwidth and delay values. IS-IS uses configurable link metrics. The question does not supply enough interface delay data or IS-IS metric settings to calculate unique numeric metrics for those protocols. Do not invent these values.

## Evidence

Build the six-router topology, configure the same reference bandwidth on all OSPF routers, and capture `show ip route`, `show ip ospf neighbor` and the selected path. No Packet Tracer output is included until it is actually run.
