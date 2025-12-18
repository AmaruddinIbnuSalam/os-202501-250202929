CONSTANT N ← 5                // jumlah filsuf
SEMAPHORE fork[N] ← {1,1,1,1,1}

PROCESS philosopher(i):
    left  ← i
    right ← (i + 1) mod N

    LOOP FOREVER:
        print("Philosopher", i, "is thinking")
        THINK for random time

        print("Philosopher", i, "tries to pick LEFT fork", left)
        WAIT(fork[left])          // mengambil garpu kiri

        print("Philosopher", i, "tries to pick RIGHT fork", right)
        WAIT(fork[right])         // mengambil garpu kanan → POTENSI DEADLOCK

        print("Philosopher", i, "is eating")
        EAT for random time

        SIGNAL(fork[left])        // meletakkan garpu kiri
        SIGNAL(fork[right])       // meletakkan garpu kanan

        print("Philosopher", i, "finished eating")
    END LOOP
END PROCESS


// Memulai semua proses filsuf
FOR i FROM 0 TO N-1:
    START PROCESS philosopher(i)
END FOR
