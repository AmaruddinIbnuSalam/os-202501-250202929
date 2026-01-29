import sys
import time

def menu_SJF():
    BAR_LENGTH = 30
    # Data: (ID, Nama File, Durasi (detik), Ukuran (MB))
    downloads = [
        (1, "Persentasi-week15.mp4", 8, 800),
        (2, "hasil-percobaan.jpg", 2, 2),
        (3, "laporan.md", 3, 3),
        (4, "musik.mp3", 5, 5)
    ]
    print("\n" + "="*40)
    print("FILE YANG AKAN DIDOWNLOAD ".center(40))
    print("="*40 + "\n")

    print("NAMA FILE                      | Arrival Time (AT) | Burst Time (BT) |")
    print("------------------------------ | ----------------: | --------------: |")
    print("hasil-percobaan.jpg            |                 0 |               2 |")
    print("Persentasi-week15.mp4          |                 1 |               8 |")
    print("laporan.md                     |                 2 |               3 |")
    print("musik.mp3                      |                 3 |               5 |")    
    # SJF (Shortest Job First) → Urutkan berdasarkan durasi (indeks ke-2)
    downloads.sort(key=lambda x: x[2])
    print("\n" + "="*40)
    print(" DOWNLOAD MANAGER (SJF) ".center(40))
    print("="*40 + "\n")

    for job_id, name, duration, size in downloads:
        print(f"Memproses: {name} ({size} MB)")
        for second in range(duration + 1):
            filled = int(BAR_LENGTH * second / duration)
            bar = "█" * filled + "-" * (BAR_LENGTH - filled)
            percent = int((second / duration) * 100)
            
            # Menggunakan \r untuk animasi progress bar di satu baris
            sys.stdout.write(f"\r[{bar}] {percent}% - {second}/{duration}s")
            sys.stdout.flush()
            time.sleep(1)
        print("\nCompleted ✅\n")

    print("-" * 40)
    print("Semua download selesai.")
    print("-" * 40)

