
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF 

---

## Identitas
- **Nama**  : AMARUDDIN IBNU SALAM  
- **NIM**   : 250202929  
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  

---

## Dasar Teori
Pemilihan Berdasarkan Waktu CPU Burst Terpendek
1. SJF memilih proses yang memiliki perkiraan waktu eksekusi (CPU burst) paling pendek untuk dijalankan lebih dulu. Tujuannya adalah meminimalkan rata-rata waktu tunggu proses.

2. Optimal dalam Rata-rata Waktu Tunggu
Menurut teori Silberschatz et al., SJF merupakan algoritma optimal secara teori, karena menghasilkan average waiting time terendah dibanding algoritma non-preemptive lainnya.
3. Dapat Bersifat Preemptive atau Non-preemptive;

   - Non-preemptive SJF: proses berjalan sampai selesai.
   - Preemptive SJF (SRTF – Shortest Remaining Time First): proses baru dengan waktu eksekusi lebih pendek dapat memotong proses yang sedang berjalan.

4. Membutuhkan Estimasi Burst Time
Implementasi SJF membutuhkan perkiraan lama waktu eksekusi setiap proses. Estimasi biasanya didasarkan pada riwayat eksekusi sebelumnya.

5. Risiko Starvation
Jika proses pendek terus berdatangan, proses panjang bisa tertunda lama (starvation), sehingga tidak adil bagi proses dengan burst time besar.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
- Urut berdasarkan Arrival Time: P1 (0) → P2 (1) → P3 (2) → P4 (3)  
- Berikut Perhitungan untuk tiap proses:
```
P1: start = 0, finish = 0 + 6 = 6
WT = start − arrival = 0 − 0 = 0
TAT = WT + burst = 0 + 6 = 6

P2: start = finish(P1) = 6, finish = 6 + 8 = 14
WT = 6 − 1 = 5
TAT = 5 + 8 = 13

P3: start = finish(P2) = 14, finish = 14 + 7 = 21
WT = 14 − 2 = 12
TAT = 12 + 7 = 19

P4: start = finish(P3) = 21, finish = 21 + 3 = 24
WT = 21 − 3 = 18
TAT = 18 + 3 = 21
```
   - Rata-rata Waiting Time dan Turnaround Time. 
   ```
      - Avg Waiting Time (FCFS) = (0 + 5 + 12 + 18) / 4 = 8.75ms
      - Avg Turnaround Time (FCFS) = (6 + 13 + 19 + 21) / 4 = 14.75ms
   ```
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).

   P4 (0) → P1 (1) → P3 (2) → P2 (3)  

   - Perhitungan WT dan TAT

| Proses | Burst Time | Arrival Time | Star Time | Finis Time |WT | TAT|
   |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
   | P4 | 3 | 3 | 3 | 6 | 0 | 3 |
   | P1 | 6 | 0 | 6  | 12  | 6  |  12 |
   | P3 | 7 | 2 | 12 | 19 | 10 | 17 |
   | P2 | 8 | 1 | 19  | 27 | 18  | 26 |

   rata-rata Waiting Time (WT) = 8,5

   rata-rata Turnaround Time (TAT) = 14,5

Buat Gantt Chart sederhana: 
    
   
     | P1 | P2 | P3 | P4 |
     0    6    12   19   27
   


   - Perbandigan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS |8.75ms|14.75 ms| Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF |8.5 ms|14.5 ms| Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |







4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

---

## Hasil Eksekusi
Perhitungan FCFS dan SJF Menggunakan Excel.

![Screenshot hasil](<screenshots/Screenshot 2025-11-05 175937.png>)

---

## Analisis
- Perbandingan hasil rata-rata WT dan TAT antara FCFS & SJF. 
## SJF 
- rata-rata Waiting Time (SJF)= 8,5ms
- rata-rata Turnaround Time (SJF) = 14,5ms

## SCFS
- Avg Waiting Time (FCFS) = 8.75ms
- Avg Turnaround Time (FCFS) = 14.75ms

- Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  

| Aspek                  | FCFS                        | SJF                                 |
| :--------------------- | :-------------------------- | :---------------------------------- |
| Jenis penjadwalan      | Non-preemptive              | Bisa preemptive atau non-preemptive |
| Dasar pemilihan proses | Urutan kedatangan           | Perkiraan waktu CPU burst           |
| Rata-rata waiting time | Bisa tinggi (*convoy effect*) | Minimum (optimal secara teori)      |
| Starvation             | Tidak ada                   | Mungkin terjadi                     |
| Implementasi           | Sederhana                   | Butuh estimasi burst time           |


- Tambahkan kesimpulan singkat di akhir laporan.

---

