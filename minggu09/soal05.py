import re
from datetime import datetime

def ekstrak_tanggal(teks):
    pattern = r'\d{4}-\d{2}-\d{2}'
    tanggal_ditemukan = re.findall(pattern, teks)
    
    return tanggal_ditemukan

def konversi_tanggal(tanggal_str):
    tahun, bulan, hari = tanggal_str.split('-')
    return f"{hari}-{bulan}-{tahun}"

def hitung_selisih_hari(tanggal_str):
    tanggal = datetime.strptime(tanggal_str, '%Y-%m-%d')
    sekarang = datetime.now()
    
    selisih = sekarang - tanggal
    return selisih.days

def main():
    teks = input("Masukkan teks: ")
    tanggal_list = ekstrak_tanggal(teks)
    
    if not tanggal_list:
        print("Tidak ditemukan tanggal dalam format YYYY-MM-DD")
    else:
        for tanggal_str in tanggal_list:
            tanggal_baru = konversi_tanggal(tanggal_str)
            selisih = hitung_selisih_hari(tanggal_str)
            
            print(f"{tanggal_str} 00:00:00 selisih {selisih} hari")
            print(f"Format baru: {tanggal_baru}\n")

if __name__ == "__main__":
    main()