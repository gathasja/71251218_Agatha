file = input("masukan file: ")
with open(file, 'r', encoding="utf-8") as f:
    isi = f.read()
    
isi = isi.lower()
for tanda in ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')', "|", '\n']:
    isi = isi.replace(tanda, ' ')
    
kata = isi.split()
unik = sorted(set(kata))

print(f"jumlah kata unik: {len(unik)}")
print("kata unik: ")
for kat in unik:
    print(kat)
    
    
    