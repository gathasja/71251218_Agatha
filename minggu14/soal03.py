import string
def baca_kata(nama_file):
    try:
        with open(nama_file, 'r') as f:
            isi = f.read()
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan!")
        exit()
    except Exception as e:
        print(f"Error: File '{nama_file}' tidak bisa dibaca! ({e})")
        exit()

    isi = isi.lower()
    for tanda in string.punctuation:
        isi = isi.replace(tanda, ' ')
    return set(isi.split())

file1 = input("Masukkan nama file pertama : ")
file2 = input("Masukkan nama file kedua   : ")

set1 = baca_kata(file1)
set2 = baca_kata(file2)
kata_sama = set1 & set2

print(f"\njumlah kata unik di {file1}  : {len(set1)} kata")
print(f"jumlah kata unik di {file2}    : {len(set2)} kata")
print(f"jumlah kata yang muncul di 2 file tsb : {len(kata_sama)} kata")

print(f"\nkata yang muncul di 2 file tersebut:")
for kata in sorted(kata_sama):
    print(f"{kata}")
