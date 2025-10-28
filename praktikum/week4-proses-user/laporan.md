
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : AMARUDDIN IBNU SALAM  
- **NIM**   : 250202929  
- **Kelas** : 1IKRA

---

## Tujuan
etelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.

---

## Dasar Teori

- ## Proses di Linux
Proses adalah program yang sedang berjalan. Setiap proses punya ID unik (PID) dan bisa dikontrol dengan perintah seperti ps, top, dan kill. Semua proses berasal dari systemd atau init sebagai induknya.

- ## User di Linux
Linux mendukung banyak pengguna (multi-user).
Setiap user punya nama (username), ID (UID), dan folder pribadi (home).

- ## User & Keamanan Sistem
Setiap user punya hak akses berbeda agar tidak bisa merusak sistem.
User root punya akses penuh dan harus digunakan dengan hati-hati, semua ini bertujuan untuk menjaga keamanan sistem.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```

---


## Hasil Eksekusi
- ## Hasil Percobaan 1 

![Hasil screenshot](<screenshots/hasil percobaan.png>)
- ## Hasil Percobaan 2
<img width="1919" height="1079" alt="Hasil percobaan ke-2" src="https://github.com/user-attachments/assets/363c855b-c0e5-458f-a92a-2405cef9735b" />

---
 ## Analisis
 ## 1. hasil semua perintah dan penjelasan 
`whoami` Fungsi: Menampilkan nama user yang sedang login dan aktif di terminal saat ini.
``` bash
mrcley
```
Contoh output: `mrcley`
Artinya user yang sedang digunakan untuk menjalankan terminal adalah `mrcley`.

`id`
Fungsi: Menampilkan informasi lengkap tentang identitas user, termasuk:
- UID (User ID): Nomor unik untuk user.
- GID (Group ID): Nomor unik grup utama user.
- Groups: Daftar semua grup yang diikuti user.
``` bash 
uid=1000(mrcley) gid=1000(mrcley) groups=1000(mrcley),27(sudo)
```
contoh ouput: `uid=1000(mrcley) gid=1000(mrcley) groups=1000(mrcley),27(sudo)` Artinya user mrcley memiliki UID dan GID 1000, dan termasuk dalam grup mrcley serta sudo (grup dengan hak akses administrator).

`groups`
Fungsi: Menampilkan daftar nama grup yang diikuti oleh user saat ini.

```bash
mrcley sudo
```
contoh output :`mrcley sudo` Artinya user mrcley termasuk dalam grup mrcley (grup utama) dan sudo (memiliki izin untuk menjalankan perintah administratif).

## 2. Tabel PID, USER, %CPU, %MEM, COMMAND 

| Kolom       | Arti                       | Penjelasan                                                                                                                    |
| ----------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **PID**     | Process ID                 | Nomor unik yang diberikan sistem untuk setiap proses. Digunakan untuk mengontrol atau menghentikan proses (misal `kill PID`). |
| **USER**    | User name                  | Nama user yang menjalankan proses tersebut (misal `root`, `mrcley`).                                                      |
| **%CPU**    | Persentase penggunaan CPU  | Menunjukkan berapa banyak CPU yang digunakan oleh proses itu. Nilai tinggi berarti proses tersebut sedang aktif/berat.        |
| **%MEM**    | Persentase penggunaan RAM  | Menunjukkan berapa persen memori (RAM) yang dipakai proses itu. Semakin besar, semakin banyak memori yang digunakan.          |
| **COMMAND** | Nama perintah atau program | Menunjukkan **perintah** atau **aplikasi** yang dijalankan. Misalnya: `sleep`, `bash`, `chrome`, `systemd`, dll.             |
## 3.
- mrcley       404  0.0  0.0   3124  1664 pts/0    S    19:39   0:00 sleep 1000
- mrcley       406  0.0  0.0   4088  1920 pts/0    S+   19:39   0:00 grep --color=auto sleep
## 4.
- Amati Hierarki Proses
Setiap indentasi menunjukkan hubungan induk–anak.
Misalnya:
systemd(1) adalah proses induk tertinggi (root of process tree).
NetworkManager(725), sshd(830), gdm3(900), dll. adalah anak dari systemd(1).

- Identifikasi Proses Induk (init atau systemd)
Di sistem modern (Ubuntu, Fedora, Debian, dsb.), proses induk utama adalah systemd(1).
Di sistem Linux lama (mis. SysV init), akan tertulis init(1).
Proses dengan PID = 1 selalu merupakan induk dari semua proses lain di sistem Linux.

---

## Kesimpulan
Dalam Linux, setiap program berjalan dengan ID unik (PID) dan dapat dikontrol oleh user, Manajemen user penting untuk membatasi hak akses dan menjaga keamanan sistem, Dengan perintah seperti ps, top, dan kill, kita bisa memantau dan mengatur proses yang berjalan,Dan Semua proses berasal dari systemd/init, dan pengaturan user yang baik membuat sistem lebih aman dan teratur.

---  
## Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.  
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.
## Jawaban
1.  Penjelasan hasil perintah 

| No | Perintah                      | Fungsi Utama                     | Kesimpulan                                    |                                       |
| -- | ----------------------------- | -------------------------------- | --------------------------------------------- | ------------------------------------- |
| 1  | `ps aux`                      | Menampilkan semua proses         | Melihat proses aktif di sistem                |                                       |
| 2  | `pstree -p`                    | head -20`                        | Menampilkan hierarki proses                   | Melihat hubungan induk–anak proses    |
| 3  | `sleep 1000 &`                | Menjalankan proses di background | Membuat proses berjalan tanpa blokir terminal |                                       |
| 4  | `ps aux`                       | grep sleep`                      | Menyaring proses berdasarkan nama             | Mencari proses spesifik               |
| 5  | `Kill 710`                    | Salah perintah (`K` besar)       | Tidak dikenali oleh sistem                    |                                       |
| 6  | `kill 710`                    | Menghentikan proses              | Mengakhiri proses dengan PID tertentu         |                                       |
| 7  | `pas aux`                      | grep sleep`                      | Salah ketik perintah                          | Menimbulkan error “command not found” |
| 8  | `[1]+  Terminated sleep 1000` | Output sistem                    | Proses background dihentikan                  |                                       |
| 9  | `pstree`                      | Menampilkan struktur proses      | Menunjukkan `systemd` sebagai induk utama     |                                       |

