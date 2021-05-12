
#! Crear vuestra propia BBDD (JSON)
#import requests as req
import os
import fun_deas as fun
import utm
import geocoder
import bcrypt

# response = req.get("https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json").json()
# with open ("D:/Programación/Cice/Master Python/Unidad_2/deas.json","w", encoding='utf8') as file:
#    json.dump(response, file, ensure_ascii=False, indent=4)

di_path = os.path.realpath(__file__)[0:-10]
data = fun.read_data(f'{di_path}deas.json')["data"]

#! 1- Cuántos DEAS hay en total
#print(f'Hay {len(data)} DEAS en la comunidad de Madrid')

#! 2- Considerando solo los DEAS de los códigos postales dentro de la M-30, cuántos hay?
cp_in_m30 = ["28029", "28036", "28046", "28039", "28016", "28020", "28002", "28003", "28015", "28010", "28006", "28028", "28008", "28004", "28001", "280013", "28014", "28009", "28007", "28012", "28005", "28045"]
result_m30 = [dea for dea in data if dea['direccion_codigo_postal'] in cp_in_m30]
result_none = [dea for dea in data if dea['direccion_codigo_postal'] == '']
#print(f'Hay {len(result_m30)} DEAS dentro de la M-30')
#print(f'Hay {len(result_none)} resultados sin código postal')

#! 3- Cuántos se encuentran en entidades públicas y cuántos en privadas?
result_publica = [dea for dea in data if dea['tipo_titularidad'] == "Pública"]
#print(f'Hay {len(result_publica)} DEAS en entidades públicas')
result_privadas = len(data)-len(result_publica)
#print(f'Hay {result_privadas} DEAS en entidades privadas')

#! 4- Crear un menu
fun.menu()
user = fun.choose()

while user != 'q':
    if user == '1':
        path = "D:/Programación/Cice/Master Python/Unidad_2/users.json"
        name = input('\tIntroduzca su nombre: ')
        password = input('\tIntroduzca su password: ')
        fun.add_user(path, name, password)
        fun.menu()
        user = fun.choose()
    elif user == '2':
        fun.menu2()
        user = fun.choose()
        if user == '1':
            resp = input('\tIntroduzca el código DEA: ')
            dea_cp = [dea for dea in data if dea['codigo_dea'] == resp]
            if len(dea_cp) == 0:
                print('\n\t No existen coincidencias con el código introducido.')
            else:
                fun.dea_tostring(dea_cp)
            fun.menu()
            user = fun.choose()
        elif user == '2':
            #pos_x = int(input('\tIndique su coordenada X: '))
            #pos_y = int(input('\tIndique su coordenada Y: '))
            geo_me = geocoder.ip('me') #'83.45.28.167'
            pos_me = utm.from_latlon(geo_me.latlng[0],geo_me.latlng[1],30,'T')
            min_distance, dea_prox = fun.compare_distance(data, pos_me[0], pos_me[1])
            print(f'\n\tCÓDIGO: {dea_prox["codigo_dea"]}, NOMBRE: {dea_prox["direccion_ubicacion"]}, DIRECCIÓN: {dea_prox["direccion_via_nombre"]} {dea_prox["direccion_portal_numero"]}')
            print(f'\tEl DEA se encuentra a una distancia de: {round(min_distance,2)} metros.') # y: 4475691 x: 439444
            #userlatlong = utm.to_latlon(pos_x, pos_y, 30,'T')
            latlong = utm.to_latlon(int(dea_prox['direccion_coordenada_x']),int(dea_prox['direccion_coordenada_y']),30,'T')
            print(f'\tDESTINO EN MAPS --> https://www.google.com/maps/search/?api=1&query={latlong[0]},{latlong[1]}')
            print(f'\tRUTA EN MAPS ---> https://www.google.com/maps/dir/{pos_me[0]},+{pos_me[1]}/{latlong[0]},{latlong[1]}')
            fun.menu()
            user = fun.choose()
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