
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
### Pentingnya System Call untuk Keamanan OS
System call sangat penting dalam keamanan OS karena menjadi jembatan antara aplikasi user dan kernel, yang mengelola sumber daya hardware. Melalui system call, OS dapat mengontrol akses dan operasi yang dijalankan program, sehingga mencegah program user langsung mengakses perangkat keras atau memory secara sembarangan, yang bisa berisiko keamanan. OS menggunakan system call untuk menerapkan proteksi, validasi input, dan mengelola hak akses file serta resource lainnya sehingga hanya operasi yang sah yang dijalankan.

### Cara OS Menjamin Transisi User ke Kernel yang Aman
Saat sebuah system call dipanggil, CPU beralih dari mode user yang terbatas ke mode kernel yang memiliki hak akses penuh, menggunakan mode proteksi CPU. Proses ini melibatkan pengalihan konteks di mana parameter system call disalin, kondisi register disiapkan, dan eksekusi fungsi kernel dilakukan. Setelah selesai, CPU kembali ke mode user dengan aman. Karena itu, kode user tidak bisa menjalankan instruksi kernel secara langsung, menjaga integritas sistem.

### Contoh System Call Umum di Linux
Beberapa system call dasar di Linux yang sering dipakai adalah:
- open: membuka file
- read: membaca isi file
- write: menulis ke file atau perangkat
- close: menutup file
- fork: membuat proses baru
- execve: menjalankan program baru
- exit: mengakhiri proses

system call merupakan elemen kunci dalam menjaga keamanan dan kestabilan sistem operasi, karena menyediakan mekanisme terstruktur dan aman untuk mengelola sumber daya serta proses di tingkat kernel, yang esensial untuk mencegah akses ilegal dan menjaga integritas sistem secara keseluruhan.

## Hasil Observasi

### Tabel Observasi System Call (strace)
| Kategori       | Observasi System Call (`strace`)                                       | Penjelasan                                                                                  |
|--------------- |----------------------------------------------------------------------- |--------------------------------------------------------------------------------------------|
| open           | File descriptor (fd=3) digunakan untuk /etc/passwd                     | File /etc/passwd dibuka oleh kernel melalui system call open dan disimpan di fd=3           |
| read           | read(3, ..., nbyte) = jumlah_baca                                      | Kernel membaca isi file per blok byte (contoh 832, 2996, dst) secara bertahap              |
| write          | write(1, "isi...") ke stdout                                           | Proses cat menulis hasil baca ke layar melalui system call write                            |
| close          | close(3)                                                               | Setelah proses selesai, kernel menutup file descriptor untuk membebaskan resource           |
| Nilai Return   | Return 0 atau jumlah byte                                              | System call berhasil dijalankan ditandai return 0 atau jumlah byte yang diproses            |
| Proses         | Tidak ada fork/exec (hanya operasi I/O file)                           | Fokus pada open, read, write, close sebagai dasar manajemen file yang diamati               |

### Tabel Observasi System Call (`dmesg`)

| Kategori       | Observasi Log Kernel (`dmesg`)                                         | Penjelasan                                                                                  |
|--------------- |----------------------------------------------------------------------- |--------------------------------------------------------------------------------------------|
| Error          | "Failed to connect to bus: No such file or directory"                  | Gagal koneksi ke bus systemd, file/directory terkait layanan tidak ditemukan                |
| Audit          | "Collecting audit messages is disabled."                               | Aktivitas audit kernel/logging keamanan dimatikan                                           |
| Systemd Error  | "init failed to start within 10000ms"                                  | Subsystem WSL gagal menjalankan init sesuai batas waktu                                     |
| ACPI           | "AC Adapter (online)", "battery absent"                                | Status hardware daya terdeteksi; tidak ada baterai                                          |
| TCP Warning    | "Driver has suspect GRO implementation, TCP performance may be compromised." | Driver jaringan eth0 bermasalah, bisa berdampak pada performa TCP                          |

---

## Kesimpulan
System call merupakan jembatan antara aplikasi pengguna dan kernel sistem operasi yang memungkinkan proses berjalan dengan aman dan terkontrol. Melalui system call, OS dapat melakukan verifikasi hak akses program terhadap sumber daya seperti file, perangkat keras, dan memori, sehingga meningkatkan tingkat keamanan. Mekanisme ini mencegah aplikasi dari melakukan operasi yang tidak sah atau berbahaya, serta menjaga integritas sumber daya sistem.​

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
cara mengatasinya akhirnya saya pinjam device temen untuk mengerjakan.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
