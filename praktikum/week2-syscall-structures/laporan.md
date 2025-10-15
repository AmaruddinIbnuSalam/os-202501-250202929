
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
2. **Eksperimen 2 – Menelusuri System Call File I/O**
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
- **Dari analisis saya tentang percobaan yang telah saya lakukakan yaitu:**
1. Menujukan cara sistem call berfungsi sebagai media komunikasi antara kernel dan aplikasi 
2. Menjunjukan mekanisme proses kernel memecahkan proses open, read,write, dan close.
3. kernel menunjukan log  yang berisi tantang bagaimana kernel dan layanan sistem menangangi berbagai runtime termasuk error,operasi I/O dan Managemen memori. informasi dari log ini sangat penting untuk sistem untuk menjalankan troubleshooting dengan baik.

- **Hubungan hasil dengan teori (fungsi kernel, system call, arsitektur OS) yaitu:**
1. Fungsi kernel adalah sebagai inti dari sistem operasi yang mengatur semua sumber daya hardware seperti CPU, memori, dan perangkat I/O,dan kernel juga menjembatan antara I/o dengan aplikasi agar berjalan lancar dan terkoordinasi dengan baik. Dalam percobaan, kernel menjalankan tugas membuka file (/etc/passwd), mengalokasikan memori untuk membaca, menulis data ke output, dan menutup file dari proses cat. Log kernel juga mencatat aktivitas penting seperti kegagalan koneksi layanan dan operasi file system, yang merupakan contoh nyata fungsi kernel dalam mengelola perangkat dan layanan sistem.
2. Sistem call berfungsi sebagai media komunikasi antara kernel dan aplikasi. Dalam percobaan, command strace memonitor semua system call terkait operasi file seperti open, read, write, dan close. Ini adalah cara aplikasi meminta layanan kernel, misalnya membuka file, membaca isi, atau output ke layar, yang kernel proses dengan aman dan efisien.​
3. Linux memiliki arsitektur dimana kernel beroperasi pada mode kernel yang memiliki akses penuh ke hardware, sedangkan aplikasi berjalan di mode user. System call berfungsi sebagai penghalang keamanan agar aplikasi tidak langsung mengakses hardware,Dalam Percobaan menampilkan bagaimana data bergerak dari aplikasi ke kernel dan kembali ke output user dengan mengikuti komunikasi system call dan peran kernel dalam manajemen sumber daya.
- **perbedaan hasil di lingkungan OS berbeda (Linux vs Windows) yaitu:**
1. Kernel dan System Call: Linux menggunakan kernel monolitik dengan system call yang standar dan terbuka, sehingga bisa dipantau dengan tools seperti strace dan dmesg. Windows menggunakan kernel hybrid dan system call-nya berbeda, sehingga tracing dan log dilakukan dengan tools lain yang lebih kompleks.
2. Logging dan Output: Output di Linux biasanya berupa log kernel dan system call yang detail dan berbasis teks. Di Windows, log lebih terintegrasi dengan GUI dan memakai event viewer serta tools Sysinternals, sehingga tampilannya berbeda.
3. Lisensi dan Fleksibilitas: Linux bersifat open source sehingga pengguna bisa melihat, memodifikasi, dan mengontrol kernel dan system call. Windows adalah proprietary sehingga kontrol dan akses terbatas. 

---

## Kesimpulan
sistem operasi linux dan windows memiliki perbedaan pada struktur mekanisme system call dan cara mereka mengolah sumber daya  serta proses,
linux menggunakan kernel monolitic yang terbuka dan berbasis POSIX dengan sistem call yang bisa di trace secara rinci, sehingga memiliki fleksibilitas dan transparasi yang tinggi untuk memantau sistem dan debuggin. 
Serta Windows memakai kernel hybrid dengan system call berbeda dan menggunakan alat monitoring yang berbeda pula, lebih terintegrasi dengan GUI.


---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
- yang paling menantang minggu ini
masih kurang paham tentang arti dari log dari hasil perintah satu sampai 3 soalnya di punya saya hasilnya banyak tulisan close,saya tidak tahu apa itu mengalami kesalahan atau emang seperti itu.
  
- Bagaimana cara Anda mengatasinya?
cara mengatasinya bertanya pada ai dan menganalisa yang saya tau saya.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
