minta = input("Enter a file name: ")
jam = []

with open(minta, 'r') as f:
    jam = [(baris.split()[5][:2], 1) for baris in f if baris.startswith('From ')]
    
hitung = {}
for j, h in jam:
    hitung[j] = hitung.get(j, 0) + h
    
for j, jmlh in sorted(hitung.items()):
    print(j, jmlh)
    
    
    