def deret(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        n = n - 1
    return n + deret(n - 2)
try:
    n = int(input("bilangan terakhir: "))
    if n % 2 == 0:
        n_asal = n
        n = n - 1
    
    hasil = deret(n)
    print(f"deret ganjil: ", end="")
    for i in range(1, n + 1, 2):
        if i < n:
            print(f"{i} + ", end="")
        else:
            print(f"{i}", end="")
    print(f"\nhasil: {hasil}")
except ValueError:
    print("harus berupa bilangan bulat!")