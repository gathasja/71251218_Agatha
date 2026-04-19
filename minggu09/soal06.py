import re
import random
import string

def ekstrak_email(teks):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, teks)
    return emails

def ambil_username(email):
    return email.split('@')[0]

def generate_password(panjang=8):
    karakter = string.ascii_letters + string.digits
    password = ''.join(random.choice(karakter) for _ in range(panjang))
    return password

def main():
    teks = input("Masukkan teks: ")
    emails = ekstrak_email(teks)
    
    if not emails:
        print("Tidak ditemukan alamat email dalam teks")
    else:
        for email in emails:
            username = ambil_username(email)
            password = generate_password(8)
            print(f"{email} username: {username} , password: {password}")

if __name__ == "__main__":
    main()