from crud.crudAnggota import CRUD as anggota
from crud.crudBuku import CRUD as buku
from crud.crudTransaksi import CRUD as transaksi
from crud.crudPetugas import CRUD as petugas

class Menu():
    #menampilkan menu aplikasi
    def showMenu(self):
        print("===Selamat Datang di Aplikasi Perpustakaan===")
        print("===Menu===")
        print("1. Transaksi Peminjaman")
        print("2. Data Buku")
        print("3. Data Anggota")
        print("4. Data Petugas")
        print("5. Keluar")
        pilih = input("Pilih Menu berdasarkan angka: ")
        stop = False
        while (not stop):
            if(pilih == "1"):
                self.dataTransaksi()
            elif(pilih == "2"):
                self.dataBuku()
            elif(pilih == "3"):
                self.dataAnggota()
            elif(pilih == "4"):
                self.dataPetugas()
            elif(pilih == "5"):
                stop = True
            else:
              print("Masukan pilihan dengan angka yang sesuai")
              self.backToMenu()

    #berfungsi untuk kembali ke menu utama
    def backToMenu(self):
        print("\n")
        input("Tekan enter untuk kembali")
        self.showMenu()

    #menampilkan menu untuk transaksi
    def dataTransaksi(self):

        print("===Anda Berada di Menu Transaksi Peminjaman===")
        print("===Silahkan pilih menu===")
        print("1. Peminjaman")
        print("2. Edit Status Transaksi")
        print("3. Hapus Transaksi")
        print("4. Lihat Data Transaksi")
        print("5. Keluar dari menu Transaksi")
        pilih = input("Pilih Menu: ")

        menu = transaksi()
        if (pilih == "1"):
            menu.create()
        elif (pilih == "2"):
            menu.update()
        elif (pilih == "3"):
            menu.delete()
        elif (pilih == "4"):
            menu.read()
        elif (pilih == "5"):
            self.backToMenu()

        self.backToMenu()

    #menampilkan menu untuk data buku
    def dataBuku(self):
        print("===Anda Berada di Menu Data Buku===")
        print("===Silahkan pilih menu===")
        print("1. Tambah Buku")
        print("2. Edit Buku")
        print("3. Hapus Buku")
        print("4. Lihat Data Buku")
        print("5. Keluar dari menu Buku")
        pilih = input("Pilih Menu: ")

        menu = buku()
        if (pilih == "1"):
            menu.create()
        elif (pilih == "2"):
            menu.update()
        elif (pilih == "3"):
            menu.delete()
        elif (pilih == "4"):
            menu.read()
        elif (pilih == "5"):
            self.backToMenu()

        self.backToMenu()

    #menampilkan menu data anggota
    def dataAnggota(self):
        print("===Anda Berada di Menu Data Anggota===")
        print("===Silahkan pilih menu===")
        print("1. Tambah Anggota")
        print("2. Edit Anggota")
        print("3. Hapus Anggota")
        print("4. Lihat Data Anggota")
        print("5. Keluar dari menu Anggota")
        pilih = input("Pilih Menu: ")

        menu = anggota()
        if (pilih == "1"):
            menu.create()
        elif (pilih == "2"):
            menu.update()
        elif (pilih == "3"):
            menu.delete()
        elif (pilih == "4"):
            menu.read()
        elif (pilih == "5"):
            self.backToMenu()

        self.backToMenu()

    #menampilkan menu data petugas
    def dataPetugas(self):
        print("===Anda Berada di Menu Data Petugas===")
        print("===Silahkan pilih menu===")
        print("1. Tambah Petugas")
        print("2. Edit Petugas")
        print("3. Hapus Petugas")
        print("4. Lihat Data Petugas")
        print("5. Keluar dari menu Petugas")
        pilih = input("Pilih Menu: ")

        menu = petugas()
        if (pilih == "1"):
            menu.create()
        elif (pilih == "2"):
            menu.update()
        elif (pilih == "3"):
            menu.delete()
        elif (pilih == "4"):
            menu.read()
        elif (pilih == "5"):
            self.backToMenu()

        self.backToMenu()


obj = Menu()
obj.showMenu()

