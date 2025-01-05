# Project UAS Pemograman Sederhana Menginput Data Nilai Mahasiswa
## Link video
https://youtu.be/CZTXmx4825A?si=BO0Zx1yMI_OXAKdL
## Flowchart 
![Flowchart](/Flowchart1.jpg)
## penjelasan program
Berikut penjelasan lebih mendetail mengenai kode Python yang berfungsi untuk mengelola data mahasiswa, khususnya untuk data nilai tugas, UTS, UAS, dan nilai akhir:

### 1. **Pendeklarasian Kelas `Mahasiswa`**

Kelas `Mahasiswa` ini digunakan untuk mengelola data mahasiswa yang meliputi nilai tugas, UTS, UAS, dan nilai akhir, menggunakan beberapa metode untuk menambah, mengubah, melihat, dan menghapus data mahasiswa. Semua data mahasiswa disimpan dalam sebuah dictionary `data_mahasiswa` di dalam objek kelas ini.

### 2. **Metode `__init__(self)`**
   Metode ini adalah konstruktor yang digunakan untuk menginisialisasi objek kelas `Mahasiswa`. Di sini, sebuah dictionary kosong (`self.data_mahasiswa = {}`) dibuat untuk menyimpan data mahasiswa, di mana key adalah `nim` dan value-nya adalah sebuah dictionary yang berisi informasi tentang mahasiswa tersebut.

   ```python
   def __init__(self):
       self.data_mahasiswa = {}
   ```

### 3. **Metode `lihat_data(self)`**
   Metode ini digunakan untuk menampilkan semua data mahasiswa dalam format tabel.

   - **Jika tidak ada data**: 
     Jika dictionary `self.data_mahasiswa` kosong, maka akan menampilkan pesan bahwa tidak ada data yang tersedia.
   - **Jika ada data**: 
     Jika terdapat data mahasiswa, maka metode ini akan menampilkan data dalam format tabel yang terstruktur. Tabel ini mencakup kolom:
       - No (Nomor urut)
       - Nama mahasiswa
       - NIM
       - Nilai Tugas
       - Nilai UTS
       - Nilai UAS
       - Nilai Akhir (yang dihitung berdasarkan rumus tertentu)

   Format penataan tabel dilakukan dengan menggunakan `center()` untuk teks yang diselaraskan secara horizontal dan `ljust()` untuk teks yang rata kiri. Pada nilai akhir, menggunakan format untuk menampilkan dua angka desimal.

   ```python
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
   ```

### 4. **Metode `tambah_data(self, nim, nama, tugas, uts, uas)`**
   Metode ini digunakan untuk menambahkan data mahasiswa baru.

   - **Parameter**: `nim` (Nomor Induk Mahasiswa), `nama` (Nama mahasiswa), `tugas`, `uts`, dan `uas` adalah nilai yang dimiliki mahasiswa tersebut.
   - **Perhitungan Nilai Akhir**: Nilai akhir dihitung dengan formula:
     - Nilai Akhir = (Nilai Tugas * 0.3) + (Nilai UTS * 0.35) + (Nilai UAS * 0.35)
   - **Penambahan Data**: Data mahasiswa yang baru dimasukkan ke dalam dictionary `self.data_mahasiswa` dengan `nim` sebagai key, dan value-nya adalah dictionary berisi `nama`, `tugas`, `uts`, `uas`, dan `nilai_akhir`.
   
   Setelah data berhasil ditambahkan, akan muncul pesan "Data berhasil ditambahkan!".

   ```python
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
   ```

