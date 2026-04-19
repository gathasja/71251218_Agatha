def bersihkanSpasi(teks):
    kata_kata = teks.split()
    return ' '.join(kata_kata)

inputString = input("Masukkan string: ")
outputString = bersihkanSpasi(inputString)

print(f"String asli: {inputString}")
print(f"String bersih: {outputString}")
