import mysql.connector


class CRUD:

    def __init__(self):
        self.__localhost = "localhost"
        self.__username = "root"
        self.__password = ""
        self.__database_name = "perpustakaan"
        self.__table_name = "transaksi"
        self.createConnection()

    def create(self):
        print('Masukan ID transaksi: ')
        id_transaksi = input()
        print('Masukan ID Anggota: ')
        id_anggota = input()
        print('Masukan Kode Buku yang dipinjam: ')
        kodeBuku = input()
        print('Masukan Tanggal Pinjam: ')
        tglpinjam = input()
        print('Masukan Tanggal Kembali: ')
        tglkembali = input()

        cursor = self.__db.cursor()
        val = (id_transaksi, id_anggota, kodeBuku, tglpinjam, tglkembali)
        cursor.execute("INSERT INTO " + self.__table_name + " (id_transaksi, id_anggota, kodeBuku, tglpinjam, tglkembali) VALUES "
                                                            "(%s, %s, %s, %s, %s)",
                       val)

        self.__db.commit()

        print("Berhasil!, Transaksi Telah ditambahkan.")

    def read(self):
        cursor = self.__db.cursor()

        cursor.execute("SELECT * FROM " + self.__table_name + "")

        myresult = cursor.fetchall()

        for x in myresult:
            print(x)

    def update(self):
        print('Search by ID Transaksi:')
        id_transaksi = input()
        print("Apakah Buku sudah dikembalikan?")
        print("1. sudah")
        print("2. belum")
        print('Pilih Keterangan:')
        status = input()
        if (status == "1"):
            print("Tanggal pengembalian: ")
            tglkembali = input()
            keterangan = "sudah dikembalikan"
        elif (status == "2"):
            keterangan = "belum dikembalikan"
            print("Perpanjang tanggal pengembalian: ")
            tglkembali = input()

        cursor = self.__db.cursor()

        cursor.execute("UPDATE " + self.__table_name + " SET keterangan=%s ,tglkembali=%s WHERE id_transaksi=%s ", (keterangan, tglkembali, id_transaksi))

        self.__db.commit()

        print("Berhasil!, Status Transaksi telah diubah.")

    def delete(self):
        print('Search by ID Transaksi to delete:')
        id_transaksi = input()

        cursor = self.__db.cursor()

        cursor.execute("DELETE FROM " + self.__table_name + " WHERE id_transaksi = %s", (id_transaksi,))

        self.__db.commit()

        print("Berhasil!, Transaksi telah dihapus.")

    def createConnection(self):
        db = mysql.connector.connect(
            host=self.__localhost,
            user=self.__username,
            passwd=self.__password,
            database=self.__database_name
        )

        self.__db = db
