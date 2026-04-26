namaFile = "soal.txt"

print(f"nama file1: {namaFile}")
with open(namaFile, 'r', encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if not baris:
            continue
        
        if "||" in baris:
            soal, jawabanBenar = baris.split("||")
            soal = soal.strip()
            jawabanBenar = jawabanBenar.strip()
            
            print(f"\n{soal}")
            inputUser = input("Jawab: ").strip()
            if inputUser.lower() == jawabanBenar.lower():
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")