# Q4 – Distance-Vector Routing

The program implements synchronous Bellman-Ford distance-vector updates. INF is represented by 99, matching the assignment's code.

## Expected converged table (original topology)

```
converged after 4 rounds
A  0  2  5  6 10
B  2  0  3  4  8
C  5  3  0  1  5
D  6  4  1  0  4
E 10  8  5  4  0
```

A reaches C through B at cost 2 + 3 = 5, which is cheaper than the direct link cost 7.

## Link failure case

The second program starts with the C–D link cost set to 99 and recalculates the routes. Expected final distances:

```
converged after 3 rounds
A  0  2  5 10 14
B  2  0  3  8 12
C  5  3  0 11 15
D 10  8 11  0  4
E 14 12 15  4  0
```

## Count to infinity

In the X–Y–Z line, after Y–Z fails, X and Y can mistakenly advertise stale routes to each other. Their metrics may rise repeatedly. Split horizon with poison reverse advertises a route back to the neighbour from which it was learned as unreachable (the protocol's infinity metric), preventing this two-router loop.

## Packet Tracer

Configure RIP on the five routers, verify routes with `show ip route` and `show ip protocols`, shut down the C–D interface, and record the actual convergence behaviour. The Python model is not a substitute for Packet Tracer evidence.