## Kesimpulan
- FCFS (First Come, First Served) merupakan algoritma penjadwalan paling sederhana karena proses dieksekusi sesuai urutan kedatangannya tanpa interupsi.
- SJF (Shortest Job First) memilih proses dengan waktu eksekusi (CPU burst) terpendek terlebih dahulu, sehingga menghasilkan rata-rata waktu tunggu yang paling rendah secara teori.
- FCFS unggul dalam keadilan dan kemudahan implementasi, namun dapat menimbulkan convoy effect yang membuat proses pendek menunggu lama di belakang proses panjang.
- SJF lebih efisien dari sisi performa CPU, tetapi sulit diterapkan karena membutuhkan estimasi waktu CPU burst dan berpotensi menyebabkan starvation pada proses panjang.
- Secara umum, FCFS cocok untuk sistem sederhana atau real-time, sedangkan SJF lebih sesuai untuk sistem batch di mana waktu eksekusi proses dapat diprediksi.

---


### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
![Screenshot hasil](<screenshots/Screenshot 2025-11-05 191234.png>)

2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  


     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS |8.75ms|14.75 ms| Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF |8.5 ms|14.5 ms| Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |


3. Analisis kelebihan dan kelemahan tiap algoritma. 

| Algoritma |  Kelebihan |  Kelemahan |
| :--------- | :----------- | :----------- |
| **FCFS (First Come, First Served)** | - Sederhana dan mudah diimplementasikan (menggunakan struktur queue FIFO).<br>- Adil secara urutan kedatangan — proses dijalankan sesuai waktu datang.<br>- Tidak menyebabkan starvation, semua proses pasti dijalankan. | - Rata-rata waktu tunggu bisa tinggi (*convoy effect*), terutama jika proses panjang datang lebih dulu.<br>- Tidak efisien untuk sistem interaktif atau multitasking karena proses panjang dapat memblokir lainnya.<br>- Tidak ada prioritas berdasarkan kebutuhan waktu eksekusi. |
| **SJF (Shortest Job First)** | - Memberikan waktu tunggu rata-rata minimum (*optimal secara teori*).<br>- Efisien dalam sistem batch, meningkatkan throughput.<br>- Mengurangi waktu turnaround total dibanding FCFS. | - Sulit diterapkan secara praktis karena memerlukan estimasi waktu CPU burst yang akurat.<br>- Dapat menyebabkan starvation pada proses panjang jika proses pendek terus datang.<br>- Kurang cocok untuk sistem interaktif atau real-time karena tidak memperhatikan keadilan. |




### Jawaban

1. FCFS (First Come First Served)
Urutan eksekusi: P1 → P2 → P3 → P4

Waiting Time (WT):

P1 = 0 (langsung jalan)
P2 = 7 - 2 = 5 ms (mulai setelah P1 selesai)
P3 = 11 - 4 = 7 ms
P4 = 12 - 5 = 7 ms

Turnaround Time (TAT) = WT + Burst Time (BT)
P1 = 0 + 7 = 7 ms
P2 = 5 + 4 = 9 ms
P3 = 7 + 1 = 8 ms
P4 = 7 + 4 = 11 ms
Rata-rata waiting time = (0+5+7+7)/4 = 4.75 ms
Rata-rata turnaround time = (7+9+8+11)/4 = 8.75 ms


## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?    
   **Jawaban:**  FCFS (First Come, First Served) dan SJF (Shortest Job First) adalah cara penjadwalan prosesnya. FCFS menjadwalkan proses berdasarkan urutan kedatangan, artinya proses yang datang lebih dulu akan dilayani lebih dulu tanpa interupsi. Sebaliknya, SJF memprioritaskan proses dengan waktu eksekusi (burst time) terpendek, sehingga proses dengan durasi paling singkat akan dilayani terlebih dahulu, yang dapat meminimalkan rata-rata waktu tunggu. FCFS bersifat non-preemptive dan sederhana, namun bisa menyebabkan waktu tunggu lama terutama jika proses awal memerlukan waktu eksekusi lama (efek konvoi). SJF juga biasanya non-preemptive, tetapi memiliki varian preemptive yang disebut Shortest Remaining Time First (SRTF) dan dikenal sebagai algoritma yang lebih optimal karena mengurangi rata-rata waktu tunggu dan meningkatkan efisiensi sistem.

2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
   **Jawaban:** SJF (Shortest Job First) bisa buat waktu tunggu rata-rata menjadi minimal karena proses yang paling cepat selesai akan dilayani duluan. Jadi, proses yang lama akan menunggu lebih singkat, sehingga keseluruhan waktu tunggu semua proses jadi lebih kecil secara rata-rata. Ini membantu sistem berjalan lebih efisien dan proses selesai cepat. 

3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?    
   **Jawaban:**  Kelemahan SJF kalau dipakai di sistem interaktif adalah sulit untuk menebak berapa lama sebuah proses akan berjalan. Selain itu, proses yang butuh waktu lama bisa terus menunggu kalau selalu ada proses baru yang lebih cepat. Jadi, proses lama bisa sering tertunda dan sistem jadi kurang adil dan responsif untuk pengguna.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? minggu ini, lebih rumit dari minggu sebellumnya, saya butuh beberapa hari untuk menyelesaikannya
- Bagaimana cara Anda mengatasinya? cara saya mengatasi kerumitan ini, adalah dengan research dari beberapa sumber untuk dapat menyesaikan tugas ini 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
