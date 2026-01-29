def lru_browser(tab_sequence, kapasitas):
    memory = []
    hit = 0
    fault = 0

    print("\n" + "="*40)
    print(" SIMULASI LRU BROWSER ".center(40))
    print("="*40 + "\n")

    for tab in tab_sequence:
        if tab in memory:
            # HIT: Pindahkan tab yang baru diakses ke posisi paling akhir (paling baru)
            memory.remove(tab)
            memory.append(tab)
            hit += 1
            status = "HIT → Tab masih aktif (Refresh)"
        else:
            # PAGE FAULT: Tambahkan tab baru
            fault += 1
            if len(memory) >= kapasitas:
                # Hapus tab yang paling lama tidak digunakan (indeks 0)
                memory.pop(0)
            memory.append(tab)
            status = "PAGE FAULT → Tab di-reload"

        print(f"Membuka Tab : {tab}")
        print(f"Tab Aktif   : {memory}")
        print(f"Status      : {status}\n")

    print("=== HASIL AKHIR ===")
    print(f"Total Hit      : {hit}")
    print(f"Total Fault    : {fault}")
    total_akses = hit + fault
    print(f"Hit Ratio      : {round(hit / total_akses, 2) if total_akses > 0 else 0}")
    print("-" * 40)

def browser_scenario():
    # Skenario akses tab
    tab_akses = [
        "YouTube", "Instagram", "WhatsApp",
        "YouTube", "Instagram",
        "Chrome", "YouTube"
    ]
    kapasitas = 3
    lru_browser(tab_akses, kapasitas)