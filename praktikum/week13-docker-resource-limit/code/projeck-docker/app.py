import time
import math
import sys

# =============================
# CEK LIMIT DARI DOCKER (CGROUP v2)
# =============================

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


# =============================
# CPU TEST (BERBASIS KECEPATAN)
# =============================

def cpu_test():
    duration = 2           # detik
    bar_len = 20

    cpu_limit = get_cpu_limit()

    print("=== SIMULASI CPU TEST ===")
    print(f"Durasi Test       : {duration} detik")
    print("Limit CPU Docker  :", "NON-LIMIT" if cpu_limit is None else cpu_limit, "\n")

    start_wall = time.time()
    start_cpu = time.process_time()

    while True:
        elapsed = time.time() - start_wall
        if elapsed >= duration:
            break

        # Beban CPU (kecepatan eksekusi)
        for i in range(1, 300_000):
            math.sqrt(i)

        progress = min(elapsed / duration, 1)
        filled = int(bar_len * progress)
        bar = "█" * filled + "░" * (bar_len - filled)

        sys.stdout.write(
            f"\rProgress: |{bar}| {progress*100:6.2f}% Waktu: {elapsed:4.2f}s"
        )
        sys.stdout.flush()

    cpu_used = time.process_time() - start_cpu
    cpu_usage = (cpu_used / duration) * 100

    bar = "█" * bar_len
    print(f"\rProgress: |{bar}| 100.00% Waktu: {duration:.2f}s")

    print("\n=== HASIL CPU TEST ===")
    print(f"CPU Time Digunakan : {cpu_used:.2f} detik")
    print(f"Estimasi CPU Usage : {cpu_usage:.2f}%")
    print("Simulasi CPU selesai.\n")


# =============================
# MEMORY TEST (BERTAHAP & SELESAI)
# =============================

def memory_test():
    step_mb = 10
    delay = 0.3
    bar_len = 30

    limit = get_memory_limit()
    test_max = 500  # batas uji jika NON-LIMIT

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


# =============================
# MAIN
# =============================

cpu_test()
memory_test()
