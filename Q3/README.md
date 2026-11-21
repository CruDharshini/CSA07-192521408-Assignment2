# Q3 – Which Way Will the Packet Go?

## Longest-prefix match

| Destination | Matching route | Next hop |
|---|---|---|
| 10.1.2.200 | 10.1.2.128/25 | 192.0.2.13 |
| 10.1.2.100 | 10.1.2.0/24 | 192.0.2.9 |
| 10.1.9.9 | 10.1.0.0/16 | 192.0.2.5 |
| 10.7.7.7 | 10.0.0.0/8 | 192.0.2.1 |
| 8.8.8.8 | 0.0.0.0/0 | 198.51.100.1 |

The router chooses the matching route with the greatest prefix length.

## Files

- `R1_primary.cfg`: Main campus router, primary serial link and static route.
- `R2.cfg`: City campus router and reverse static route.
- `R1_floating_backup.cfg`: Example floating static route using administrative distance 200.

The backup next hop 10.0.1.2 is an example. Build and address a physically separate backup link in Packet Tracer before using it. The backup route will not work until that link and the corresponding route on R2 are configured.

## Packet Tracer test

1. Connect R1 and R2 using a serial link; ensure the DCE end is identified.
2. Configure the interface addresses and clock rate on the DCE end.
3. Configure LAN PCs, gateways and the static routes.
4. Ping between the two LANs and record the result.
5. Add and configure a separate backup link and floating routes at both ends.
6. Shut down the primary link, inspect `show ip route`, and repeat the ping.
7. Restore the primary link and verify route preference.

Removing the DCE clock rate can prevent the serial connection from operating correctly. Interface names may differ by Packet Tracer router model.
