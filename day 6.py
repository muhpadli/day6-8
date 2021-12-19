print("Pesan Tiket Bus!! Gak Antri, Gak ribet")
print("\n>>>>>>>>>>>DAFTAR  JURUSAN<<<<<<<<<<<<")
print("\n1. Surabaya (SBY) = Rp. 300.000,-")
print("2. Bali (BL)      = Rp. 350.000,-")
print("3. Lampung (LMP)  = Rp. 500.000,-")
print("\n>>>>>>>>>>>>>>>><<><<<<<<<<<<<<<<<<<<<")

nama = input("\nmasukkan nama anda:")
jml_tiket = int(input("masukkan jumlah tiket yang dibeli:"))
no_hp =  int(input("masukkan no HP anda:"))
jurusan = input("masukkan kode jurusan (SBY/BL/LMP) :")
jurusan = jurusan.lower()
if( jml_tiket >= 3):
	if(jurusan == "sby"):
		harga = 300000
	elif(jurusan == "bl"):
		harga = 350000
	elif(jurusan == "lmp"):
		harga = 500000
	else:
		print("maaf kode yang anda masukkan salah")
	potongan = (10/100)*(jml_tiket*harga)
	total_harga = (jml_tiket*harga) - potongan
else:
	if(jurusan == "sby"):
		harga = 300000
	elif(jurusan == "bl"):
		harga = 350000
	elif(jurusan == "lmp"):
		harga = 500000
	else:
		print("maaf kode yang anda masukkan salah")
	potongan = 0
	total_harga = (jml_tiket*harga) - potongan
print("\n_____________________________________")
print("\nPotongan : Rp.", potongan)
print("Total Harga : Rp.", total_harga)
		