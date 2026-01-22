
from CPU import menu_SJF
def main():
    while True:
        print("\n" + "╔══════════════════════════════╗")
        print("║      MINI SIMULASI OS        ║")
        print("╠══════════════════════════════╣")
        print("║ 1. CPU Scheduling (SJF)      ║")
        print("║ 2. Page Replacement (LRU)    ║")
        print("║ 3. Keluar                    ║")
        print("╚══════════════════════════════╝")
        
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan =='1':
            menu_SJF()
        elif pilihan == '3':
            print("keluar dari program ")
            break
        else:
            print("error input silakan coba lagi")
            main()


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        # Menangani error jika dijalankan di Docker tanpa -it
        pass
    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa.")

            