### 5. **Metode `ubah_data(self, nim, nama=None, tugas=None, uts=None, uas=None)`**
   Metode ini digunakan untuk mengubah data mahasiswa berdasarkan `nim`.

   - **Cek apakah data ada**: Jika `nim` yang diberikan tidak ditemukan di `self.data_mahasiswa`, maka akan muncul pesan "Data dengan NIM tersebut tidak ditemukan!".
   - **Pengubahan data**: Jika data ditemukan, maka setiap parameter yang diberikan (misalnya `nama`, `tugas`, `uts`, atau `uas`) akan mengupdate nilai yang bersangkutan dalam dictionary.
   - **Perhitungan ulang nilai akhir**: Setelah data diubah, nilai akhir mahasiswa dihitung ulang menggunakan rumus yang sama dengan metode `tambah_data`.
   
   Setelah data berhasil diubah, akan muncul pesan "Data berhasil diubah!".

   ```python
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
   ```

### 6. **Metode `hapus_data(self, nim)`**
   Metode ini digunakan untuk menghapus data mahasiswa berdasarkan `nim`.

   - **Cek apakah data ada**: Jika `nim` ditemukan dalam `self.data_mahasiswa`, maka data tersebut akan dihapus.
   - **Pesan jika data tidak ditemukan**: Jika `nim` tidak ada dalam dictionary, maka akan muncul pesan "Data dengan NIM tersebut tidak ditemukan!".
   
   Setelah data berhasil dihapus, akan muncul pesan "Data berhasil dihapus!".

   ```python
   def hapus_data(self, nim):
       if nim in self.data_mahasiswa:
           del self.data_mahasiswa[nim]
           print("Data berhasil dihapus!")
       else:
           print("Data dengan NIM tersebut tidak ditemukan!")
   ```

---

### Kesimpulan:

Kelas `Mahasiswa` ini berfungsi sebagai sistem sederhana untuk mengelola data mahasiswa yang terdiri dari nilai tugas, UTS, UAS, dan nilai akhir. Kelas ini menyediakan metode untuk:

- **Melihat data mahasiswa** yang sudah disimpan, dengan tampilan yang terstruktur.
- **Menambahkan data mahasiswa baru**.
- **Mengubah data mahasiswa yang sudah ada**.
- **Menghapus data mahasiswa** berdasarkan NIM.

Dengan menggunakan struktur data dictionary, kita bisa dengan mudah mengakses, memperbarui, dan menghapus data berdasarkan NIM mahasiswa.

Kode yang Anda berikan berisi dua metode statis (`@staticmethod`) dalam kelas `InputForm`. Kedua metode ini digunakan untuk menangani input data dari pengguna melalui terminal (CLI), yaitu untuk memasukkan data mahasiswa baru dan mengubah data mahasiswa yang sudah ada. Mari kita jelaskan kode tersebut secara rinci.

### 1. **Metode `input_data()`**
   Metode ini digunakan untuk meminta input data dari pengguna yang diperlukan untuk membuat entri data mahasiswa baru. Input yang diminta adalah:
   - **NIM (Nomor Induk Mahasiswa)**: Sebuah string yang merepresentasikan identitas mahasiswa.
   - **Nama**: Nama lengkap mahasiswa.
   - **Nilai Tugas**: Nilai yang diberikan untuk tugas.
   - **Nilai UTS**: Nilai Ujian Tengah Semester (UTS).
   - **Nilai UAS**: Nilai Ujian Akhir Semester (UAS).

   **Langkah-langkah**:
   - Menggunakan fungsi `input()` untuk mendapatkan input dari pengguna.
   - Nilai tugas, UTS, dan UAS dikonversi menjadi angka desimal (tipe data `float`) menggunakan fungsi `float()`. Ini diperlukan karena nilai-nilai tersebut bisa berupa angka dengan koma.
   - Setelah semua input diterima, data tersebut dikembalikan dalam bentuk tuple yang berisi: `nim`, `nama`, `tugas`, `uts`, dan `uas`.

   **Contoh Implementasi**:

   ```python
   @staticmethod
   def input_data():
       nim = input("NIM: ")  # Meminta input NIM
       nama = input("Nama: ")  # Meminta input Nama
       tugas = float(input("Nilai Tugas: "))  # Meminta input Nilai Tugas dan mengubahnya menjadi float
       uts = float(input("Nilai UTS: "))  # Meminta input Nilai UTS dan mengubahnya menjadi float
       uas = float(input("Nilai UAS: "))  # Meminta input Nilai UAS dan mengubahnya menjadi float
       return nim, nama, tugas, uts, uas  # Mengembalikan data dalam bentuk tuple
   ```

   **Fungsi**:
   - Meminta input dari pengguna untuk membuat data mahasiswa baru.
   - Mengembalikan tuple yang berisi data mahasiswa, yang nantinya bisa digunakan untuk menambah data ke dalam sistem.

