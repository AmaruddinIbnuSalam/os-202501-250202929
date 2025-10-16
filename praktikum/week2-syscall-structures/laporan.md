
# Laporan Praktikum Minggu 2
Topik : Struktur System Call dan Fungsi Kernel

---

## Identitas
- **Nama**  : Amaruddin Ibnu Salam  
- **NIM**   : 250202929
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.
---

## Dasar Teori
Teori dasar yang mendasari percobaan menggunakan strace analisis log kernel dalam konteks ststem operasi linux (Ubuntu)
- Kernel sebagai Inti Sistem Operasi.
- Manajemen Proses dan Memori oleh Kernel.
- Logging Kernel untuk Monitoring Sistem.
- sistem cell sebagai penghubung komunikasi  kernel dan aplikasi.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan perintah `strace` dan `man` sudah terinstal.
   - Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

2. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
   > Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
   Simpan hasil analisis ke `results/syscall_ls.txt`.

3. **Eksperimen 2 – Menelusuri System Call File I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
   > Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

4. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
   > Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

5. **Diagram Alur System Call**
   - Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
   - Gunakan draw.io / mermaid.
   - Simpan di:
     ```
     praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
     ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   git push origin main
   ```

---

## Kode / Perintah
1. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
2. **Eksperimen 2 – Menelusuri System Call sFile I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```

3. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
---

## Hasil Eksekusi
- Hasil Screenshot Eksperimen 1
![ Hasil Screenshot Eksperimen 1](<command strace ls.png>)
![hasil Screenshot Eksperimen 1 part 2](<command strace ls 2.png>)
- Hasil Screenshot Eksperimen 2
![- Hasil Screenshot Eksperimen 2](<command strace -e trace=open,read,write,close cat etcpasswd.png>)
- Hasil Screenshot Eksperimen 3
![alt text](<dmesg  tail -n 10.png>)
---

## Analisis
Kernel adalah bagian inti dari sistem operasi yang mengelola komunikasi antara perangkat keras dan perangkat lunak komputer. Ketika sebuah program membuka file, kernel memberikan sebuah nomor identifikasi yang disebut file descriptor (seperti angka 3 dalam contoh) untuk mengakses file tersebut. Kernel kemudian bertugas membaca data dari file dan menempatkannya ke dalam memori agar program bisa menggunakannya. Setelah selesai, kernel menutup file descriptor itu sehingga sumber daya komputer bisa digunakan untuk kebutuhan lain. Proses buka, baca, dan tutup file ini diatur secara rapi oleh kernel untuk menjaga keamanan dan kestabilan sistem.

Berbeda dengan program biasa yang mengeluarkan output untuk pengguna, log kernel menunjukkan aktivitas internal sistem secara teknis, seperti pengelolaan hardware, kondisi driver, dan event sistem yang penting untuk memonitor kesehatan komputer. Log ini merekam semua kejadian penting di level sistem operasi yang berjalan "di balik layar" dan biasanya digunakan oleh administrator atau teknisi untuk memecahkan masalah.

---

## Kesimpulan
Jadi, kernel berperan sebagai pengendali utama agar semua perangkat keras dan program dapat berjalan bersama dengan efektif dan aman. Log kernel adalah catatan detail aktivitas kernel tersebut, berbeda dari output aplikasi yang lebih sederhana dan fokus ke kebutuhan pengguna langsung. Pemahaman ini membantu mengerti bagaimana komputer mengatur proses internal dan interaksi file secara efisien pada level sistem operasi.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?  
   **Jawaban:**  Sistem call berfungsi sebagai media komunikasi antara kernel dan aplikasi 
2. Sebutkan 4 kategori system call yang umum digunakan
   **Jawaban:**  Prosess control,file management,device management, information maintenance, communication
4. Mengapa system call tidak bisa dipanggil langsung oleh user program?  
   **Jawaban:**  sistem call tidak dapat di panggil langsung oleh user karena ada yang namanya user mode ysng membatasi aksen ke kernel untuk menjaga ke stabilan dan keamanan sistem operasi

---

## Refleksi Diri
- yang paling menantang minggu ini
masih kurang paham tentang arti dari log dari hasil perintah satu sampai 3 soalnya di punya saya hasilnya banyak tulisan close,saya tidak tahu apa itu mengalami kesalahan atau emang seperti itu.
  
- Bagaimana cara Anda mengatasinya?
cara mengatasinya bertanya pada ai dan menganalisa yang saya tau saya.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
