#definir la lista de números

lista = [5, 6, 9, 1, 15, 19, 1, 2]

max_num = lista[0]

for num in lista:
    if num > max_num:
        max_num = num
        
print (max_num)