2. - ## Diagram Hirarki Proses
![Hasil screenshot](<screenshots/Diagram hirarki proses.png>)

3. Hubungan antara user management dan keamanan sistem Linux adalah bahwa pengelolaan pengguna yang baik memastikan setiap user memiliki hak akses sesuai kebutuhannya, sehingga mencegah penyalahgunaan dan menjaga keamanan sistem.
  

## Quiz
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?  
   **Jawaban:**  init berfungsi untuk menjalankan starup secara berurutan layanan sistem operasi dan Fungsi systemd meliputi menginisialisasi layanan secara paralel untuk mempercepat proses booting, mengelola dependensi layanan secara otomatis, serta menyediakan kontrol dan monitoring layanan yang lebih efisien. 
2. Apa perbedaan antara `kill` dan `killall`?  
   **Jawaban:**  Code `Kill` hanya digunakan untuk terminate satu proses yang sedang berjalan sedangkan `killall` digunakan untuk terminate semua proses yang sedang berjalan tanpa kecuali.
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?  
   **Jawaban:**  karena dibutuhkan untuk menjalankan operasi yang mempengaruhi seluruh sistem 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
Bagian yang paling menantang minggu ini adalah saat mencoba memahami bagaimana proses bekerja di Linux, terutama ketika harus melihat hierarki proses dengan pstree dan menghentikan proses tertentu dengan kill. Awalnya saya cukup bingung karena hasil yang muncul banyak dan terlihat rumit
- Bagaimana cara Anda mengatasinya?  
Saya mengatasinya dengan mencoba beberapa kali menjalankan perintah yang sama sambil mencatat hasilnya. Saya juga mencari penjelasan tambahan dari internet dan berdiskusi dengan teman untuk memastikan pemahaman saya benar. Setelah beberapa kali praktik, saya mulai lebih paham bagaimana cara membaca struktur proses dan mengelola proses di terminal. Rasanya cukup memuaskan setelah berhasil memahami hal yang awalnya terasa rumit.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

