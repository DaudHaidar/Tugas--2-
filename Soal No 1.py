sambutan = ( "SELAMAT DATANG", "======== MENU =======",)
menu = ( "1. DAFTAR KONTAK", "2. TAMBAHKAN KONTAK", "3. KELUAR" )

nama = []
no_telephone = []

def TambahKontak():
    banyak_data = int(input("JUMLAH KONTAK :"))


    for x in range(banyak_data):
        nama_kontak = str(input("NAMA : "))
        nomor = (input("NOMOR TELEPHONE : "))
        nama.append(nama_kontak)
        no_telephone.append(nomor)
    print(nama)
    print(no_telephone)

TambahKontak()

def DaftarKontak():
    print("======= DAFTAR KONTAK ========")
    for y in nama:
        print(y)


DaftarKontak()







