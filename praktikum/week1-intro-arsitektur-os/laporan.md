# **Perbedaan Monolithic Kernel, Microkernel dan Layered Architecture**


Dari Ketiga artitecture ini memiliki keunggulan dan kekurangan masing-masing, 

 ## 1. Monolithic kernel 
kernel yang Keseluruhan komponen OS (managemen proses, memori, I/O, device drivers) Berjalan dalam satu kernel space,
yang menjadikan kecepatan komunikasi antar komponen menjadi cepat dan efisien, namun monolitthic kernel ini memiliki kekurangan, yaitu karena ukuran yang sangat besar dan kompleks dan jika ada satu device driver bermasalah seluruh kernel dan system bisa crash.

 ### Contoh
* Linux (termasuk Android).
* UNIX.
* FreeBSD, OpenBSD.
* MS-DOS.

## 2. Micro kernel
kernel ini memiliki ukuran kecil dan minimalis, karena komponen os yang berada pada kernel space (manajemen memori, manajemen proses/thread, dan komunikasi antar proses/IPC),speed pengiriman pesan relatif lebih lama dari monolithic karena melalui IPC. Keunggulan Micro kernel lebih stabil dari monolithic kernel jika ada kegagalan layanan di user space tidak akan mempengaruhi kernel.

### Contoh
* Mach (digunakan sebagai dasar untuk kernel-hybrid).
* MINIX.
* QNX.
* L4.

  
## 3. Layered Architecture
Struktur system ini dibagi menjadi beberapa lapisan dan setiap lapisan hanya berinteraksi dengan lapisan di atas dan di bawahnya menciptakan stuktur yang modular dan terorganisir, umumnya lapisannya (Hardware layer, Kenel, Device Drivers, I/O, User Programs, User interface shell/GUI), keamanan dan kestabilan layered architecture jika ada kelalahan disatu lapisan tidak langung memperngaruhi seluruh sistem dan kinerja bisa lebih lambat jika desaint antar lapisan tidak efisien

### Contoh
* THE Operating System (oleh Dijkstra).
* Multics.
* Windows NT (menggunakan arsitektur berlapis dengan komponen hybrid).

# **Analisis Tentang Model Kernel Yang Paling Relevan Untuk Sistem Modern** 
kernel yang paling relevan untuk sistem modern yaitu hybrid kernel yang menggabungkan kernel monolithic kernel dan micro kernel,atau layerd architekture untuk sekarang sistem modern tidak menggunakan satu model murni, melainkan menggabungkan kelebihan dari setiap model 
### Contoh
* Windows NT: mengkombinasikan microkernel dan monolicthic
* MacOS(XNU) : berdasarkan mach, MacOS mengkombinasikan micro kenel, monolithic dan Driver Modular.
* Linux : Secara teknis monolithic, tapi sudah sangat modular dan mendukung loadable kernel modules (LKM), mirip pendekatan layered