### 2. **Metode `input_ubah_data()`**
   Metode ini digunakan untuk meminta input data yang akan mengubah data mahasiswa yang sudah ada. Pengguna diberi opsi untuk mengubah data tertentu atau membiarkannya kosong (dengan menekan `Enter`), dan jika tidak ada perubahan, nilai tersebut akan diatur menjadi `None`.

   **Langkah-langkah**:
   - Pertama, metode ini meminta `NIM` mahasiswa yang datanya ingin diubah.
   - Kemudian, untuk setiap data (nama, nilai tugas, nilai UTS, nilai UAS), pengguna diberi opsi untuk memasukkan data baru. Jika pengguna tidak ingin mengubah data tersebut, mereka cukup menekan tombol `Enter` dan nilai tersebut akan diatur menjadi `None`.
   - Untuk nilai tugas, UTS, dan UAS, input kosong akan diubah menjadi `None`, sedangkan jika ada nilai yang dimasukkan, input tersebut akan diubah menjadi tipe data `float`.

   **Contoh Implementasi**:

   ```python
   @staticmethod
   def input_ubah_data():
       nim = input("Masukkan NIM: ")  # Meminta NIM untuk mahasiswa yang akan diubah datanya
       print("Masukkan data baru (tekan Enter jika tidak ingin mengubah):")  # Petunjuk untuk pengguna
       nama = input("Nama: ").strip() or None  # Jika nama kosong, set menjadi None
       tugas = input("Nilai Tugas: ").strip()  # Input nilai tugas
       tugas = float(tugas) if tugas else None  # Jika ada nilai, ubah ke float, jika kosong set None
       uts = input("Nilai UTS: ").strip()  # Input nilai UTS
       uts = float(uts) if uts else None  # Jika ada nilai, ubah ke float, jika kosong set None
       uas = input("Nilai UAS: ").strip()  # Input nilai UAS
       uas = float(uas) if uas else None  # Jika ada nilai, ubah ke float, jika kosong set None
       return nim, nama, tugas, uts, uas  # Mengembalikan data yang telah diubah dalam bentuk tuple
   ```

   **Fungsi**:
   - Meminta input dari pengguna untuk mengubah data mahasiswa yang sudah ada.
   - Jika pengguna tidak ingin mengubah data tertentu (misalnya nama, nilai tugas, UTS, atau UAS), mereka cukup menekan `Enter`, dan data yang tidak diubah akan diatur ke `None`.
   - Mengembalikan data mahasiswa yang sudah diubah dalam bentuk tuple, yang nantinya bisa digunakan untuk memperbarui data di sistem.

### **Perbedaan Antara Kedua Metode**:
- **`input_data()`**: Digunakan untuk memasukkan data baru mahasiswa ke dalam sistem. Semua input wajib diisi, terutama nilai tugas, UTS, dan UAS yang harus berupa angka (konversi ke tipe `float`).
- **`input_ubah_data()`**: Digunakan untuk mengubah data mahasiswa yang sudah ada. Jika pengguna tidak ingin mengubah nilai tertentu, mereka cukup menekan `Enter`, dan data tersebut akan tetap `None`.

### **Contoh Penggunaan**:
1. **Menambah Data Mahasiswa Baru**:
   - Anda akan memanggil `input_data()` untuk mengumpulkan data mahasiswa baru. Setelah data dikumpulkan, Anda bisa memprosesnya lebih lanjut (misalnya untuk ditambahkan ke database atau sistem lainnya).
   
   ```python
   nim, nama, tugas, uts, uas = InputForm.input_data()
   ```

