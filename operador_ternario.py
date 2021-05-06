
age = 15

if age >= 18:
    print(True)
else:
    print(False)

#? Operador ternario (ternary)
is_adult = True if age >= 18 else False #Cualquier condición, pero no se pueden igualar variables dentro del operador ternario
print(is_adult)
is_adult = 'Es adulto' if age >= 18 else 'No es adulto'
print(is_adult)

list_a = [1,2,3,4]
result = list(map(lambda num: num*2 if num %2==0 else num,list_a))
print(result)

