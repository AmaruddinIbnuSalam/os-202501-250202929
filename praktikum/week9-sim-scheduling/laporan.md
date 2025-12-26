
# Tugas Praktikum Minggu 9  
Topik: Simulasi Algoritma Penjadwalan CPU 

---

## Identitas
- **Nama**  : AMARUDDIN IBNU SALAM  
- **NIM**   : 250202929 
- **Kelas** : 1IKRA

---
## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.
---
Struktur folder 
```
praktikum/week9-sim-scheduling/
├─ code/
│  ├─ #Algoritma FCFS .py
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```

## Dataset Uji
dataset proses yang dingunakan sebagai berikut:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |
---

## Implementasi program
Program ini di buat menggunakan bahasa pyhton dan berjalan melalui terminal.Program Dapat menghitung *waiting time* dan *turnaround time* berdasarkan Algoritma yang di pakai adalah FCFS 
 Alur program:
 1. Menginput jumlah proses, arrival time ,brust time 
 2. Program mengimplementasikan algoritma FCFS 
 3. Hasil nya akan berupa tabel dan rata-rata *waiting time* dan Turnaround time*

## Hasil Eksekusi
Hasil simulasi  Algoritma FCFS
![Hasil simulasi FCFS](<screenshots/Hasil simulasi .png>)

---

## Analisis
Hasil simulasi dengan perhitungan dengan program seperti ini lebih effisien dan minim kesalahan dalam perhitungan.

---

## Kesimpulan
 kelebihan simulasi ini:
 - Cepat
 - Akurat
 - Bisa untuk dataset besar atau dengan jumlah Proses yang lebih banyak

 Kekurangan simulasi ini:
 - Tidak bisa berjalan secara real-time 
 - Belum mendukung preemtive scheduling 
---

## Quiz
1. Mengapa simulasi diperlukan? 

    Simulasi diperlukan untuk menguji kinerja algoritma secara otomatis,
    terutama pada dataset besar yang sulit dihitung secara manual.

2. Perbedaan simulasi dan manual 
    pada dataset besar?
    Pada dataset besar, simulasi jauh lebih cepat dan akurat dibandingkan
    perhitungan manual yang rentan kesalahan.

3. Algoritma mana yang lebih mudah diimplementasikan?

    FCFS lebih mudah diimplementasikan karena tidak memerlukan pemilihan
    proses berdasarkan burst time.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  karena saya tidak menguasai bahasa pemprograman sama sekali jadi saya tidak tau saya harus mulai dari mana dan apa yang harus saya tulus.
- Bagaimana cara Anda mengatasinya? cara saya untuk mengatasi kebingungan saya adalah dengan cara tanya ke ai untuk membantu untuk membuatkan code yang bisa saya pahami cara kerjanyanya code algoritma FCFS tersebut.  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