2. **Mengubah Data Mahasiswa yang Sudah Ada**:
   - Jika Anda ingin mengubah data mahasiswa yang sudah ada, Anda akan memanggil `input_ubah_data()`. Pengguna dapat memilih untuk mengubah sebagian atau seluruh data mahasiswa.
   
   ```python
   nim, nama, tugas, uts, uas = InputForm.input_ubah_data()
   ```

### **Kesimpulan**:
Kelas `InputForm` menyediakan dua metode statis yang memudahkan interaksi dengan pengguna untuk mengumpulkan dan mengubah data mahasiswa:
1. **`input_data()`**: Digunakan untuk menambahkan data mahasiswa baru dengan mengumpulkan NIM, nama, nilai tugas, UTS, dan UAS.
2. **`input_ubah_data()`**: Digunakan untuk mengubah data mahasiswa yang sudah ada, dengan opsi untuk membiarkan beberapa data kosong (tidak diubah).

Kedua metode ini sangat berguna dalam aplikasi berbasis terminal yang membutuhkan input interaktif dari pengguna.
Kode yang Anda berikan mendefinisikan sebuah kelas bernama `ViewMahasiswa` dengan satu metode statis (`@staticmethod`), yaitu `tampilkan_data(mahasiswa)`. Mari kita jelaskan kode tersebut secara rinci:

### Kelas `ViewMahasiswa`

Kelas `ViewMahasiswa` bertujuan untuk menangani tampilan (view) dari data mahasiswa, dengan memisahkan logika pemrosesan data dari logika tampilan. Hal ini adalah penerapan prinsip **separation of concerns** dalam pengembangan perangkat lunak, yang membuat kode lebih terstruktur dan mudah dipelihara.

### Metode Statis `tampilkan_data(mahasiswa)`

#### 1. **Decorator `@staticmethod`**:
   - **`@staticmethod`** digunakan untuk mendeklarasikan metode ini sebagai metode statis. Ini berarti metode ini dapat dipanggil tanpa memerlukan objek dari kelas `ViewMahasiswa` terlebih dahulu. Metode ini tidak bergantung pada atribut atau status objek kelas `ViewMahasiswa` itu sendiri. Cukup dengan parameter yang diberikan (dalam hal ini objek `mahasiswa`), metode ini bisa langsung dipanggil.

#### 2. **Parameter `mahasiswa`**:
   - Parameter `mahasiswa` di sini adalah **objek** dari kelas yang memiliki data mahasiswa (misalnya, objek kelas `Mahasiswa`), yang diharapkan memiliki metode `lihat_data()`. 
   - Dalam konteks kode yang lebih besar, `mahasiswa` adalah objek yang menyimpan dan mengelola data mahasiswa seperti NIM, nama, nilai tugas, UTS, UAS, dll.

#### 3. **`mahasiswa.lihat_data()`**:
   - Di dalam metode `tampilkan_data()`, ada pemanggilan metode `lihat_data()` pada objek `mahasiswa`. 
   - `lihat_data()` diharapkan merupakan metode yang ada di dalam kelas `Mahasiswa` (atau kelas lain yang terkait) yang bertanggung jawab untuk **menampilkan data** mahasiswa. Biasanya, ini akan mencetak atau mengembalikan daftar data mahasiswa, misalnya dalam bentuk tabel atau daftar format tertentu.

### Contoh Implementasi:

Untuk lebih memahami bagaimana ini bekerja, berikut adalah contoh implementasi sederhana yang menggabungkan kelas `ViewMahasiswa` dengan kelas `Mahasiswa`:

