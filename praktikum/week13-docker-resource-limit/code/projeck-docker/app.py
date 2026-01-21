import time
import math
import sys


def get_cpu_limit():
    try:
        with open("/sys/fs/cgroup/cpu.max") as f:
            quota, period = f.read().strip().split()
            if quota == "max":
                return None
            return round(int(quota) / int(period), 2)
    except:
        return None


def get_memory_limit():
    try:
        with open("/sys/fs/cgroup/memory.max") as f:
            data = f.read().strip()
            if data == "max":
                return None
            return int(data) // (1024 * 1024)
    except:
        return None



def cpu_test():
    total_work = 200_000_000   # jumlah kerja tetap
    bar_len = 20

    cpu_limit = get_cpu_limit()

    print("=== SIMULASI CPU TEST ===")
    print("Model Test        : Fixed Workload")
    print("Total Work        :", total_work)
    print("Limit CPU Docker  :", "NON-LIMIT" if cpu_limit is None else cpu_limit, "\n")

    start_wall = time.time()
    start_cpu = time.process_time()

    for i in range(1, total_work + 1):
        math.sqrt(i)

        if i % (total_work // bar_len) == 0:
            progress = i / total_work
            filled = int(bar_len * progress)
            bar = "█" * filled + "░" * (bar_len - filled)

            elapsed = time.time() - start_wall
            sys.stdout.write(
                f"\rProgress: |{bar}| {progress*100:6.2f}% Waktu: {elapsed:6.2f}s"
            )
            sys.stdout.flush()

    cpu_used = time.process_time() - start_cpu
    wall_time = time.time() - start_wall

    bar = "█" * bar_len
    print(f"\rProgress: |{bar}| 100.00%")

    print("\n=== HASIL CPU TEST ===")
    print(f"Wall Time         : {wall_time:.2f} detik")
    print(f"CPU Time Digunakan: {cpu_used:.2f} detik")
    print("Simulasi CPU selesai.\n")


def memory_test():
    step_mb = 10
    delay = 0.3
    bar_len = 30

    limit = get_memory_limit()
    test_max = 500 

    used_mb = 0
    allocated = []

    print("=== SIMULASI MEMORY TEST ===")

    if limit is None:
        print(f"Limit Memori Docker : NON-LIMIT (uji sampai {test_max} MB)\n")
        target = test_max
    else:
        print(f"Limit Memori Docker : {limit} MB\n")
        target = limit

    try:
        while used_mb < target:
            allocated.append(bytearray(step_mb * 1024 * 1024))
            used_mb += step_mb

            progress = used_mb / target
            filled = int(bar_len * progress)
            bar = "█" * filled + "░" * (bar_len - filled)

            sys.stdout.write(
                f"\rProgress: |{bar}| {progress*100:6.2f}% Memori: {used_mb:.2f} MB"
            )
            sys.stdout.flush()

            time.sleep(delay)

        print("\n\nMemory test selesai (target tercapai)")

    except MemoryError:
        print("\n\n=== MEMORY LIMIT TERCAPAI ===")
        print(f"Memori sebelum gagal : {used_mb:.2f} MB")

    print("Simulasi Memori selesai.\n")



cpu_test()
memory_test()
