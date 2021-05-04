#import requests as req
import json
from Models import Municipality

#response = req.get("https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json").json()

#with open("municipalities.json", "w", encoding="utf8") as file:
#    json.dump(response, file, ensure_ascii=False)

#! Ejercicio Bonus: Crea una función que reciba como parametro el dataset y devuelva tres listas con la siguiente condición:
#!      - la lista 1 tendrá todos los valores de densidad que empiecen por 1
#!      - la lista 2 tendrá todos los valores de densidad que empiecen por 2 ej: lista_1 = ["134324", "1354211", "349.34"]

def get_data():
    with open("municipalities.json", "r", encoding="utf8") as file:
        data = json.load(file)["data"]
        return data

data = get_data()

def bonus_benford(given_list):
    list_1 = list(filter(lambda num: str(num["densidad_por_km2"]).startswith('1'),given_list))
    list_2 = list(filter(lambda num: str(num["densidad_por_km2"]).startswith('2'),given_list))
    list_3 = list(filter(lambda num: str(num["densidad_por_km2"]).startswith('3'),given_list))
    return len(list_1)/len(given_list), len(list_2)/len(given_list), len(list_3)/len(given_list)

lista1,lista2, lista3 = bonus_benford(data)
#print(lista1)
#print(lista2)
#print(lista3)

def benford(given_list):
    result = {}
    for num in range(1,10):
        result[str(num)] = len(list(filter(lambda mun: str(mun["densidad_por_km2"]).startswith(str(num)), given_list)))/len(given_list)
    return result

benford_v = benford(data)
#print(benford_v)

#! Ejercicio 6: Crear una función que acepte un solo parámetro (municipio) y que devuleva un objecto con las propiedades (nombre, densidad, superfice)

def create_mun(municipality):
    mun = Municipality(municipality["densidad_por_km2"], municipality["municipio_nombre"], municipality["superficie_km2"])
    return mun

#test = create_mun(data[0])
#print(test.population())

#! Ejercicio 8: Crear una función que acepte como parámetro toda la lista de diccionarios y devuelva una lista de objetos

def create_mun_list(data):
    result = list(map(lambda mun: create_mun(mun), data))
    return result

mun_list = create_mun_list(data)
#print(mun_list)

#! Ejercicio 10: Ya que tenemos una lista con todos los objetos, con su método "get_total_density()" obtener la densidad total de la comunidad de Madrid

def total_population(given_list):
    # for mun in given_list: #? Opción clásica
    #  result += mun.population()
    # return result

    # result = sum(list(map(lambda mun: mun.population(),given_list))) #? Opción simple con Map
    # return result
    result = 0
    for population in map(lambda mun: mun.population(),given_list): #? Opción mixta 
        result += population
    return result

print(total_population(mun_list))

#! Ejercicio 11: Crea un contador de modo que cada vez que se cree una nueva instancia, el mencionado contador aumente en 1
print(Municipality.count)