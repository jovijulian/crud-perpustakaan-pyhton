import mysql.connector
class CRUD:

    def __init__(self):
        self.__localhost = "localhost"
        self.__username = "root"
        self.__password = ""
        self.__database_name = "perpustakaan"
        self.__table_name = "buku"
        self.createConnection()

    def create(self):
        print('Masukan Kode Buku: ')
        kodeBuku = input()
        print('Masukan Judul Buku: ')
        judulBuku = input()
        print('Masukan Penerbit Buku: ')
        penerbit = input()
        print('Masukan Penulis Buku: ')
        penulis = input()
        print('Masukan Tahun Terbit Buku: ')
        tahunTerbit = input()
        print('Masukan Posisi Rak Buku: ')
        posisiRak = input()

        cursor = self.__db.cursor()

        val = (kodeBuku, judulBuku, penerbit, penulis, tahunTerbit, posisiRak)
        cursor.execute("INSERT INTO " + self.__table_name + " (kodeBuku, judulBuku, penerbit, penulis, tahunTerbit, posisiRak) VALUES (%s, %s, %s, %s, %s, %s)", val)

        self.__db.commit()

        print("Berhasil!, Buku telah ditambahkan.")

    def read(self):
        cursor = self.__db.cursor()

        cursor.execute("SELECT * FROM " + self.__table_name + "")

        myresult = cursor.fetchall()

        for x in myresult:
            print(x)

    def update(self):
        print('Search by kode buku:')
        kodeBuku = input()

        print('Edit judul buku:')
        judulBuku = input()
        print('Edit penerbit:')
        penerbit = input()
        print('Edit penulis:')
        penulis = input()
        print('Edit tahun terbit:')
        tahunTerbit = input()
        print('Edit posisi rak:')
        posisiRak = input()


        cursor = self.__db.cursor()

        cursor.execute("UPDATE " + self.__table_name + " SET judulBuku=%s, penerbit=%s, penulis=%s, tahunTerbit=%s, posisiRak=%s WHERE kodeBuku=%s ",
                       (judulBuku, penerbit, penulis, tahunTerbit, posisiRak, kodeBuku))

        self.__db.commit()

        print("Berhasil!, Buku telah diubah.")

    def delete(self):
        print('Cari berdasarkan Judul Buku untuk dihapus: ')
        judulBuku = input()
        print('Cari berdasarkan Kode Buku untuk dihapus: ')
        kodeBuku = input()

        cursor = self.__db.cursor()

        cursor.execute("DELETE FROM " + self.__table_name + " WHERE judulBuku = %s || kodeBuku = %s", (judulBuku,kodeBuku,))

        self.__db.commit()

        print("Berhasil!, Buku telah dihapus.")

    def createConnection(self):
        db = mysql.connector.connect(
            host=self.__localhost,
            user=self.__username,
            passwd=self.__password,
            database=self.__database_name
        )

        self.__db = db
