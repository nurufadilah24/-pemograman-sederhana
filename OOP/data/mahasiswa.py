class Mahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def lihat_data(self):
        if not self.data_mahasiswa:
            print("Daftar Nilai")
            print("=" * 81)
            print(f"{'No'.center(5)}|{'Nama'.center(15)}|{'NIM'.center(10)}|{'Nilai Tugas'.center(13)}|{'Nilai UTS'.center(10)}|{'Nilai UAS'.center(10)}|{'Nilai Akhir'.center(10)}|")
            print("=" * 81)
            print(f"{'TIDAK ADA DATA'.center(75)}")
            print("=" * 81)
            return
        print("Daftar Nilai")
        print("=" * 81)
        print(f"{'No'.center(5)}|{'Nama'.center(15)}|{'NIM'.center(10)}|{'Nilai Tugas'.center(13)}|{'Nilai UTS'.center(10)}|{'Nilai UAS'.center(10)}|{'Nilai Akhir'.center(10)}|")
        print("=" * 81)
        for i, (nim, mhs) in enumerate(self.data_mahasiswa.items(), start=1):
            print(f"{str(i).center(5)}|{mhs['nama'].ljust(15)}|{nim.center(10)}|{str(mhs['tugas']).center(13)}|{str(mhs['uts']).center(10)}|{str(mhs['uas']).center(10)}|{format(mhs['nilai_akhir'], '.2f').center(10)}|")
        print("=" * 81)

    def tambah_data(self, nim, nama, tugas, uts, uas):
        nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        self.data_mahasiswa[nim] = {
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "nilai_akhir": nilai_akhir
        }
        print("Data berhasil ditambahkan!")

    def ubah_data(self, nim, nama=None, tugas=None, uts=None, uas=None):
        if nim not in self.data_mahasiswa:
            print("Data dengan NIM tersebut tidak ditemukan!")
            return
        if nama:
            self.data_mahasiswa[nim]['nama'] = nama
        if tugas is not None:
            self.data_mahasiswa[nim]['tugas'] = tugas
        if uts is not None:
            self.data_mahasiswa[nim]['uts'] = uts
        if uas is not None:
            self.data_mahasiswa[nim]['uas'] = uas
        self.data_mahasiswa[nim]['nilai_akhir'] = (self.data_mahasiswa[nim]['tugas'] * 0.3 +
                                                   self.data_mahasiswa[nim]['uts'] * 0.35 +
                                                   self.data_mahasiswa[nim]['uas'] * 0.35)
        print("Data berhasil diubah!")

    def hapus_data(self, nim):
        if nim in self.data_mahasiswa:
            del self.data_mahasiswa[nim]
            print("Data berhasil dihapus!")
        else:
            print("Data dengan NIM tersebut tidak ditemukan!")