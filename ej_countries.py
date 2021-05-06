
#! Ejercicio 1: Crea, en un directorio aparte, un entorno virtual y un archivo main.py
#! Ejercicio 2: Instalar la librería requests
import requests as req
import json
import csv
import time
import concurrent.futures
from Models2 import Country

#! Ejercicio 3: Hacer una request a la url que nos traiga todos los países del mundo
#response = req.get('https://restcountries.eu/rest/v2/all').json()
#with open ("D:/Programación/Cice/Master Python/Unidad_2/countries.json","w", encoding='utf8') as file:
#    json.dump(response, file, ensure_ascii=False, indent=4)

def get_data():
    with open("D:/Programación/Cice/Master Python/Unidad_2/countries.json", "r", encoding="utf8") as file:
        data = json.load(file)
        return data
data = get_data()
#print(len(data))

#! Ejercicio 4: Crear una pequeña aplicación con las siguientes características:
#!    Debe permitirnos buscar países por nombre y por continentes Cada uno de los países buscados debe quedar escrito en un archivo tipo csv que solo admitirá los siguientes 
#!    valores: name, capital, region, population, area, idioma (el primero), flag A su vez estos valores acturán como encabezados
def menu_principal():
    print('------------------------------')
    print('1- Buscar país')
    print('2- Buscar continente')
    print('3- Consultar población')
    print('4- Historial')
    print('5- Consultar población mundial')
    print('0- Salir')
    print('------------------------------')

def choose():
    return input('Elija opción:')

def open_csv(file_csv):
    with open(file_csv,"r", newline='', encoding='utf8') as file:
        historial = csv.reader(file)
        next(historial)
        return list(historial)

def req_countries(pais):
    return req.get(f'https://restcountries.eu/rest/v2/name/{pais}').json()[0]

def req_continent(continent):
    return req.get(f'https://restcountries.eu/rest/v2/region/{continent}').json()[0]

def record_csv(country):
    try:
        with open("Unidad_2/historial.csv","r", newline='', encoding='utf8') as file:
            with open("Unidad_2/historial.csv","a", newline='', encoding='utf8') as file:
                writer = csv.writer(file, delimiter=',')
                data = [country['name'],country['capital'],country['region'],country['population'],country['area'],country['languages'][0],country['flag']]
                writer.writerow(data)
                return 'Datos de país añadidos al historial.'
    except FileNotFoundError:
        with open("Unidad_2/historial.csv","w", newline='', encoding='utf8') as file:
            writer = csv.writer(file, delimiter=',')
            data = ['PAIS','CAPITAL','CONTINENTE','POBLACION','SUPERFICIE','IDIOMA','BANDERA']
            writer.writerow(data)
            return 'Historial creado.'

def save_flags(country_list):
    url_img = country[-1]
    response = req.get(url_img).content
    name = country[0] # Otra opción: name = url_img.split('/')[-1]
    with open(f'Unidad_2/img/{name}.svg', 'wb') as img:
        img.write(response)
        print(f'Bandera {name} guardada.')

def create_country(country):
    country = Country(country['name'],country['capital'],country['population'])
    return country

menu_principal()
user = choose()
while user != 'q':
    if user == '1':
        user = input('Introduzca país: ')
        # start = time.perf_counter()
#! Ejercicio 5: Agregar un mensaje asíncrono que indique al usuario que se está procesando su respuesta
        with concurrent.futures.ThreadPoolExecutor() as executor:
            country = executor.submit(req_countries,user)
            print('Su petición esta siendo procesada')
            country = country.result()
        # finish = time.perf_counter()
        # print(finish-start)
        print(record_csv(country))
        print(f"{country['name']} con una población de {country['population']} habitantes.")
#! Ejercicio 8: Luego de buscar un país e imprimirlo por pantalla preguntar si desea guardar la imagen del país encontrado.
#! Ejercicio 9: Descargar la imagen indicada con anterioridad en --> ./images (Nota: El formato de las imágenes de restcountries es SVG)
        user = input('¿Desea descargar una imagen de la bandera?(Y/N)').lower()
        if user == 'y':
            url_img = country['flag']
            response = req.get(url_img).content
            name = country['name']
            with open(f'img/{name}.svg', 'wb') as img:
                img.write(response)
        menu_principal()
        user = choose()
    elif user == '2':
        user = input('Introduzca continente: ')
        response = req_continent(user)
        with open (f"D:/Programación/Cice/Master Python/Unidad_2/{user}.json","w", encoding='utf8') as file:
                json.dump(response, file, ensure_ascii=False)
        menu_principal()        
        user = choose()

#! Ejercicio 6: Agregar opción "population"
#! Ejercicio 7: Al elegir la opción population se obtendrá la población total que el usuario haya indicado anteriormente, de no existir el archivo manejar el error
    elif user == '3':
        user = input('Introduzca país: ').capitalize()
        reader = open_csv("Unidad_2/historial.csv")
        print(reader)
        population = sum(list(map(lambda country: int(country[3]) if country[0] == user else 0,reader)))
        if population > 0:
            print(f'{user} tiene {population} habitantes.')
        elif population == 0:
            print(f'El país {user} no se encuentra en la base de datos.', end='')
            resp = input('¿Desea añadirlo?(Y/N)').lower()
            if resp == 'y':
                country = req_countries(user)
                print(record_csv(country))
        menu_principal()        
        user = choose()

#! Ejercicio 10: Agregar una root function historial de búsqueda
#! Ejercicio 11: La función del ejercicio 10, entregará los nombres y las poblaciones de todos los países previamente buscados de la siguiente manera name:value**\n**poblacion: value
#! Ejercicio 12: Luego de mostrar la lista de países del ejercicio 10 preguntar si quiere descargar las banderas de los mismos
#! Ejercicio 13: Descargar todas las imágenes en un directorio aparte
    elif user == '4':
        historial = open_csv("Unidad_2/historial.csv")
        countrys = list(map(lambda country: (country[0],int(country[3])),historial))
        for country in countrys:
            print(f'Pais: {country[0]}\nPoblación: {country[1]}\n')
        user = input('Desea descargar las banderas de estos paises?(Y/N)').lower()
        if user == 'y':
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for country in historial:
                    flag = executor.submit(save_flags,country)
                    print('Su petición esta siendo procesada')
                    flag = flag.result()
        menu_principal()        
        user = choose()

#! Ejercicio 15: Convertir TODOS los países en un objeto y luego podamos acceder a un atributo de clase y nos indique la población total
    elif user == '5':
        result = list(map(lambda country: create_country(country), data))
        print(f'La población total del mundo es: {Country.populationTotal}')    
        menu_principal()        
        user = choose()

    elif user == '0':
        print('Adios...')
        user = 'q'

    else:
        print('No se ha reconocido su repuesta')
        menu_principal()        
        user = choose()