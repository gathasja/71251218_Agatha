lista = ['red', 'green', 'blue']
listb = ['#ff0000', '#008000', '#0000ff']

hasil  = {}
for i in range(len(lista)):
    hasil[lista[i]] = listb[i]
    
urutan = ['green', 'blue', 'red']
hasil1 = {key: hasil[key] for key in urutan}
    
print(hasil1)
