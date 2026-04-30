total = 0
jumlah = 0

while True:
    inputan = input()
    if inputan.lower() == "done":
        break
    try:
        total += float(inputan)
        jumlah += 1
    except ValueError:
        print("input harus berupa angka atau kata done")
        
if jumlah > 0:
    print(f"rata-rata: {total / jumlah:.2f}")
else:
    print("tidak ada data")