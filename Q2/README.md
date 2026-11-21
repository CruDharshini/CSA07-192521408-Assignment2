# Q2 – Subnet a Campus That Keeps Growing

## Equal-size subnetting

The largest LAN requirement is 100 hosts, so each equal-size subnet must be at least /25 (126 usable hosts). A /24 can be split into only two /25 subnets. It therefore cannot provide four separate equal-size subnets for Labs, Staff, Library and WAN.

## VLSM plan

| Department | Network/prefix | Mask | First host | Last host | Broadcast |
|---|---|---|---|---|---|
| Labs | 192.168.10.0/25 | 255.255.255.128 | 192.168.10.1 | 192.168.10.126 | 192.168.10.127 |
| Staff | 192.168.10.128/26 | 255.255.255.192 | 192.168.10.129 | 192.168.10.190 | 192.168.10.191 |
| Library | 192.168.10.192/27 | 255.255.255.224 | 192.168.10.193 | 192.168.10.222 | 192.168.10.223 |
| WAN | 192.168.10.224/30 | 255.255.255.252 | 192.168.10.225 | 192.168.10.226 | 192.168.10.227 |

The next free address is 192.168.10.228.

## Hostel growth requirement

A 60-host network needs a /26 (64 addresses, 62 usable). Only 28 addresses remain in the original /24 after the given VLSM allocation, and they do not form a /26 block. It cannot be added in the remaining space. The smallest straightforward contiguous expansion that preserves the existing assignments is to extend the allocation to 192.168.10.0/23 and use 192.168.11.0/26 for the hostel.

## Route summarisation

172.16.8.0/24 through 172.16.11.0/24 summarize to 172.16.8.0/22. A /21 summary beginning at 172.16.8.0 covers 172.16.8.0–172.16.15.255, including 172.16.12.0/24 through 172.16.15.0/24. Advertising that broader summary can attract traffic for networks not actually reachable through the summarizing router (a black-hole or misrouting risk).

## Why largest-first VLSM

Allocating largest blocks first reserves the aligned address ranges they need. Allocating small blocks first can fragment the address space and leave no correctly aligned contiguous block for a larger subnet.

## Verification

Run `python vlsm.py` and `python verify_subnets.py`. The programs use Python's standard library only.
