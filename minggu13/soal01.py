inputan = input()
t = tuple(int(x) for x in inputan.split())
if all (x == t[0] for x in t):
    print("True")
else:
    print("False")
    
    