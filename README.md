# CSA07 – Computer Networks Assignment 2 (CO2)

**Student:** Dharshini  
**Register Number:** 192521408  
**Department:** Information Technology  
**Academic Year:** 2026–2027  
**Repository:** CSA07-192521408-Assignment2

## Assignment coverage

IPv4 addressing, NAT, packet switching, subnetting, VLSM, route summarisation, static routing, floating static routes, distance-vector routing, OSPF, IPv6, ICMP, multicast and SDN.

## Repository structure

| Folder | Contents |
|---|---|
| `Q1` | IPv4 address validation, NAT/PAT example and switching analysis |
| `Q2` | VLSM Python program, subnet verification and written analysis |
| `Q3` | Static-route and floating-static-route Cisco IOS configurations |
| `Q4` | Distance-vector Python program, failure case and routing analysis |
| `Q5` | OSPF reference-bandwidth calculations, router configurations and Dijkstra example |
| `Q6` | IPv6, EUI-64, ICMP, multicast and OpenFlow calculations |
| `Q7` | Campus redesign proposal, address plan and validation procedure |
| `Report` | Consolidated written assignment answers |

## Software

- Python 3 (standard library only)
- Cisco Packet Tracer or GNS3 for network simulations
- A text editor for viewing configuration and Markdown files

The exact software versions and operating-system details should be filled in by the student after checking the local machine.

## Running the Python programs

Open a terminal in the repository directory and run:

```bash
python Q1/address_check.py
python Q2/vlsm.py
python Q2/verify_subnets.py
python Q4/distance_vector.py
python Q4/distance_vector_failure.py
```

On Windows, use `py` instead of `python` if that is the configured Python launcher.

## Packet Tracer work still requiring local execution

The IOS configuration text files are provided as starting configurations. Build the corresponding topologies in Packet Tracer, adapt interface names to the router models, execute the commands, and save the resulting `.pkt` files and screenshots in the matching task folders.

Do not report a ping, failover, OSPF path, RIP convergence or other simulation as successful until it has been executed and verified.

## Evidence to add

- Packet Tracer topology screenshots and `.pkt` files for Q3–Q7 where applicable
- Actual `show ip route`, `show ip ospf neighbor`, `show ip protocols` and ping outputs
- Python execution screenshots or captured terminal output
- Local OS, Python and Packet Tracer/GNS3 versions
- Any instructor-specific corrections or observations

## Important notes

1. Each task folder contains the relevant source files and a short task README.
2. Calculated or expected results are labelled as such; they are not substitutes for simulation evidence.
3. Commit task work progressively. The repository history should reflect the work actually added.
4. Review the assignment sheet and confirm all interface names, IP addresses and evidence requirements before submission.
