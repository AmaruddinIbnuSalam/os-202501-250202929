
# Laporan Praktikum Minggu 4
Topik: Manajemen File dan Permission di Linux 

---

## Identitas
- **Nama**  : AMARUDDIN IBNU SALAM  
- **NIM**   : 250202929
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori
- **Ownership**: Setiap file dimiliki oleh user dan grup tertentu.
- **Kategori Pengguna**: Permission diberikan untuk owner, group, dan others.
- **Jenis Hak Akses**: Read (baca), Write (tulis), Execute (jalankan).
- **Representasi**: Permission bisa dilihat dalam format simbolik (rwx) atau angka (0-7).
- **Keamanan**: Permission mengontrol akses dan menjaga keamanan file di sistem.
---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```

## Hasil Eksekusi
<img width="1919" height="1079" alt="hasil percobaan teminal linux fs permision" src="https://github.com/user-attachments/assets/3dccd02a-ee37-4b47-aa0d-c481f9a8d308" />


---

## Analisis
- Jelaskan makna hasil percobaan.
  Perintah yang di jalanakan berfungsi sebagai berikut:
  `pwd`  perntintah untuk  mengetahui directory yang sedang aktif `/home/levi`
  `ls -l` perintah untuk menampilkan format panjang.
  `cd/ /tmp` perintah mengubah directory aktif ke /tmp.
  `ls -a` perintah `-a` pada `ls` adalah untuk menampilkan semua file  termasuk file yang tersembunyi di directory
  penjelasan dari perintah `cat /etc/passwd | head -n 5`

- Username – Nama pengguna untuk login, misalnya `root`.
- Password – Biasanya berisi `x` yang menandakan password disimpan secara aman di file `/etc/shadow`.
- UID (User ID) – Nomor identifikasi unik pengguna, 0 biasanya untuk root.
- GID (Group ID) – Nomor grup awal pengguna.
- GECOS – Biasanya berisi informasi deskriptif seperti nama lengkap.
- Home Directory – Direktori utama pengguna, contohnya `/root`.
- Login Shell – Program shell yang dijalankan saat login, misalnya `/bin/bas`

  perbedaan sebelum dan sesudah cdmod
  pada awalnya file `percobaan.txt` memiliki hak akses `-rw-r--r--`
  dan setelah di cdmod `percobaan.txt` menjadi berubah memikili hak akses `-rw-------`
  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
## Tugas

1.Tabel Observasi
| Perintah                         | Fungsi                                              | Hasil / Output                                                      |
|---------------------------------|----------------------------------------------------|-------------------------------------------------------------------|
| `pwd`                           | Menampilkan direktori kerja saat ini                | /home/mrcley                                                      |
| `ls -l`                        | Menampilkan isi direktori dengan format panjang     | total 0 (tidak ada file di /home/mrcley)                         |
| `cd /tmp`                      | Pindah direktori aktif ke /tmp                       | -                                                                 |
| `ls -a`                        | Menampilkan semua file termasuk tersembunyi di /tmp | . .. .X11-unix snap-private-tmp systemd-private-...               |
| `cat /etc/passwd \| head -n 5` | Menampilkan 5 baris pertama dari file /etc/passwd   | root:x:0:0:root:/root:/bin/bash dan 4 baris pengguna berikutnya  |
| `echo "<AMARUDDIN IBNU SALAM><250202929>" > percobaan.txt` | Membuat file percobaan.txt dengan isi teks       | -                                                                 |
| `ls -l percobaan.txt`          | Menampilkan hak akses dan info file percobaan.txt   | -rw-r--r-- 1 mrcley mrcley 34 Oct 22 19:56 percobaan.txt         |
| `chmod 600 percobaan.txt`      | Mengubah hak akses file menjadi hanya pemilik baca/tulis | -rw------- 1 mrcley mrcley 34 Oct 22 19:56 percobaan.txt          |
| `sudo chown root percobaan.txt`| Mengubah pemilik file menjadi root                   | -rw------- 1 root mrcley 34 Oct 22 19:56 percobaan.txt            |
| `ls -l percobaan.txt`          | Menampilkan status akhir file percobaan.txt          | -rw------- 1 root mrcley 34 Oct 22 19:56 percobaan.txt            |

Jelaskan fungsi tiap perintah dan arti kolom permission (rwxr-xr--)
1. rwx (Owner/Pemilik): pemilik file bisa membaca (r), menulis (w), dan menjalankan (x) file.
2. r-x (Group/Grup): anggota grup bisa membaca (r) dan mengeksekusi (x) file, tapi tidak bisa menulis.
3. r-- (Others/Pengguna lainnya): pengguna lain hanya bisa membaca file saja tanpa boleh menulis atau mengeksekusi.
   
Analisis peran chmod dan chown dalam keamanan sistem Linux.   
kedua perintah ini membangun mekanisme kontrol akses yang kuat, mendukung prinsip keamanan seperti prinsip least privilege (hak akses minimum) dan menjaga integritas serta kerahasiaan data di sistem Linux.

---

## Kesimpulan
Setiap file di Linux memiliki pemilik (owner) dan grup yang mengatur siapa yang boleh mengakses file tersebut. Permission adalah aturan yang menentukan apa yang bisa dilakukan oleh pemilik, grup, dan pengguna lain terhadap file, seperti membaca, menulis, dan mengeksekusi. Sistem permission ini penting untuk menjaga keamanan dan mencegah akses ilegal ke file atau data di dalam sistem. Perintah chmod digunakan untuk mengatur hak akses, sedangkan chown mengatur pemilik file.

Intinya, permission dan ownership bekerja sama untuk mengelola akses dan menjaga keamanan file di Linux.

---

## Quiz
1. Apa fungsi dari perintah `chmod`? 
   **Jawaban:**  fungsi chmod adalah untuk mengubah hak asses directory untuk meningkatkan keamanan atau mengatur akses pengguna
2. Apa arti dari kode permission `rwxr-xr--`? 
   **Jawaban:**  jika kode permission file `rwxr-xr--` pemilik file mendapat kontrol prenuh, anggota grup hanya bisa membaca dan menjalankan file dan pengguna lain hanya bisa membaca file tersebut.
3. Jelaskan perbedaan antara `chown` dan `chmod`. 
   **Jawaban:**  chown berguna untuk mengubah kepemilikan file, sedangkan chmod untuk mengatur hak akses apa saja yang bisa di lakukan oleh pemilik dan pengguna lain terhadap file yang mereka punya. keduanya memiliki fungsi yang penting dalam pengelolahan keamanan dan kontrol akses file di system linux, chmod dan chown biasanya hanya bisa di jalankan oleh root/ pengguna dengan hak istimewa.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini, adalah saya akhirnya saya berhasil menjalankan 3 percobaan yang di tugaskan tanpa ada error,
- Bagaimana cara Anda mengatasinya?
  karena saya tidak mengalami masalah dari percobaan yang saya lakukan jadi saya menganalisan dan mencari di internet tentang masuk percobaan tersebut.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
