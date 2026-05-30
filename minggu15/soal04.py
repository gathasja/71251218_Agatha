def jumlah_digit(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + jumlah_digit(n // 10)

angka = int(input())
print(f"jumlah dari {angka} = {jumlah_digit(angka)}")