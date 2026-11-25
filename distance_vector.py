"""Synchronous Bellman-Ford distance-vector exchange for routers A-E."""
INF = 99
NAMES = "ABCDE"
COST = {
    ("A", "B"): 2, ("A", "C"): 7, ("B", "C"): 3,
    ("B", "D"): 8, ("C", "D"): 1, ("D", "E"): 4,
}


def run(failed_link=None):
    links = {}
    for (u, v), cost in COST.items():
        if failed_link == (u, v) or failed_link == (v, u):
            cost = INF
        links[u, v] = links[v, u] = cost

    table = {
        u: {v: (0 if u == v else links.get((u, v), INF)) for v in NAMES}
        for u in NAMES
    }

    rounds = 0
    changed = True
    while changed:
        changed = False
        rounds += 1
        old = {u: dict(table[u]) for u in NAMES}

        for u in NAMES:
            for neighbour in NAMES:
                if (u, neighbour) not in links or links[u, neighbour] >= INF:
                    continue
                for destination in NAMES:
                    candidate = links[u, neighbour] + old[neighbour][destination]
                    if candidate < table[u][destination]:
                        table[u][destination] = candidate
                        changed = True

    print(f"converged after {rounds} rounds")
    for u in NAMES:
        print(u, " ".join(f"{table[u][v]:2d}" for v in NAMES))


if __name__ == "__main__":
    run()
