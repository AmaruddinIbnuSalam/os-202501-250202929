
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

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
-dapat menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io/mermaid)
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Setup Environment**

- Pastikan Linux (Ubuntu/WSL) sudah terinstal.

- Jalankan perintah berikut di terminal:
```bash
uname -a
whoami
lsmod | head
dmesg | head
```

4. **Membuat Diagram Arsitektur**

- Buat diagram hubungan antara User → System Call → Kernel → Hardware.
- Gunakan draw.io atau Mermaid.
Simpan hasilnya di:
```
praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
```
**Penulisan Laporan**

Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam laporan.md.
Tambahkan screenshot hasil terminal ke folder screenshots/.
Commit & Push

git add .
git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
git push origin main


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
    ![hasil Screeenshot](screenshots/Screenshot%20Terminal%20%202025-10-09%20221425.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
