import mysql.connector

class Database:
    def __init__(self, database_name):
        self.__database_name = database_name

    def setLocalhost(self, localhost):
        self.__localhost = localhost

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setTableBuku(self, table_buku):
        self.__table_buku = table_buku

    def setTableAnggota(self, table_anggota):
        self.__table_anggota = table_anggota

    def setTablePetugas(self, table_petugas):
        self.__table_petugas = table_petugas

    def setTableTransaksi(self, table_transaksi):
        self.__table_transaksi = table_transaksi

    def createDatabase(self):
        db = mysql.connector.connect(
            host        = self.__localhost,
            user        = self.__username,
            password     = self.__password
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS "+self.__database_name)
        return "Database "+self.__database_name+" has been created"

    def createTable(self):
        self.createConnection()
        cursor = self.__db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS "+self.__table_buku+"(kodeBuku varchar(10) primary key, judulBuku varchar(255), penerbit varchar (100), penulis varchar(100),"
                                                                       "tahunTerbit varchar(20), posisiRak varchar(20))")
        cursor.execute("CREATE TABLE IF NOT EXISTS "+self.__table_anggota+"(id_anggota char(10) primary key, nama varchar(100), alamat text, nohp varchar(15))")
        cursor.execute("CREATE TABLE IF NOT EXISTS "+self.__table_petugas+"(id_petugas char(10) primary key, nama varchar(100), alamat text, jamTugas varchar(50), nohp varchar(15))")
        cursor.execute("CREATE TABLE IF NOT EXISTS "+self.__table_transaksi+"(id_transaksi char(10), id_anggota char(10), kodeBuku char(10), tglpinjam varchar(20), tglkembali varchar(20),"
                                                                            "keterangan text, primary key(id_transaksi, id_anggota, kodeBuku))")
        return "Table has been created"

    def createConnection(self):
        db = mysql.connector.connect(
            host        = self.__localhost,
            user        = self.__username,
            password     = self.__password,
            database    = self.__database_name
        )
        self.__db = db
