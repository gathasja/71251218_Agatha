def bandingkanFile(file1,file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        baris1 = f1.readlines()
        baris2 = f2.readlines()
        
    maxbaris = max(len(baris1), len(baris2))
    for i in range(maxbaris):
        b1 = baris1[i].rstrip() if i < len(baris1) else "tidak ada"
        b2 = baris2[i].rstrip() if i < len(baris2) else "tidak ada"
        
        if b1 != b2:
            print(f"baris {i+1}:")
            print(f"file 1: {b1}")
            print(f"file 2: {b2}")
            
bandingkanFile("soal1.txt", "soalsatu.txt")