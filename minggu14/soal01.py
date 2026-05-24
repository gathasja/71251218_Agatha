n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    aplikasi = set()
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.add(nama_aplikasi)
    data_aplikasi[nama_kategori] = aplikasi

for kategori, apps in data_aplikasi.items():
    print(f"{kategori}: {apps}")

semua_set = list(data_aplikasi.values())
muncul_semua = semua_set[0]
for s in semua_set[1:]:
    muncul_semua = muncul_semua & s
print(f"\naplikasi yang muncul di semua kategori: {muncul_semua}")

print("\naplikasi yang hanya muncul di 1 kategori:")
for kategori, apps in data_aplikasi.items():
    set_lain = set()
    for k, v in data_aplikasi.items():
        if k != kategori:
            set_lain = set_lain | v
    hanya_disini = apps - set_lain
    print(f"{kategori}: {hanya_disini}")

if n > 2:
    print("\naplikasi muncul di 2 kategori:")
    kategori_list = list(data_aplikasi.keys())
    tepat_dua = set()
    for i in range(len(kategori_list)):
        for j in range(i + 1, len(kategori_list)):
            irisan_dua = data_aplikasi[kategori_list[i]] & data_aplikasi[kategori_list[j]]
            for k in range(len(kategori_list)):
                if k != i and k != j:
                    irisan_dua = irisan_dua - data_aplikasi[kategori_list[k]]
            tepat_dua = tepat_dua | irisan_dua
    print(f"{tepat_dua}")