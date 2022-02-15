import mysql.connector


class CRUD:

    def __init__(self):
        self.__localhost = "localhost"
        self.__username = "root"
        self.__password = ""
        self.__database_name = "perpustakaan"
        self.__table_name = "petugas"
        self.createConnection()

    def create(self):
        print('Masukan ID Petugas: ')
        id_petugas = input()
        print('Masukan Nama Petugas: ')
        nama = input()
        print('Masukan Alamat Petugas: ')
        alamat = input()
        print('Masukan Jam Tugas Anggota: ')
        jamTugas = input()
        print('Masukan No. HP Petugas: ')
        nohp = input()

        cursor = self.__db.cursor()

        val = (id_petugas, nama, alamat, jamTugas, nohp)
        cursor.execute("INSERT INTO " + self.__table_name + " (id_petugas, nama, alamat, jamTugas, nohp) VALUES (%s, %s, %s, %s, %s)",
                       val)

        self.__db.commit()

        print("Berhasil!, Petugas Telah ditambahkan.")

    def read(self):
        cursor = self.__db.cursor()

        cursor.execute("SELECT * FROM " + self.__table_name + "")

        myresult = cursor.fetchall()

        for x in myresult:
            print(x)

    def update(self):
        print('Search by ID Petugas:')
        id_petugas = input()

        print('Edit nama petugas:')
        nama = input()
        print('Edit alamat anggota:')
        alamat = input()
        print('Edit jam tugas petugas:')
        jamTugas = input()
        print('Edit no. hp anggota:')
        nohp = input()

        cursor = self.__db.cursor()

        cursor.execute("UPDATE " + self.__table_name + " SET nama=%s, alamat=%s, jamTugas=%s, nohp=%s WHERE id_petugas=%s ", (nama, alamat, jamTugas, nohp, id_petugas))

        self.__db.commit()

        print("Berhasil!, Petugas telah diubah.")

    def delete(self):
        print('Search by ID Petugas to delete:')
        id_petugas = input()

        cursor = self.__db.cursor()

        cursor.execute("DELETE FROM " + self.__table_name + " WHERE id_petugas = %s", (id_petugas,))

        self.__db.commit()

        print("Berhasil!, Petugas telah dihapus.")

    def createConnection(self):
        db = mysql.connector.connect(
            host=self.__localhost,
            user=self.__username,
            passwd=self.__password,
            database=self.__database_name
        )

        self.__db = db
