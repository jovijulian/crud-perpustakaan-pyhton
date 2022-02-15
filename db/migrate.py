import database as db

db = db.Database("perpustakaan")
db.setLocalhost("localhost")
db.setUsername("root")
db.setPassword("")
db.createDatabase()

db.setTableBuku("buku")
db.setTableAnggota("anggota")
db.setTablePetugas("petugas")
db.setTableTransaksi("transaksi")
db.createTable()
