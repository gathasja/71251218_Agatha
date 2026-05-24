list_a = [10, 20, 30, 20, 10, 40]
print(f"list       : {list_a}")
print(f"list ke Set: {set(list_a)}")
print()

set_a = {'apel', 'jeruk', 'mangga', 'apel'}
print(f"set        : {set_a}")
print(f"set ke list: {list(set_a)}")
print()

tuple_a = (5, 10, 15, 10, 5, 20)
print(f"tuple       : {tuple_a}")
print(f"tuple ke set: {set(tuple_a)}")
print()

set_b = {'merah', 'biru', 'hijau', 'merah'}
print(f"set         : {set_b}")
print(f"set ke tuple: {tuple(set_b)}")
