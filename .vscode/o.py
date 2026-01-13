
print("Drag and drop refrence string.txt")
file_path = input().strip()

def read_refrence_string(file_path):
    with open(file_path, mode='r') as file:
        lines = file.readlines()
    
    reference_string = [int(x.strip()) for x in lines[1].split(',')]
    frames = int(lines[0].split('=')[1].strip())

    return frames, reference_string

def algo_fifo (refrence_string, frames) :
    memory =[]
    page_fault = 0
    pointer = 0

    print ("=== FIFO Page Replacement Algorithm ===")
    for page in refrence_string:
        if page in memory :
            status = "HIT"

        else:
            page_fault += 1
            status ="FAULT"
            if len (memory) < frames:
                memory.append(page)
            else:
                memory[pointer] =page 
                pointer = (pointer + 1)% frames
        print(f"page:{page} | memory: {memory} | {status}")

    return page_fault

def lru(refrence_string, frames):
    memory =[]
    last_used ={}
    page_fault = 0
    time = 0

    print("\n=== LRU Page Replacement Algorithm ===")
    for page in refrence_string:
        time += 1
        if page in memory:
            status="HIT"

        else:
            if len(memory) < frames:
                memory.append(page)
                page_fault += 1
                status="FAULT"
            else:
                lru_page = min (memory, key=last_used.get)
                memory.remove(lru_page)
                memory.append(page)
                page_fault += 1
                status="FAULT"
        last_used[page] = time
        print(f"page:{page} | memory: {memory} | {status}")

    return page_fault

# PROGRAM UTAMA 
frames, reference_string = read_refrence_string(file_path)

print("\njumlah frame:",frames)
print("reference string:",reference_string)

fifo_faults = algo_fifo(reference_string, frames)
lru_faults = lru(reference_string, frames)

print("\n=== HASIL AKHIR ===")
print(f"Total Page Fault FIFO: {fifo_faults}")
print(f"Total Page Fault LRU : {lru_faults}")
    


