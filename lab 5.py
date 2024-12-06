# Program untuk mengelola daftar nilai mahasiswa
# Inisialisasi daftar data mahasiswa
data_mahasiswa = []
def tambah(nama, nilai):
    """Fungsi untuk menambah data mahasiswa."""
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print(f"Data mahasiswa dengan nama {nama} telah ditambahkan.")

def tampilkan():
    """Fungsi untuk menampilkan semua data mahasiswa."""
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Nilai Mahasiswa:")
        for i, data in enumerate(data_mahasiswa, start=1):
            print(f"{i}. Nama: {data['nama']}, Nilai: {data['nilai']}")
def hapus(nama):
    """Fungsi untuk menghapus data mahasiswa berdasarkan nama."""
    for data in data_mahasiswa:
        if data["nama"] == nama:
            data_mahasiswa.remove(data)
            print(f"Data mahasiswa dengan nama {nama} telah dihapus.")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")
def ubah(nama, nilai_baru):
    """Fungsi untuk mengubah data mahasiswa berdasarkan nama."""
    for data in data_mahasiswa:
        if data["nama"] == nama:
            data["nilai"] = nilai_baru
            print(f"Data mahasiswa dengan nama {nama} telah diperbarui.")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")
# Contoh penggunaan fungsi
while True:
    print("\nMenu:")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Hapus Data Mahasiswa")
    print("4. Ubah Data Mahasiswa")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        tambah(nama, nilai)
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        nilai_baru = float(input("Masukkan nilai baru: "))
        ubah(nama, nilai_baru)
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
