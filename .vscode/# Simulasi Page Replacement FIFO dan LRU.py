# Simulasi Page Replacement FIFO dan LRU
# Praktikum Sistem Operasi - Minggu 10

def fifo_page_replacement(reference_string, frames):
    memory = []
    page_faults = 0
    queue_index = 0

    print("=== FIFO Page Replacement ===")
    for page in reference_string:
        if page in memory:
            status = "HIT"
        else:
            page_faults += 1
            status = "FAULT"
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[queue_index] = page
                queue_index = (queue_index + 1) % frames
        print(f"Page: {page} | Memory: {memory} | {status}")

    return page_faults


def lru_page_replacement(reference_string, frames):
    memory = []
    recent_use = {}
    page_faults = 0
    time = 0

    print("\n=== LRU Page Replacement ===")
    for page in reference_string:
        time += 1
        if page in memory:
            status = "HIT"
        else:
            page_faults += 1
            status = "FAULT"
            if len(memory) < frames:
                memory.append(page)
            else:
                # Cari halaman yang paling lama tidak digunakan
                lru_page = min(memory, key=lambda p: recent_use[p])
                memory[memory.index(lru_page)] = page
        recent_use[page] = time
        print(f"Page: {page} | Memory: {memory} | {status}")

    return page_faults


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    fifo_faults = fifo_page_replacement(reference_string, frames)
    lru_faults = lru_page_replacement(reference_string, frames)

    print("\n=== HASIL AKHIR ===")
    print(f"Total Page Fault FIFO: {fifo_faults}")
    print(f"Total Page Fault LRU : {lru_faults}")