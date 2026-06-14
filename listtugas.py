# aplikasi manajemen nilai mahasiswa

data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90],
    ["Dewi", 72],
    ["Eko", 88]
]

while True:
    # tampilkan menu
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")
    print("====================================")
    pilihan = input("Pilih menu 1-8 : ")

    # menu 1 - tampilkan data
    if pilihan == "1":
        print("\n--- Daftar Mahasiswa ---")
        print(f"{'No':<5} {'Nama':<20} {'Nilai'}")
        print("-" * 35)
        for i in range(len(data_mahasiswa)):
            print(f"{i+1:<5} {data_mahasiswa[i][0]:<20} {data_mahasiswa[i][1]}")
        print(f"\nTotal mahasiswa : {len(data_mahasiswa)} orang")

    # menu 2 - tambah data
    elif pilihan == "2":
        nama_baru = input("\nMasukkan nama mahasiswa : ")
        nilai_baru = int(input("Masukkan nilai mahasiswa : "))
        data_mahasiswa.append([nama_baru, nilai_baru])
        print(f"Data '{nama_baru}' berhasil ditambahkan!")

    # menu 3 - ubah data
    elif pilihan == "3":
        print("\n--- Daftar Mahasiswa ---")
        for i in range(len(data_mahasiswa)):
            print(f"{i+1}. {data_mahasiswa[i][0]} - {data_mahasiswa[i][1]}")
        nomor = int(input("Masukkan nomor data yang diubah : "))
        nama_ubah = input("Masukkan nama baru : ")
        nilai_ubah = int(input("Masukkan nilai baru : "))
        data_mahasiswa[nomor-1][0] = nama_ubah
        data_mahasiswa[nomor-1][1] = nilai_ubah
        print(f"Data nomor {nomor} berhasil diubah!")

    # menu 4 - hapus data
    elif pilihan == "4":
        print("\n--- Daftar Mahasiswa ---")
        for i in range(len(data_mahasiswa)):
            print(f"{i+1}. {data_mahasiswa[i][0]} - {data_mahasiswa[i][1]}")
        nomor = int(input("Masukkan nomor data yang dihapus : "))
        nama_hapus = data_mahasiswa[nomor-1][0]
        data_mahasiswa.pop(nomor-1)
        print(f"Data '{nama_hapus}' berhasil dihapus!")

    # menu 5 - cari data
    elif pilihan == "5":
        cari = input("\nMasukkan nama yang dicari : ")
        daftar_nama = []
        for mhs in data_mahasiswa:
            daftar_nama.append(mhs[0])
        if cari in daftar_nama:
            posisi = daftar_nama.index(cari)
            print(f"Data ditemukan!")
            print(f"Nama  : {data_mahasiswa[posisi][0]}")
            print(f"Nilai : {data_mahasiswa[posisi][1]}")
            print(f"Index ke : {posisi}")
        else:
            print(f"Data '{cari}' tidak ditemukan!")

    # menu 6 - urutkan data berdasarkan nilai
    elif pilihan == "6":
        print(f"\nData awal : {data_mahasiswa}")
        data_mahasiswa.sort(key=lambda x: x[1])
        data_mahasiswa.reverse()
        print(f"\n--- Data Diurutkan (Nilai Tertinggi) ---")
        print(f"{'No':<5} {'Nama':<20} {'Nilai'}")
        print("-" * 35)
        for i in range(len(data_mahasiswa)):
            print(f"{i+1:<5} {data_mahasiswa[i][0]:<20} {data_mahasiswa[i][1]}")

    # menu 7 - hitung rata-rata
    elif pilihan == "7":
        total = 0
        for mhs in data_mahasiswa:
            total = total + mhs[1]
        rata_rata = total / len(data_mahasiswa)
        daftar_nilai = []
        for mhs in data_mahasiswa:
            daftar_nilai.append(mhs[1])
        daftar_nilai.sort()
        print(f"\n--- Statistik Nilai ---")
        print(f"Total nilai   : {total}")
        print(f"Rata-rata     : {rata_rata:.2f}")
        print(f"Nilai terendah: {daftar_nilai[0]}")
        print(f"Nilai tertinggi: {daftar_nilai[-1]}")

    # menu 8 - keluar
    elif pilihan == "8":
        print("\nTerima kasih, program selesai!")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1-8!")