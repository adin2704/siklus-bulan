from collections import deque

jadwal = deque()

def tambah_jadwal(fase):
    jadwal.append(fase)
    print(f"Fase {fase} ditambahkan ke jadwal")

def proses_jadwal():
    if jadwal:
        print("Memproses fase:", jadwal.popleft())
    else:
        print("Jadwal fase kosong")

def tampilkan_jadwal():
    print("\n=== JADWAL FASE BULAN ===")
    if jadwal:
        for fase in jadwal:
            print(fase)
    else:
        print("Jadwal kosong")


tambah_jadwal("Bulan Baru")
tambah_jadwal("Sabit Muda")
tambah_jadwal("Perbani Awal")

tampilkan_jadwal()
proses_jadwal()
tampilkan_jadwal()