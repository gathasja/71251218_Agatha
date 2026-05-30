def palindrom(teks):
    if len(teks) <= 1:
        return True
    if teks[0] != teks[-1]:
        return False
    return palindrom(teks[1:-1])

def rapi(teks):
    teks = teks.lower()
    
    teksrapi = ""
    for karakter in teks:
        if 'a' <= karakter <= 'z':
            teksrapi += karakter
    return teksrapi

kalimat = input("isi kalimat: ")
kalimat_bersih = rapi(kalimat)

if palindrom(kalimat_bersih):
    print(f"{kalimat} adalah palindrom")
else:
    print(f"{kalimat} bukan palindrom")