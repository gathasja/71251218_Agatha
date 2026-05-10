nama_file = input("Masukan nama file : ")

email = {}
with open(nama_file, 'r') as f:
    for baris in f:
        if baris.startswith('From:'):
            sender = baris.split()[1]
            email[sender] = email.get(sender, 0) + 1
print(email)