```python
# Kelas Mahasiswa yang berfungsi untuk menyimpan dan menampilkan data mahasiswa
class Mahasiswa:
    def __init__(self):
        # Data mahasiswa disimpan dalam dictionary
        self.data_mahasiswa = {}

    def lihat_data(self):
        # Menampilkan data mahasiswa dalam format yang terstruktur
        if not self.data_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            print("Daftar Mahasiswa:")
            for nim, data in self.data_mahasiswa.items():
                print(f"NIM: {nim}, Nama: {data['nama']}, Nilai Akhir: {data['nilai_akhir']}")

    def tambah_data(self, nim, nama, nilai_akhir):
        # Menambahkan data mahasiswa baru
        self.data_mahasiswa[nim] = {"nama": nama, "nilai_akhir": nilai_akhir}
        print(f"Data mahasiswa dengan NIM {nim} telah ditambahkan.")

# Kelas ViewMahasiswa yang berfungsi untuk menampilkan data mahasiswa
class ViewMahasiswa:
    @staticmethod
    def tampilkan_data(mahasiswa):
        # Memanggil metode lihat_data() dari objek mahasiswa untuk menampilkan data
        mahasiswa.lihat_data()

# Membuat objek mahasiswa dan menambahkan data
mahasiswa = Mahasiswa()
mahasiswa.tambah_data("12345", "John Doe", 85.5)
mahasiswa.tambah_data("67890", "Jane Smith", 90.0)

# Menampilkan data mahasiswa menggunakan kelas ViewMahasiswa
ViewMahasiswa.tampilkan_data(mahasiswa)
```

### Penjelasan:

1. **Kelas `Mahasiswa`**:
   - Kelas ini menyimpan data mahasiswa dalam sebuah dictionary `data_mahasiswa`, dengan `nim` sebagai key dan nilai berupa dictionary yang berisi nama dan nilai akhir.
   - Metode `lihat_data()` akan menampilkan daftar mahasiswa dengan informasi seperti NIM, nama, dan nilai akhir.
   - Metode `tambah_data()` digunakan untuk menambahkan data mahasiswa ke dalam dictionary `data_mahasiswa`.

2. **Kelas `ViewMahasiswa`**:
   - Kelas ini hanya memiliki satu metode statis, `tampilkan_data(mahasiswa)`, yang memanggil metode `lihat_data()` dari objek `mahasiswa` untuk menampilkan data mahasiswa. 
   - Karena metode ini statis, kita tidak perlu membuat objek `ViewMahasiswa` untuk memanggilnya; kita bisa langsung memanggil `ViewMahasiswa.tampilkan_data(mahasiswa)`.

### Output:

```
Data mahasiswa dengan NIM 12345 telah ditambahkan.
Data mahasiswa dengan NIM 67890 telah ditambahkan.
Daftar Mahasiswa:
NIM: 12345, Nama: John Doe, Nilai Akhir: 85.5
NIM: 67890, Nama: Jane Smith, Nilai Akhir: 90.0
```

### **Kesimpulan**:

- **Fungsi Kelas `ViewMahasiswa`**: Kelas ini bertugas untuk **menampilkan data mahasiswa** dengan cara yang terpisah dari logika data itu sendiri. Dengan pendekatan ini, Anda dapat memisahkan **tampilan (view)** dari **logika data (model)**, yang merupakan prinsip dasar dalam desain perangkat lunak yang baik (misalnya, dalam pola arsitektur Model-View-Controller atau MVC).
  
- **Metode Statis**: Penggunaan `@staticmethod` memungkinkan kita untuk memanggil metode `tampilkan_data()` tanpa harus membuat instance dari kelas `ViewMahasiswa`. Metode ini hanya memerlukan objek `mahasiswa` yang berisi data yang ingin ditampilkan.

Dengan demikian, `ViewMahasiswa.tampilkan_data(mahasiswa)` memfasilitasi tampilan data mahasiswa dengan memanggil metode `lihat_data()` pada objek `mahasiswa` yang sesuai.
Kode yang Anda berikan adalah implementasi program berbasis **Command Line Interface (CLI)** untuk mengelola data mahasiswa. Program ini memungkinkan pengguna untuk melakukan berbagai operasi, seperti melihat, menambah, mengubah, dan menghapus data mahasiswa. Program ini terstruktur dengan baik, memisahkan logika data, input, dan tampilan ke dalam beberapa kelas yang terpisah, yang mengikuti prinsip pemrograman berorientasi objek (OOP).

