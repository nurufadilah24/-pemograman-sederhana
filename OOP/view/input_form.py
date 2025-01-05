class InputForm:
    @staticmethod
    def input_data():
            nim = input("NIM: ")
            nama = input("Nama: ")
            tugas = float(input("Nilai Tugas: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))
            return nim, nama, tugas, uts, uas

    @staticmethod
    def input_ubah_data():
            nim = input("Masukkan NIM: ")
            print("Masukkan data baru (tekan Enter jika tidak ingin mengubah):")
            nama = input("Nama: ").strip() or None
            tugas = input("Nilai Tugas: ").strip()
            tugas = float(tugas) if tugas else None
            uts = input("Nilai UTS: ").strip()
            uts = float(uts) if uts else None
            uas = input("Nilai UAS: ").strip()
            uas = float(uas) if uas else None
            return nim, nama, tugas, uts, uas