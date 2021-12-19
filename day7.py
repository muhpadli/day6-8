profil = {"Nama" : "Junaedi", "NIM" : "H0755758", "Prodi" : "S1 - Informatika", "gmail" :"Junaedi31@gmail.com", "Alamat" : "Banggae Timur"}
print("Nama   :", profil["Nama"])
print("NIM    :", profil["NIM"])
print("Prodi  :", profil["Prodi"])
print("Gmail  :", profil["gmail"])
print("Alamat :", profil["Alamat"])
print()
#mengubah elemen dictionary
profil["Prodi"] = "S1- Pendidikan Matematika"
print(profil)
print()
#Menambahkan elemen dictionary
profil["Kabupaten"]  = "Majene"
print(profil)
print()
#menghapus element dictionary
del profil["gmail"]
print(profil)
print()
#cara membuat dictionary dengan construktor dic()
profil = dict ( Nama = "Junaedi", NIM = "H0745647", Alamat = "Banggae Timur")
print(profil)
