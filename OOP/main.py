from data.mahasiswa import Mahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

def main():
    mahasiswa = Mahasiswa()
    while True:
        pilihan = input("[(L)ihat (T)ambah (U)bah (H)apus (K)eluar] : ").lower()

        if pilihan == 'l':
            ViewMahasiswa.tampilkan_data(mahasiswa)
        elif pilihan == 't':
            nim, nama, tugas, uts, uas = InputForm.input_data()
            mahasiswa.tambah_data(nim, nama, tugas, uts, uas)
        elif pilihan == 'u':
            nim, nama, tugas, uts, uas = InputForm.input_ubah_data()
            mahasiswa.ubah_data(nim, nama, tugas, uts, uas)
        elif pilihan == 'h':
            nim = input("Masukkan NIM yang akan dihapus: ")
            mahasiswa.hapus_data(nim)
        elif pilihan == 'k':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()