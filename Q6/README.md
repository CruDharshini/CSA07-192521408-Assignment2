# Q6 – IPv6, ICMP, Multicast and SDN

## IPv6 shortening

`2001:0db8:0000:0000:0000:ff00:0042:8329` becomes `2001:db8::ff00:42:8329`.

## EUI-64

MAC: `00:1A:2B:3C:4D:5E`

Insert `FF:FE` in the middle and invert the U/L bit in the first octet (00 becomes 02):

`02:1A:2B:FF:FE:3C:4D:5E`

Interface identifier: `021A:2BFF:FE3C:4D5E`.

## Traceroute and ICMP

Traceroute sends probes with increasing TTL (IPv4) or Hop Limit (IPv6). A router that decrements the field to zero discards the probe and normally returns an ICMP Time Exceeded message. The source uses these replies to identify successive hops.

## IPv4 multicast MAC mapping

For multicast group `239.1.2.3`, the Ethernet multicast mapping is `01:00:5E:01:02:03`. Multicast forwarding allows a source to send one stream to a group; the network replicates packets where paths branch toward group members.

## OpenFlow rules

- Priority 200: destination 10.5.0.0/16 → port 3
- Priority 100: TCP destination port 80 → controller
- Priority 0: drop

An HTTP packet to 10.5.1.1 matches both the /16 and TCP/80 rules. The higher-priority /16 rule wins, so it is sent to port 3. An SSH packet to 10.6.1.1 matches neither specific rule and is dropped by the priority-0 rule.

SDN offers centralized policy and flexible control, but the controller needs strong security, availability and capacity planning.

## IPv6 transition

A 6in4 tunnel adds an outer IPv4 header. With a 20-byte IPv4 header and a 100-byte inner packet, the tunneled packet is 120 bytes, adding 20 bytes (20%) before any other link-layer overhead. Dual-stack is a practical transition when IPv4 systems must continue to operate while IPv6 is introduced.
