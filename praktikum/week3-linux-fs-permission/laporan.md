
# Laporan Praktikum Minggu [X]
Topik: Manajemen File dan Permission di Linux 

---

## Identitas
- **Nama**  : [Nama Mahasiswa]  
- **NIM**   : [NIM Mahasiswa]  
- **Kelas** : [Kelas]

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
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

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

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi dari perintah `chmod`? 
   **Jawaban:**  
2. Apa arti dari kode permission `rwxr-xr--`? 
   **Jawaban:**  
3. Jelaskan perbedaan antara `chown` dan `chmod`. 
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini, adalah saya akhirnya saya berhasil menjalankan 3 percobaan yang di tugaskan tanpa ada error,
- Bagaimana cara Anda mengatasinya?
  karena saya tidak mengalami masalah dari percobaan yang saya lakukan jadi saya menganalisan dan mencari di internet tentang masuk percobaan tersebut.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
