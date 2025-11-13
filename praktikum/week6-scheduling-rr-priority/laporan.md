
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling  

---

## Identitas
- **Nama**  : AMARUDDIN IBNU SALAM 
- **NIM**   : 250202929  
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.
---

## Dasar Teori
- Round Robin (RR) menggunakan metode time-sharing dengan membagi waktu CPU secara adil kepada tiap proses berdasarkan time quantum yang sama. Setiap proses berjalan selama jatah waktu tersebut secara bergilir, lalu dilanjutkan proses berikutnya.

- Round Robin (RR) menjamin tidak ada proses yang menunggu lebih lama, karena quantum bersifat bebas starvation, tetapi performa quantum dipengaruhi ukuran quantum (terlalu kecil banyak switching, jika terlalu besar seperti FCFS).

- Priority Scheduling memilih proses dengan prioritas tertinggi untuk dijalankan lebih dulu. Bisa preemptive (proses bisa digantikan jika ada prioritas lebih tinggi) atau non-preemptive(proses  jika ada prioritas lebih tinggi pun tidak dapat digantikan ).

- Sesama prioritas sama, bisa dipakai FCFS sebagai tie-breaker. Algoritma ini cocok untuk proses penting, namun berisiko terjadi starvation pada prioritas rendah.

---

## Langkah Pengerjaan
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.




   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12   14   17   20   22
     ```
   - Catat sisa *burst time* tiap putaran.
   - 
| Proses | Completion Time | Burst Time | Arrival Time | Turnaround Time | Waiting Time |
| :----: | :-------------: | :--------: | :----------: | :-------------: | :----------: |
| P1     | 14              | 5          | 0            | 14              | 9            |
| P2     | 6               | 3          | 1            | 5               | 2            |
| P3     | 22              | 8          | 2            | 20              | 12           |
| P4     | 20              | 6          | 3            | 17              | 11           |


| Proses | Waktu | Burst Time | Quantum | Sisa waktu |
| :---: | :---: | :---: | :---: | :---: |
| P1 | 0 | 5 | 3 | 2 |
| P2 | 3 | 3 | 3 | 0 |
| P3 | 6 | 8 | 3 | 5 |
| P4 | 9 | 6 | 3 | 3 |
| P1 | 12 | 2 | 2 | 0 |
| P3 | 14 | 5 | 3 | 2 |
| P4 | 17 | 3 | 3 | 0 |
| P3 | 20 | 2 | 2 | 0 |


3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi). 

| Proses | Completion Time | Burst Time | Arrival Time | Turnaround Time | Waiting Time |
| :----: | :-------------: | :--------: | :----------: | :-------------: | :----------: |
| P1     | 14              | 5          | 0            | 14              | 9            |
| P2     | 6               | 3          | 1            | 5               | 2            |
| P3     | 22              | 8          | 2            | 20              | 12           |
| P4     | 20              | 6          | 3            | 17              | 11           |
Rata-rata WT = 5,25
Rata-rata TAT = 10,75

   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.
  
Quantum 2
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	18 |  0 | 5 |	18 |  13|
|  P2  |	13 |	1 | 3 |	12 |	9 |
|  P3  |	24 |	2 | 8 |	22 |	14|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |   ||17.75|12.25|

Quantum 5
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	5  |  0 | 5 |	5  |  0 |
|  P2  |	8  |	1 | 3 |	7  |	4 |
|  P3  |	21 |	2 | 8 |	19 |	11|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |  || 12.5|  7 |

   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | 8,5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | 4,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis

- RR adil tapi tergantung quantum
Round Robin memberikan waktu CPU bergantian ke semua proses. Jika quantum terlalu kecil, sering ganti proses jadi lambat. Kalau terlalu besar, mirip antrian biasa.
- Priority lebih cepat proses penting
Proses dengan prioritas tinggi jalan dulu, bikin proses penting cepat selesai. Tapi proses prioritas rendah bisa kelamaan nunggu (starvation).
- Quantum pengaruh besar di RR
Quantum kecil bikin proses sering berhenti-berhenti, jadi lama. Quantum besar bikin proses cepat selesai tapi bisa kurang responsif.
- Priority lebih efisien, RR lebih adil
Priority lebih cepat secara rata-rata, cocok buat tugas penting. RR lebih cocok buat sistem yang butuh keadilan semua proses.
- Kesimpulan: pilih sesuai kebutuhan
Pakai RR kalau ingin semua proses dapat giliran. Pakai Priority kalau ada proses yang harus didahulukan, tapi perlu cara supaya proses kecil tidak kelamaan menunggu.

---

## Kesimpulan
- Round Robin cocok untuk sistem yang butuh keadilan karena semua proses mendapat giliran CPU secara bergantian, tapi efisiensinya bergantung pada pemilihan time quantum.

- Priority Scheduling lebih efisien untuk memproses tugas penting lebih cepat, namun berisiko membuat proses dengan prioritas rendah menunggu terlalu lama (starvation).

---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* untuk algoritma RR dan Priority.  
2. Sajikan hasil perhitungan dan Gantt Chart dalam `laporan.md`.  
3. Bandingkan performa dan jelaskan pengaruh *time quantum* serta prioritas.  
4. Simpan semua bukti (tabel, grafik, atau gambar) ke folder `screenshots/`.  

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?  
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?  
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
