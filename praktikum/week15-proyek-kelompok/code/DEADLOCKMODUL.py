import csv
from collections import defaultdict
import os

def maindead():
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(BASE_DIR, "dataset.csv")

    processes, allocation, request = read_dataset(filename)

    print("=== DATASET ===")
    for p in processes:
        print(f"{p}: Allocation={allocation[p]}, Request={request[p]}")

    wfg = build_wait_for_graph(processes, allocation, request)

    print("\n=== HASIL ===")
    deadlocks = detect_deadlock(wfg, processes)

    if deadlocks:
        for d in deadlocks:
            print("DEADLOCK:", " → ".join(d))
    else:
        print("Tidak terjadi deadlock")


def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = row['Process']
            processes.append(p)
            allocation[p] = row['Allocation']
            request[p] = row['Request']

    return processes, allocation, request


def build_wait_for_graph(processes, allocation, request):
    wfg = defaultdict(list)
    print("\n=== MEMBANGUN WAIT-FOR GRAPH ===")

    for p1 in processes:
        for p2 in processes:
            if p1 != p2 and request[p1] == allocation[p2]:
                wfg[p1].append(p2)
                print(f"{p1} menunggu {p2} (resource {request[p1]})")

    return wfg


def detect_deadlock(wfg, processes):
    visited = set()
    stack = []
    deadlocks = []

    def dfs(p):
        visited.add(p)
        stack.append(p)

        for neighbor in wfg[p]:
            if neighbor not in visited:
                dfs(neighbor)
            elif neighbor in stack:
                cycle = stack[stack.index(neighbor):]
                deadlocks.append(cycle)

        stack.pop()

    print("\n=== PROSES DETEKSI DEADLOCK ===")
    for p in processes:
        if p not in visited:
            dfs(p)

    return deadlocks


if __name__ == "__main__":
    maindead()

