def pendekPanjang(kalimat):
    kata_kata = kalimat.split()
    if not kata_kata:
        return None, None
    
    kata_terpendek = kata_kata[0]
    kata_terpanjang = kata_kata[0]
    
    for kata in kata_kata:
        kata_bersih = kata.strip(".,!?;:()\"'")
        
        if len(kata_bersih) < len(kata_terpendek):
            kata_terpendek = kata_bersih
        if len(kata_bersih) > len(kata_terpanjang):
            kata_terpanjang = kata_bersih
    
    return kata_terpendek, kata_terpanjang

kalimat = input("Masukkan kalimat: ")
terpendek, terpanjang = pendekPanjang(kalimat)

print(f"Kalimat: {kalimat}")
print(f"Kata TERPENDEK : {terpendek} ({len(terpendek)} huruf)")
print(f"Kata TERPANJANG: {terpanjang} ({len(terpanjang)} huruf)")
