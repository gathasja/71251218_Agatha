def frekuensi(kalimat, kata):
    kalimat = kalimat.lower()
    kata = kata.lower()
    kata_kata = kalimat.split()
    
    jumlah = 0
    for kat in kata_kata:
        kata = kata.strip(".,!/;:()\"'")
        if kat == kata:
            jumlah += 1
            
    return jumlah

kalimat = input("masukan kalimat: ")
kata = input("masukan kata yang dicari: ")
hasil = frekuensi(kalimat, kata)

print(f"output: '{kata}' ada {hasil} buah")
