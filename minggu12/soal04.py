nama_file =input("Masukan nama file: ")

domin = {}
with open(nama_file, 'r') as f:
    for baris in f:
        if baris.startswith('From:'):
            email = baris.split()[1]
            domain = email.split('@')[1]
            domin[domain] = domin.get(domain, 0) + 1
print(domin)



