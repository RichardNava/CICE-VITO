
#! Ejercicio 1: Crea, en un directorio aparte, un entorno virtual y un archivo main.py
#! Ejercicio 2: Instalar la librería requests
import requests as req
import json
import csv
import time
import concurrent.futures

#! Ejercicio 3: Hacer una request a la url que nos traiga todos los países del mundo
#response = req.get('https://restcountries.eu/rest/v2/all').json()
#with open ("D:/Programación/Cice/Master Python/Unidad_2/countries.json","w", encoding='utf8') as file:
#    json.dump(response, file, ensure_ascii=False)

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
    print('1- Buscar país')
    print('2- Buscar continente')
    print('0- Salir')

def choose():
    return input('Elija opción:')

menu_principal()
user = choose()

def req_countries(pais):
    return req.get(f'https://restcountries.eu/rest/v2/name/{pais}').json()[0]

while user != 'q':
    if user == '1':
        user = input('Introduzca país: ')
        start = time.perf_counter()
#! Ejercicio 5: Agregar un mensaje asíncrono que indique al usuario que se está procesando su respuesta
        with concurrent.futures.ThreadPoolExecutor() as executor:
            country = executor.submit(req_countries,user)
            print('Su petición esta siendo procesada')
            country = country.result()
        finish = time.perf_counter()
        print(finish-start)
        try:
            with open("historial.csv","r", newline='', encoding='utf8') as file:
                with open("historial.csv","a", newline='', encoding='utf8') as file:
                    writer = csv.writer(file, delimiter=',')
                    data = [country['name'],country['capital'],country['region'],country['population'],country['area'],country['languages'][0],country['flag']]
                    writer.writerow(data)
        except FileNotFoundError:
            with open("historial.csv","w", newline='', encoding='utf8') as file:
                writer = csv.writer(file, delimiter=',')
                data = ['PAIS','CAPITAL','CONTINENTE','POBLACION','SUPERFICIE','IDIOMA','BANDERA']
                writer.writerow(data)
        print(f"{country['name']} con una población de {country['population']} habitantes.")
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
        response = req.get(f'https://restcountries.eu/rest/v2/region/{user}').json()
        #print(f"{country['name']} con una población de {country['population']} habitantes.")
        with open (f"D:/Programación/Cice/Master Python/Unidad_2/{user}.json","w", encoding='utf8') as file:
                json.dump(response, file, ensure_ascii=False)
        menu_principal()        
        user = choose()
    elif user == '0':
        print('Adios...')
        user = 'q'
    else:
        print('No se ha reconocido su repuesta')
        user = choose()