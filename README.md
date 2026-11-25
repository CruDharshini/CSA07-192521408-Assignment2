# CSA07 – Computer Networks Assignment 2 (CO2)

- Student: Dharshini
- Register number: 192521408
- Department: Information Technology
- Academic year: 2026–2027

## Topics

IPv4 addressing, NAT/PAT, packet switching, subnetting, VLSM, route summarisation, static and floating routes, distance-vector routing, OSPF, IPv6, ICMP, multicast and SDN.

## Python programs

Run these from the repository's main directory using Python 3:

```bash
python address_check.py
python vlsm.py
python verify_subnets.py
python distance_vector.py
python distance_vector_failure.py
```

The scripts use Python's standard library only. Run them locally and capture your own terminal output for submission.

## Router configuration templates

- `R1_primary.cfg`, `R2.cfg`: primary static-routing example.
- `R1_floating_backup.cfg`: floating static route example. Configure a separate backup link and the return route before testing.
- `ospf_area0_template.cfg`: OSPF reference-bandwidth starting template; add the correct network statements for each router.

## Written answers

See [Assignment_Answers.md](Assignment_Answers.md) for the worked calculations, explanations and Q7 redesign.

## Before submission

- Build and save the required Packet Tracer/GNS3 topologies as `.pkt` files.
- Capture genuine routing-table, ping, failover and OSPF evidence.
- Record your actual operating system, Python and Packet Tracer/GNS3 versions.
- Do not describe a simulation as successful until it has been run and checked.

The assignment sheet asks for one folder per task and progressive commits. This repository is arranged in the main directory to match the requested layout; check with your faculty whether this layout is acceptable before final submission.
