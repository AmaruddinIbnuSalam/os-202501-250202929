# **Perbedaan Monolithic Kernel, Microkernel dan layered architecture**

Dari Ketiga artitecture ini memiliki keunggulan dan kekurangan masing-masing.

**Monolithic kernel** 
Keseluruhan layanan os seperti managemen proses, memory, I/O, device drivers kernel ini Berjalan dalam satu kernel space,
yang menjadikan kecepatan komunikasi antar komponen menjadi cepat dan efisien, namun monolitthic kernel ini memiliki kekurangan yaitu
ukuran yang sangat besar dan kompleks karena semua layanan ada dalam satu kernel space yang sama.

**Micro kernel** 
Berbeda dengan kernel sebelumnya kernel,layanan yang berada pada kernel space hanya yang fungsional seperti(managemen memori, manajemen proses/thread, dan komunikasi antar proses/IPC)
