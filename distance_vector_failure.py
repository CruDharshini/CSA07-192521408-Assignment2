"""Recalculate the distance vectors after the C-D link fails."""
from distance_vector import run

if __name__ == "__main__":
    print("After C-D link failure (cost set to INF):")
    run(("C", "D"))
