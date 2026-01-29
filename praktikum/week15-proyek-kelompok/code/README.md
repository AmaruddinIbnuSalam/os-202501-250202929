## Mini Simulasi Sistem Operasi
---
#### CPU Scheduling (SJF), Page Replacement (LRU), dan Deadlock Detection
### 1. Deskripsi singkat
Mini Simulasi Sistem Operasi ini dirancang untuk memodelkan cara kerja sistem operasi modern dalam mengelola sumber daya komputasi. Aplikasi ini mengintegrasikan konsep penjadwalan CPU, manajemen memori, isolasi kontainer, serta deteksi deadlock dalam lingkungan simulasi yang aman dan terkontrol. Melalui simulasi ini, pengguna dapat memahami secara praktis bagaimana proses dijadwalkan, memori dialokasikan, dan sumber daya dibatasi guna menjaga kinerja dan stabilitas sistem
### 2. Modul yang diimplementasikan
**Modul A - CPU Scheduling**
* Algoritma: SJF
* Skenario: Download Manager
* Output: berupa simulasi visual SJF yang menampilkan:
  - Tabel proses
  - Urutan eksekusi SJF
  - Progress bar tiap proses
  - Pesan selesai

**Modul B - Page Replacement**
* Algoritma: LRU
* Skenario: Tab browser
* Output: Program menampilkan simulasi LRU browser beserta status hit dan page fault.

**Modul C - Deadlock Detection**
* Deadlock antar proses 
* Skenario: Proses saling menunggu resource tunggal
* Output:
    - Ada cycle → Deadlock
    - Tidak ada cycle → Aman

---
### Struktur Proyek
```bash
week15-proyek-kelompok
 ┣ code
 ┃ ┣ data
 ┃ ┃ ┗ database
 ┃ ┣ CPU.py
 ┃ ┣ dataset.csv
 ┃ ┣ deadlock.py
 ┃ ┣ DEADLOCKMODUL.py
 ┃ ┣ dockerfile
 ┃ ┣ kelompok.py
 ┃ ┣ LRU.py
 ┃ ┣ main.py
 ┃ ┗ README.md
 ┣ screenshots
 ┃ ┣ cpuscheduling.png
 ┃ ┣ dockerbuild.png
 ┃ ┣ example.png
 ┃ ┣ keluar.png
 ┃ ┗ pagereplacemen.png
 ┗  laporan.md
```
---
### Menjalankan Tanpa Docker
1. Pastikan bahasa pemrograman Python telah terpasang pada perangkat.
2. Buka terminal, lalu masuk ke direktori `week15-proyek-kelompok/code/`.
3. Jalankan file main.py
Setelah program dijalankan, akan muncul beberapa pilihan menu dengan fungsi sebagai berikut:
- Menu 1 menjalankan simulasi CPU Scheduling menggunakan algoritma SJF.
- Menu 2 menjalankan simulasi Page Replacement menggunakan algoritma LRU.
- Menu 3 menjalankan simulasi Deadlock Detection untuk mendeteksi kondisi deadlock.
- Menu 0 digunakan untuk mengakhiri program dan keluar dari aplikasi.

### Menjalankan Via Docker
1. Buka terminal, lalu masuk ke direktori `week15-proyek-kelompok/code/ .`
2. Lakukan proses build image Docker dengan perintah:
   ```bash
   docker build -t week15-proyek-kelompok .
   ```
3. Setelah proses build image selesai, jalankan program dengan perintah:
   ```bash
   docker run -it --rm week15-proyek-kelompok
   ```
Setelah program dijalankan, akan muncul beberapa pilihan menu dengan fungsi sebagai berikut:
- Menu 1: Menjalankan simulasi CPU Scheduling menggunakan algoritma Shortest Job First (SJF).
- Menu 2: Menjalankan simulasi Page Replacement menggunakan algoritma Least Recently Used (LRU).
- Menu 3: Menjalankan simulasi Deadlock Detection untuk mendeteksi adanya kondisi deadlock pada sistem.
- Menu 0: Digunakan untuk mengakhiri program dan keluar dari aplikasi.

---
### Dataset
**`process.csv` (CPU Scheduling)**
| Proses | Burst Time | Arrival Time |
|:--:|:--:|:--:|
| Persentasi-week15.mp4 | 8 | 0 |
| hasil-percobaan.jpg | 2 | 1 |
| laporan.md | 3 | 2 |
| musik.mp3 | 5 | 3 |

**`page_reference.txt`(Page Replacement)**

YouTube,Instagram,WhatsApp,YouTube,Instagram,Spotify,YouTube

**`dataset.csv` (Deadlock Detection)**
| Process | Allocation | Request |
| --- | --- | --- |
| P1 | R1 | R2 |
| P2 | R2 | R1 |
| P3 | R3 | R4 |



