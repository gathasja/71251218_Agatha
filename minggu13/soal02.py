nama = "Agatha Sabda Alethea Prabawa"
nim = "71251218"
alamt ="Kediri, Jawa Timur"

data = (nama, nim, alamt)
print(f"data: {data}")
print(f"\nNIM : {data[1]}")
print(f"NAMA : {data[0]}")
print(f"ALAMAT : {data[2]}")

print(f"\nNIM: {tuple(data[1])}")

namadpn = data[0].split()[0]
print(f"\nNAMA DEPAN: {tuple(namadpn[1:])}")

namatukr = data[0].split()
print(f"\nNAMA TERBALIK: {tuple(reversed(namatukr))}")






