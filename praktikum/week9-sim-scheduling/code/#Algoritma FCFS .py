# Algoritma FCFS dengan output tabel
print("Algoritma FCFS")
n = int(input("Masukkan jumlah proses: "))

process = []
arrival_time = []
burst_time = []
waiting_time = [0] * n
turnaround_time = [0] * n

# Input data
for P in range(n):
    process.append(f"P{P+1}")
    arrival_time.append(int(input(f"Arrival Time P{P+1}: ")))
    burst_time.append(int(input(f"Burst Time P{P+1}: ")))

# Sorting berdasarkan Arrival Time
for i in range(n):
    for j in range(i + 1, n):
        if arrival_time[i] > arrival_time[j]:
            arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
            burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
            process[i], process[j] = process[j], process[i]

# Hitung Waiting Time
waiting_time[0] = 0
for i in range(1, n):
    waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

# Hitung Turnaround Time
for i in range(n):
    turnaround_time[i] = waiting_time[i] + burst_time[i]

# Cetak Tabel
print("\n+--------+--------------+------------+--------------+----------------+")
print("| Proses | Arrival Time | Burst Time | Waiting Time | Turnaround Time |")
print("+--------+--------------+------------+--------------+----------------+")

for i in range(n):
    print(f"| {process[i]:<6} | {arrival_time[i]:<12} | {burst_time[i]:<10} | {waiting_time[i]:<12} | {turnaround_time[i]:<14} |")

print("+--------+--------------+------------+--------------+----------------+")

# Rata-rata
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

print(f"\nRata-rata Waiting Time    : {avg_wt:.2f}")
print(f"Rata-rata Turnaround Time : {avg_tat:.2f}")