### Penjelasan Detail Kode:

#### 1. **Import Modul**
   Di awal kode, ada tiga perintah `import` yang mengimpor kelas-kelas yang diperlukan dari modul lain:

   ```python
   from data.mahasiswa import Mahasiswa
   from view.input_form import InputForm
   from view.mahasiswa import ViewMahasiswa
   ```

   - `from data.mahasiswa import Mahasiswa`: Mengimpor kelas `Mahasiswa` yang terdapat dalam modul `mahasiswa` di folder `data`. Kelas ini bertanggung jawab untuk menangani data mahasiswa, seperti menambah, mengubah, menghapus, dan melihat data mahasiswa.
   - `from view.input_form import InputForm`: Mengimpor kelas `InputForm` dari modul `input_form` yang terdapat di folder `view`. Kelas ini menangani input data dari pengguna untuk menambah atau mengubah data mahasiswa.
   - `from view.mahasiswa import ViewMahasiswa`: Mengimpor kelas `ViewMahasiswa` dari modul `mahasiswa` yang ada di folder `view`. Kelas ini bertanggung jawab untuk menampilkan data mahasiswa kepada pengguna dalam format yang mudah dibaca.

#### 2. **Fungsi `main()`**
   Fungsi `main()` adalah titik masuk dari program ini, yang menjalankan perulangan **menu utama** dan menangani berbagai pilihan yang dimasukkan oleh pengguna.

   ```python
   def main():
       mahasiswa = Mahasiswa()
       while True:
           pilihan = input("[(L)ihat (T)ambah (U)bah (H)apus (K)eluar] : ").lower()
   ```

   - `mahasiswa = Mahasiswa()`: Membuat objek `mahasiswa` dari kelas `Mahasiswa`. Objek ini digunakan untuk menyimpan dan memanipulasi data mahasiswa.
   - `while True:`: Membuat perulangan tak terbatas untuk terus menampilkan menu pilihan hingga pengguna memilih untuk keluar (`break`).
   - `pilihan = input("[(L)ihat (T)ambah (U)bah (H)apus (K)eluar] : ").lower()`: Program menampilkan menu pilihan dan menunggu input dari pengguna. Pilihan yang dimasukkan kemudian diubah menjadi huruf kecil menggunakan `.lower()` agar bisa diproses secara konsisten.

