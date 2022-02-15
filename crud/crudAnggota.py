import mysql.connector

class CRUD:

	def __init__(self):
		self.__localhost     = "localhost"
		self.__username      = "root"
		self.__password      = ""
		self.__database_name = "perpustakaan"
		self.__table_name 	 = "anggota"
		self.createConnection()

	def create(self):
		print('Masukan ID Anggota: ')
		id_anggota = input()
		print('Masukan Nama Anggota: ')
		nama = input()
		print('Masukan Alamat Anggota: ')
		alamat = input()
		print('Masukan No. HP Anggota: ')
		nohp = input()

		cursor = self.__db.cursor()

		val = (id_anggota, nama, alamat, nohp)
		cursor.execute("INSERT INTO "+self.__table_name+" (id_anggota, nama, alamat, nohp) VALUES (%s, %s, %s, %s)", val)

		self.__db.commit()

		print("Berhasil!, Anggota Telah ditambahkan.")

	def read(self):
		cursor = self.__db.cursor()

		cursor.execute("SELECT * FROM "+self.__table_name+"")

		myresult = cursor.fetchall()

		for x in myresult:
		  print(x)

	def update(self):
		print('Search by ID Anggota:')
		id_anggota = input()

		print('Edit nama anggota:')
		nama = input()
		print('Edit alamat anggota:')
		alamat = input()
		print('Edit no. hp anggota:')
		nohp = input()


		cursor = self.__db.cursor()

		cursor.execute ("UPDATE "+self.__table_name+" SET nama=%s, alamat=%s, nohp=%s WHERE id_anggota=%s ", (nama, alamat, nohp, id_anggota))

		self.__db.commit()

		print("Berhasil!, Anggota telah diubah.")

	def delete(self):
		print('Search by ID Anggota to delete:')
		id_anggota = input()

		cursor = self.__db.cursor()

		cursor.execute ("DELETE FROM "+self.__table_name+" WHERE id_anggota = %s", (id_anggota,))

		self.__db.commit()

		print("Berhasil!, Anggota telah dihapus.")

	def createConnection(self):
		db = mysql.connector.connect(
		  host     = self.__localhost,
		  user     = self.__username,
		  passwd   = self.__password,
		  database = self.__database_name
		)

		self.__db = db

