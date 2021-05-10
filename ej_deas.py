
#! Crear vuestra propia BBDD (JSON)
import requests as req
import json
import os
import fun_deas as fun

di_path = os.path.realpath(__file__)[0:-10]
# response = req.get("https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json").json()
# with open ("D:/Programación/Cice/Master Python/Unidad_2/deas.json","w", encoding='utf8') as file:
#    json.dump(response, file, ensure_ascii=False, indent=4)

def get_data():
    with open(f'{di_path}deas.json', "r", encoding="utf8") as file:
        data = json.load(file)["data"]
        return data
data = get_data()

#! 1- Cuántos DEAS hay en total
print(f'Hay {len(data)} DEAS en la comunidad de Madrid')

#! 2- Considerando solo los DEAS de los códigos postales dentro de la M-30, cuántos hay?
cp_in_m30 = ["28029", "28036", "28046", "28039", "28016", "28020", "28002", "28003", "28015", "28010", "28006", "28028", "28008", "28004", "28001", "280013", "28014", "28009", "28007", "28012", "28005", "28045"]
result_m30 = [dea for dea in data if dea['direccion_codigo_postal'] in cp_in_m30]
result_none = [dea for dea in data if dea['direccion_codigo_postal'] == '']
print(f'Hay {len(result_m30)} DEAS dentro de la M-30')
print(f'Hay {len(result_none)} resultados sin código postal')

#! 3- Cuántos se encuentran en entidades públicas y cuántos en privadas?
result_publica = [dea for dea in data if dea['tipo_titularidad'] == "Pública"]
print(f'Hay {len(result_publica)} DEAS en entidades públicas')
result_privadas = len(data)-len(result_publica)
print(f'Hay {result_privadas} DEAS en entidades privadas')

#! 4- Crear un menu
fun.menu()
user = fun.choose()

while user != 'q':
    if user == '1':
        pass
    elif user == '2':
        fun.menu2()
        user = fun.choose()
        if user == '1':
            resp = input('Introduzca el código postal: ')
            dea_cp = [dea for dea in data if data['direccion_codigo_postal'] == resp]
            for dea in dea_cp:
                print(f'Código: {dea["direccion_via_nombre"]}, Dirección: {dea["direccion_via_nombre"]} {dea["direccion_portal_numero"]}')
        elif user == '2':
            pass
        elif user == '0':
            fun.menu()
            user = fun.choose()
    elif user == '3':
        pass
    elif user == '0':
        user='q'
    else:
        print('No se reconoce su respuesta')
        fun.menu()
        user = fun.choose()