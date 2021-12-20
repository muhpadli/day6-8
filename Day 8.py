buah = ["mangga", "pisang", "melon", "jambu"]
print(buah)
#menampilkan data list
print(buah[0])
print(buah[1])
print(buah[2])
print(buah[3])
print()
#mengganti nilai data list
buah[2] = "jeruk"
print(buah)
print()
#slicing data list
print(buah[1:3])
print(buah[:3])
print()
#menambahkan nilai data list
buah.insert(3, "pepaya")
print(buah)
print()
#menghapus dua data list
buah.remove("pisang")
print(buah)
del buah[1:3]
print(buah)
print()
#menggabungkan dua nilai data list
buah = [ "mangga", "pisang", "melon", "jambu"]
buah1 = [ "semangka", "anggur", "apel"]
buah2 = buah + buah1
print(buah2)
#mengurutkan data list
buah2.sort()
print(buah)