#### 3. **Menangani Pilihan Pengguna**
   Berdasarkan pilihan yang dimasukkan oleh pengguna, program akan melakukan aksi yang sesuai. Berikut adalah penjelasan setiap kondisi dalam perulangan.

   ##### a. **Melihat Data Mahasiswa** (`pilihan == 'l'`)
   ```python
   if pilihan == 'l':
       ViewMahasiswa.tampilkan_data(mahasiswa)
   ```
   - Jika pengguna memilih **L** untuk melihat data mahasiswa, program akan memanggil metode `tampilkan_data()` dari kelas `ViewMahasiswa`, yang akan menampilkan data mahasiswa yang ada dalam objek `mahasiswa`.

   ##### b. **Menambah Data Mahasiswa** (`pilihan == 't'`)
   ```python
   elif pilihan == 't':
       nim, nama, tugas, uts, uas = InputForm.input_data()
       mahasiswa.tambah_data(nim, nama, tugas, uts, uas)
   ```
   - Jika pengguna memilih **T** untuk menambah data mahasiswa, metode `input_data()` dari kelas `InputForm` akan meminta input data mahasiswa (NIM, nama, nilai tugas, nilai UTS, dan nilai UAS) dari pengguna.
   - Setelah data diperoleh, program akan memanggil metode `tambah_data()` dari objek `mahasiswa` untuk menambahkan data mahasiswa ke dalam daftar.

   ##### c. **Mengubah Data Mahasiswa** (`pilihan == 'u'`)
   ```python
   elif pilihan == 'u':
       nim, nama, tugas, uts, uas = InputForm.input_ubah_data()
       mahasiswa.ubah_data(nim, nama, tugas, uts, uas)
   ```
   - Jika pengguna memilih **U** untuk mengubah data mahasiswa, metode `input_ubah_data()` dari kelas `InputForm` akan meminta input baru untuk data mahasiswa yang ingin diubah. Pengguna dapat memasukkan data baru atau membiarkannya kosong untuk mengubah sebagian data.
   - Setelah input diperoleh, metode `ubah_data()` pada objek `mahasiswa` akan dipanggil untuk memperbarui data mahasiswa sesuai dengan NIM yang diberikan.

   ##### d. **Menghapus Data Mahasiswa** (`pilihan == 'h'`)
   ```python
   elif pilihan == 'h':
       nim = input("Masukkan NIM yang akan dihapus: ")
       mahasiswa.hapus_data(nim)
   ```
   - Jika pengguna memilih **H** untuk menghapus data mahasiswa, program akan meminta input NIM dari pengguna.
   - Setelah NIM dimasukkan, metode `hapus_data()` pada objek `mahasiswa` akan dipanggil untuk menghapus data mahasiswa yang memiliki NIM tersebut.

   ##### e. **Keluar dari Program** (`pilihan == 'k'`)
   ```python
   elif pilihan == 'k':
       print("Program selesai.")
       break
   ```
   - Jika pengguna memilih **K** untuk keluar, program akan mencetak "Program selesai." dan menghentikan perulangan dengan menggunakan `break`. Program akan berakhir setelah ini.

   ##### f. **Pilihan Tidak Valid**
   ```python
   else:
       print("Pilihan tidak valid!")
   ```
   - Jika pengguna memasukkan pilihan yang tidak sesuai dengan opsi yang ada (selain 'l', 't', 'u', 'h', atau 'k'), program akan menampilkan pesan "Pilihan tidak valid!" dan kembali menunggu input pilihan yang benar.

#### 4. **Menjalankan Program**
   ```python
   if __name__ == "__main__":
       main()
   ```
   - Baris ini memastikan bahwa fungsi `main()` hanya akan dijalankan jika file ini dieksekusi langsung, bukan ketika diimpor sebagai modul ke dalam program lain. Hal ini adalah cara umum untuk memastikan bahwa kode hanya dieksekusi ketika file utama dijalankan.

### Alur Program
- **Memulai Program**: Program dimulai dengan memanggil `main()`, yang membuat objek `mahasiswa` dari kelas `Mahasiswa`.
- **Menu Pilihan**: Pengguna diberi menu pilihan untuk:
  - Melihat data mahasiswa (`L`),
  - Menambah data mahasiswa (`T`),
  - Mengubah data mahasiswa (`U`),
  - Menghapus data mahasiswa (`H`),
  - Keluar dari program (`K`).
- **Tindak Lanjut**: Berdasarkan pilihan pengguna, program akan melakukan aksi yang sesuai:
  - Melihat data mahasiswa dengan menampilkan data yang ada.
  - Menambah data baru dengan meminta input dan menambahkannya ke dalam daftar.
  - Mengubah data dengan meminta input baru dan memperbarui data yang ada.
  - Menghapus data dengan meminta NIM dan menghapus data yang sesuai.
  - Keluar dari program jika memilih opsi "K".

### Kesimpulan

Program ini adalah aplikasi berbasis teks yang memungkinkan pengguna untuk melakukan operasi dasar (menambah, mengubah, melihat, menghapus) pada data mahasiswa. Program ini menerapkan prinsip **Object-Oriented Programming (OOP)** dengan memisahkan logika aplikasi menjadi beberapa kelas terpisah: `Mahasiswa` untuk menangani data, `InputForm` untuk menangani input pengguna, dan `ViewMahasiswa` untuk menampilkan data kepada pengguna. Struktur program ini memudahkan pemeliharaan dan pengembangan lebih lanjut.
