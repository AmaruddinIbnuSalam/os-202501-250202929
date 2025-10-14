
# Laporan Praktikum Minggu 1
Topik : Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Amaruddin Ibnu Salam   
- **NIM**   : 250202929  
- **Kelas** : 1IKRA

---

## Tujuan
 Setelah mengikuti praktikum mahasiswa diharapkan mampu: 
- Menjelaskan dan memahami Komponen - komponen utama system operasi
- Mengenal jenis-jenis arsitektur kernel
- Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
- apat menggambarkan diagram sederhana arsitektur OS 
---

## Dasar Teori
Sistem operasi adalah perangkat lunak yang mengontrol dan mengatur perangkat keras komputer serta menjalankan program aplikasi.
Sistem ini bertindak sebagai penghubung antara pengguna dengan perangkat keras  (system call), memungkinkan komputer berfungsi dan program dapat berjalan dengan baik, dengan bagian terpenting nya adalah kernel yang mengelolah sumber daya CPU,Memory,Storage (hardisk) dan I/O

---

## Langkah Praktikum
1. **Setup Environment**

- Pastikan Linux (Ubuntu/WSL) sudah terinstal.
- Pastikan Git sudah dikonfigurasi dengan benar:

```bash
git config --global user.name "Nama Anda"
git config --global user.email "email@contoh.com"
```
2. **Diskusi Konsep**

- Baca materi pengantar tentang komponen OS.
- Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar** Jalankan perintah berikut di terminal:

```bash
uname -a
whoami
lsmod | head
dmesg | head
```

Catat dan analisis modul kernel yang tampil.

4. Membuat Diagram Arsitektur

- Buat diagram hubungan antara User → System Call → Kernel → Hardware.
- Gunakan draw.io atau Mermaid.
Simpan hasilnya di:

```bash
praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
```
5. Penulisan Laporan

- Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
- Tambahkan screenshot hasil terminal ke folder `screenshots/`.
6. Commit & Push

```bash
git add .
git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
git push origin main
```

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
    ![hasil Screeenshot Ubuntu](screenshots/Screenshot%20Terminal%20%202025-10-09%20221425.png)
    ![hasil Screenshot Diagram Arsitecture](<Diagram arsitektur OS.png>)
---

## Analisis

- Hasil nya adalah Dengan Virtual machine Ubuntu/WSl kita dapat menggunakan/menjalankan Linux tanpa membuat dual boot, dan hasil Experimen perintah saya berhasil menjalan kan Linux 
- Hasil terminal tersebut merefleksikan konsep penting dalam teori sistem operasi, yaitu fungsi kernel, system call, dan arsitektur OS modern:
Fungsi Kernel

   - Managemen sumber daya (PU, memori, perangkat keras) dan menjalankan proses
   - Modul kernel di hasil lsmod menunjukkan bagian kernel yang bisa dimuat sesuai kebutuhan sistem, seperti virtualisasi (kvm_intel), manajemen daya, serta perangkat keras lain.​​`hasil Screeenshot Ubuntu`

System Call

Perintah seperti dmesg mengakses log kernel yang dihasilkan melalui system call, yaitu mekanisme komunikasi antara user space (aplikasi/perintah) dan kernel. Dengan system call, aplikasi dapat meminta layanan kernel seperti akses perangkat keras, file system, dan memori, yang semuanya dicatat/dilaporkan di log kernel.

Arsitektur OS

Arsitektur sistem operasi ini menggunakan Ubuntu, di mana Linux berjalan sebagai mesin virtual ringan dengan kernel asli di dalam Windows. Sistem ini seperti menggunakan kontainer, di mana kernel Linux mengatur sumber daya dan ruang kerja, sementara proses berjalan terpisah satu sama lain. Hal ini terlihat dari informasi kernel dan modul yang berjalan seperti di sistem Linux asli. Ini menunjukkan contoh arsitektur OS modern yang mendukung virtualisasi, keamanan, dan pemakaian sumber daya yang efisien
---

## Kesimpulan
 - Praktikum membuktikan bahwa kernel Linux pada Ubuntu berjalan optimal dan mampu mendeteksi serta mengelola Sumber daya hardware (CPU, RAM) secara efisien sesuai peran inti kernel dalam sistem operasi.
 - Penggunaan perintah dasar ini melatih keterampilan analisa sistem dan pemahaman penerapan konsep arsitektur OS, kernel, dan system call secara nyata di lingkungan hybrid Windows-Linux menggunakan Ubuntu.


---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi  
   **Jawaban:**  
   - Manajemen Proses : mengatur dan mengolah proses yang berjalan di dalam komputer, dan termasuk mengatur daya dan core CPU dengan efisien. 
   - Manajemen Memory : mengatur pembagian RAM untuk aplikasi software yang sedang berjalan agar stabil.
   - Manajemen Storage dan I/O : mengolah penyimpanan, mengakses file , serta  mengontrol perangkat keras yang terhubung dengan menyediakan drivers agar dapat di gunakan dengan oleh aplikasi/software

2. Jelaskan perbedaan antara kernel mode dan user mode 
   **Jawaban:**  
   - Kernel mode memiliki hak ases penuh terhadap perangkat keras dan sistem operasi sehingga dapat menjalankan perintah sensitif dengan resiko mengilangkan stabilitas sistem operasi atau perangkat kerasa yang digunakan
   - user mode memiliki akses yang terbatas untuk menjaga kestabilan sistem operasi tersebut. 
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel
   **Jawaban:**  
   - Contoh OS pada Monolithic : Linux, MS-DOS, dan Unix Tradisional

   - Contoh OS pada Microkernel : Minix, QNX, dan Mach

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
yang pertama adalah menginstal dan mengsetup ubuntu Dipc pribadi saya yang eror terus , dan melakukan commit github menggunakan Visual Studio itu lumayan sulit dan ribet mungkin karena ini hal pertama saya melakukannya? tapi overall menarik untuk di pelajari lebih lanjut  
- Bagaimana cara Anda mengatasinya?
cara saya menengatasi semua kesulitan tersebut yaitu dengan mencari satu persatu yang masalah saat penginstalan ubuntu menganalisa dan tanya ke chatgpt atau google mengatasinya.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
