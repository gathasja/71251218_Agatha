# # Data awal
# harga_beli_1_per_gram = 650000  # dalam Rupiah
# berat_1 = 25  # gram
# harga_sekarang_per_gram = 685000

# # 1. Keuntungan dari pembelian pertama (25 gram) saat harga naik menjadi 685000/gram
# modal_awal = harga_beli_1_per_gram * berat_1
# nilai_sekarang = harga_sekarang_per_gram * berat_1
# keuntungan_rp = nilai_sekarang - modal_awal
# keuntungan_persen = (keuntungan_rp / modal_awal) * 100

# print("1. Keuntungan dari 25 gram emas:")
# print(f"   Modal awal: Rp {modal_awal:,}")
# print(f"   Nilai sekarang: Rp {nilai_sekarang:,}")
# print(f"   Keuntungan (Rp): Rp {keuntungan_rp:,}")
# print(f"   Keuntungan (%): {keuntungan_persen:.2f}%")

# # 2. Pembelian kedua 15 gram di harga 685000/gram
# harga_beli_2_per_gram = 685000
# berat_2 = 15
# total_berat = berat_1 + berat_2

# modal_pembelian_2 = harga_beli_2_per_gram * berat_2
# total_modal = modal_awal + modal_pembelian_2

# # 3. Harga naik menjadi 715000/gram
# harga_naik_per_gram = 715000
# nilai_total_naik = harga_naik_per_gram * total_berat

# keuntungan_total_rp = nilai_total_naik - total_modal
# keuntungan_total_persen = (keuntungan_total_rp / total_modal) * 100

# print("\n2. Setelah beli tambahan 15 gram dan harga naik ke Rp 715.000/gram:")
# print(f"   Total berat emas: {total_berat} gram")
# print(f"   Total modal: Rp {total_modal:,}")
# print(f"   Nilai total (Rp 715.000/gram): Rp {nilai_total_naik:,}")
# print(f"   Keuntungan total (Rp): Rp {keuntungan_total_rp:,}")
# print(f"   Keuntungan total (%): {keuntungan_total_persen:.2f}%")

print("Hello world")