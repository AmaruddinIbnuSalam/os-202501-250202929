
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

| Proses | Completion Time | Burst Time | Arrival Time | Turnaround Time | Waiting Time |
| :---: | :---: | :---: | :---: | :---: | :---: |
| P1 | 14 | 5 | 0 | 14 | 10 |
| P2 | 6 | 3 | 1 | 5 | 4 |
| P3 | 22 | 8 | 2 | 20 | 2 |
| P4 | 20 | 6 | 3 | 17 | 20 |

   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12   14   17   20   22
     ```
   - Catat sisa *burst time* tiap putaran.

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

| Proses | Burst Time | Arrival Time | Priority |
| :---: | :---: | :---: | :---: | 
| P2 |  3 | 0 | 1 |
| P1 |  5 | 1 | 2 |
| P4 |  6 | 2 | 3 |
| P3 |  8 | 3 | 4 |

   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

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
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
