def bilprima(n, cek=2):
    if n < 2:
        return False
    if cek == n:
        return True
    if n % cek == 0:
        return False
    return bilprima(n, cek + 1)

inpute = int(input("bilangan: "))

if bilprima(inpute):
    print(f"{inpute} adalah prima")
else:
    print(f"{inpute} bukan prima")