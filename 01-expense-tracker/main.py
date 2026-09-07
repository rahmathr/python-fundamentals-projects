daftar_pengeluaran = []

def tampilkan_daftar_pengeluaran(daftar_pengeluaran):
    for item in daftar_pengeluaran:
        print(f'Nama pengeluaran: {item["nama"]}')
        print(f'Jumlah pengeluaran: {item["jumlah"]}')
        print(f'Kategori pengeluaran: {item["kategori"]}\n')

def hitung_total_pengeluaran(daftar_pengeluaran):
    total = 0
    for item in daftar_pengeluaran:
        total += item["jumlah"]
    return total

def tambah_pengeluaran():
    nama_pengeluaran = input("Nama pengeluaran: ")
    while nama_pengeluaran == "":
        print("\nNama pengeluaran tidak boleh kosong.\n")
        nama_pengeluaran = input("Nama pengeluaran: ")
    jumlah = int(input("Jumlah pengeluaran: "))
    while jumlah <= 0:
        print("\nJumlah pengeluaran harus lebih dari 0.\n")
        jumlah = int(input("Jumlah pengeluaran: "))
    kategori = input("Kategori pengeluaran: ")
    while kategori == "":
        print("\nKategori pengeluaran tidak boleh kosong.\n")
        kategori = input("Kategori pengeluaran: ")
    data_pengeluaran = {
        "nama": nama_pengeluaran,
        "jumlah": jumlah,
        "kategori": kategori
    }
    daftar_pengeluaran.append(data_pengeluaran)
    print("\nPengeluaran berhasil ditambahkan!\n")

def cari_pengeluaran_berdasarkan_kategori(daftar_pengeluaran):
    kategori = input("Cari berdasarkan kategori pengeluaran: ")
    ditemukan = False
    for item in daftar_pengeluaran:
        if item["kategori"] == kategori:
            print(f'Nama pengeluaran: {item["nama"]}')
            print(f'Jumlah pengeluaran: {item["jumlah"]}')
            print(f'Kategori pengeluaran: {item["kategori"]}\n')
            ditemukan = True
    if not ditemukan:
        print(f'\nPengeluaran dengan kategori "{kategori}" tidak ditemukan.\n')

def hitung_total_berdasarkan_kategori(daftar_pengeluaran, kategori):
    total_pengeluaran_kategori = 0
    for item in daftar_pengeluaran:
        if item["kategori"] == kategori:
            total_pengeluaran_kategori += item["jumlah"]
    return total_pengeluaran_kategori

while True:
    print("=== EXPENSE TRACKER ===\n")
    print("1. Tambah pengeluaran")
    print("2. Lihat daftar pengeluaran")
    print("3. Hitung total pengeluaran")
    print("4. Hitung total berdasarkan kategori")
    print("5. Cari pengeluaran berdasarkan kategori")
    print("6. Keluar\n")
    pilihan_menu = int(input("Pilih menu: "))
    print("")
    if pilihan_menu == 1:
        tambah_pengeluaran()
    elif pilihan_menu == 2:
        tampilkan_daftar_pengeluaran(daftar_pengeluaran)
    elif pilihan_menu == 3:
        total = hitung_total_pengeluaran(daftar_pengeluaran)
        print(f'Total pengeluaran: Rp{total}\n')
    elif pilihan_menu == 4:
        kategori = input("Kategori pengeluaran: ")
        total_pengeluaran_kategori = hitung_total_berdasarkan_kategori(daftar_pengeluaran, kategori)
        print(f'\nTotal pengeluaran {kategori}: Rp{total_pengeluaran_kategori}\n')
    elif pilihan_menu == 5:
        cari_pengeluaran_berdasarkan_kategori(daftar_pengeluaran)
    elif pilihan_menu == 6:
        break
    else:
        print(f"Pilihan {pilihan_menu} tidak tersedia.\n")