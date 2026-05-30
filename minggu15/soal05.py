def kombinasi(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    return kombinasi(n - 1, r - 1) + kombinasi(n - 1, r)

isin = input("n = ")
isir = input("r = ")
print(kombinasi(int(isin), int(isir)))