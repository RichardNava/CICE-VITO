
#? con comprehension
a = [1,2,3,4]
result_en_lista = sum([num ** 2 for num in a])
#print(result_en_lista)
def doble(num):
    return num ** 2
listado = [doble(num) for num in a]
#print(listado)

#? con generator sintaxis comprehension
result_en_generador = (num ** 2 for num in a)
print(result_en_lista)
# print(type(result_1))

#? con función normal
def dobles(given_list):
    result = []
    for num in given_list:
        result.append(num ** 2)
    return result

#? con función generadora
def dobles_generator(given_list):
    for num in given_list:
        yield num ** 2

result_2 = dobles(a)

#? con map:
result_map = map(lambda num: num ** 2, a)

#? Con comprehension y operador ternario
result_ternario = [num for num in a if num %2==0] #Sin else(Con comprehension permite omitir el else)
result_ternario = [num if num %2==0 else num for num in a] #Con else(Hay que escribirlo a la izquierda)

