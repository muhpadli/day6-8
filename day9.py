print("belajar tipe data tuple")

transportasi = ("sepeda", "motor", "mobil", "bus", "truck", "pesawat")
print(transportasi)
print(type(transportasi))

#menghitung nilai data tuple
print(len(transportasi))

#menampilkan sebagian nilai data tuple
print(transportasi[:4])
print(transportasi[2:4])
print(transportasi[:-3])

#sequence unpacking
identitas = ("Muh. Padli", "D0221513", "S1-Informatika")
Nama, NIM, Prodi = identitas
print("Nama :", Nama)
print("NIM :", NIM)
print("Prodi :", Prodi)

#menggabungkan dua tuple
data = transportasi + identitas
print(data)

#mencari nilai tertinggi dan terendah pada tuple
nilai = (15, 14, 17, 14, 17, 19)
print(max(nilai))
print(min(nilai))