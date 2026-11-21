"""Synchronous Bellman-Ford distance-vector exchange for routers A-E."""
INF = 99
names = "ABCDE"
cost = {
    ("A", "B"): 2, ("A", "C"): 7, ("B", "C"): 3,
    ("B", "D"): 8, ("C", "D"): 1, ("D", "E"): 4,
}

def run(failed_link=None):
    links = {}
    for (u, v), c in cost.items():
        if failed_link == (u, v) or failed_link == (v, u):
            c = INF
        links[u, v] = links[v, u] = c

    table = {
        u: {v: (0 if u == v else links.get((u, v), INF)) for v in names}
        for u in names
    }
    rounds = 0
    changed = True
    while changed:
        changed = False
        rounds += 1
        old = {u: dict(table[u]) for u in names}
        for u in names:
            for n in names:
                if (u, n) not in links or links[u, n] >= INF:
                    continue
                for dest in names:
                    candidate = links[u, n] + old[n][dest]
                    if candidate < table[u][dest]:
                        table[u][dest] = candidate
                        changed = True
    print(f"converged after {rounds} rounds")
    for u in names:
        print(u, " ".join(f"{table[u][v]:2d}" for v in names))

if __name__ == "__main__":
    run()
