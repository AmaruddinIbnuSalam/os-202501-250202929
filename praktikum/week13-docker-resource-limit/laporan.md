
# Tugas Praktikum Minggu 13  
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : AMARUDDIN IBNU SALAM 
- **NIM**   : 250202929 
- **Kelas** : IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
1. **Docker Container** adalah virtual mesin yang ringan yang bisa untuk menjalankan aplikasi secara di background, dengan berbagi kernel sistem operasi host 
2. **Resource Limit** adalah untuk membatasi penggunaan CPU dan Memori container agar tidak menggangu container lain.
3. 'docker stats' di gunakan untuk melihat **Monitoring resource** doker
4. Doker memmakai control grup di linux buat mengatur dan batasi sumber daya CPU dan memori

## Langkah Praktikum
1. Memastikan Docker telah terinstal dan berjalan dengan baik pada sistem.
2. Membuat program uji sederhana berbasis Python untuk menguji penggunaan CPU dan memori.
3. Menulis Dockerfile untuk menjalankan program uji tersebut di dalam container.
4. Melakukan build image Docker menggunakan Dockerfile.
5. Menjalankan container tanpa pembatasan resource.
6. Menjalankan container dengan pembatasan CPU dan memori.
7. Mengamati perbedaan hasil eksekusi serta penggunaan resource.
8. Melakukan commit dan push hasil praktikum ke repository GitHub.

---
Strukture folder
week13-docker-resource-limit
 ┣ code
 ┃ ┗ projeck-docker
 ┃ ┃ ┣ app.py
 ┃ ┃ ┣ Dockerfile
 ┃ ┃ ┗ requirements.txt
 ┣ screenshots
 ┃ ┣ docker_stats.png
 ┃ ┣ ssstrestestcpunonlimit.png
 ┃ ┣ sstestcpudenganlimit.png
 ┃ ┗ sstestmemoridenganlimit.png
 ┗ laporan.md

## Kode / Perintah

```
Perintah utama yang digunakan dalam praktikum:

- Pertama buka teminal untuk Monitoring resource 

``` bash
docker stats

```
- Lalu buka teminal ke 2  pada folder code/projeck-docker
dan menjalankan command ini untuk build image docker
```bash 
docker build -t week13-resource-limit 
```
- Setelah telah image docker terbuat lalu jalankan docker dengan non limit 

```bash
docker run --rm week13-resource-limit
```
- Untuk menjalankan docker dengan limit dengan cpu 0.5 dan memori 256mb 
```bash

docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```
- 


---

## Hasil Eksekusi
screenshot hasil percobaan docker
![docker stats](screenshots/docker_stats.png)
![ss stres test cpu non limit](<screenshots/ssstrestestcpunonlimit.png>)
pada screenshot hasil percobaan ini menampilkan jika docker di jalankan pada tanpa limit/non limit cpu used mencapai 100% dan proses dapat di selesaikan dengan 44 detik setelah itu lanjut menjalankan memori test dengan nilai uji sampai 500mb dan alokasi pemakaian nya 10mb per detik, dapat dijalankan tanpa ada eror dan kehabisan resource  memori yang menandakan docker berhasil menjalankan stress test cpu dan testing memori dengan baik.
pada screenshot hasil percobaan ini menampilkan docker menjalankan memori test dengan nilai uji sampai 500mb dan alokasi pemakaian nya 10mb per detik, dapat dijalankan tanpa ada eror dan kehabisan resource  memori 
![ss test cpu dengan limit](screenshots/sstestmemoridenganlimit.png)
![ss test memori dengan limit](<screenshots/sstestcpudenganlimit.png>)
pada screenshot hasil percobaan ini menampilkan jika docker dijalankan dengan cpu yang di limit 0.5, yang terjadi cpu used yang di gunakan hanya 50% dan proses diselesaikan dengan waktu yang lebih lama yaitu 85 detik, docker menjalankan test memori dengan limit 256mb, yang terjadi adalah alokasi berhenti pada saat resource  memori menyentuh 256mb 

## Analisis
Analisis saya pada container yang di jalankan tanpa batasan resource,program 
dapat menggunakan cpu dan memori tanpa batasan yang menyebabkan kecepatan eksekusi program berjalan dengan lebih cepat dan  penggunaan ram meningkat terus. Namun ketika container di jalan kan dengan limit CPU 0,5 ( setengan dari inti cpu host ) dan memori 256MB, karena konfigurasi ini memori dibatasi dan proses eksekusi program berjalan sangat lambat.
Jika program  mencoba menggunakan resource memori melebihi batas container akan mengalami eror atau di hentikan oleh sistem. ini menunjukan bahwa docker secara efektif menerapkan Resource Limit menggunakan control gruoup.


## Kesimpulan
1. Docker memungkinkan melakukan pembatasan resource CPU dan Memori pada container secara efektif
2. Menerapkan Resource Limit sangat penting untuk menjaga kestabilan container 
3. Pembatasan resource mencegah satu program menghabiskan resource sistem yang membuat error atau crash.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?  
   **Jawaban:** Agar penggunaan resource lebih terkontrol dan tidak mengganggu container atau proses lain pada sistem.
2. Apa perbedaan VM dan container dalam konteks isolasi resource?  
   **Jawaban:** VM memiliki sistem operasi sendiri dan menggunakan hypervisor, sedangkan container berbagi kernel host dan menggunakan cgroups untuk isolasi resource sehingga lebih ringan. 
3. Apa dampak limit memori terhadap aplikasi yang boros memori?  
   **Jawaban:**  Aplikasi dapat mengalami error, berjalan lambat, atau dihentikan ketika penggunaan memori melebihi batas yang ditentukan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? Memahami cara kerja pembatasan resource CPU dan memori pada container.
- Bagaimana cara Anda mengatasinya? Membaca dokumentasi Docker dan melakukan percobaan langsung dengan berbagai konfigurasi limit resource.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
