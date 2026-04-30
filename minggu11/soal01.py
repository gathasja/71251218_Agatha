def angka_terbaik(angka):
    urutan = sorted(angka, reverse=True)
    return urutan[:3]

inputan = input()
data = [int(x) for x in inputan.split()]

if len(data) < 3:
    print("list harus memiliki min. 3 angka")
else:
    hasil = angka_terbaik(data)
    print(f"list angka: {data}")
    print(f"3 angka terbaik: {hasil}")
    
    
    