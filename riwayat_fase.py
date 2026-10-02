riwayat = []

def tambah_fase(fase):
    riwayat.append(fase)
    print(f"Fase {fase} ditambahkan ke riwayat")

def hapus_fase():
    if riwayat:
        print("Fase dihapus:", riwayat.pop())
    else:
        print("Riwayat fase kosong")

def tampilkan_riwayat():
    print("\n=== RIWAYAT FASE BULAN ===")
    if riwayat:
        for fase in reversed(riwayat):
            print(fase)
    else:
        print("Riwayat kosong")


tambah_fase("Bulan Baru")
tambah_fase("Sabit Muda")
tambah_fase("Perbani Awal")

tampilkan_riwayat()
hapus_fase()
tampilkan_riwayat()