from models_dea import Dea
import json

def menu():
    print('----------------')
    print('1- Crear Usuario')
    print('2- Acceder')
    print('3- Admins')
    print('0- Salir')
    print('----------------')

def choose():
    resp= input('Elija una opción: ')
    return resp

def menu2():
    print('\t------------------------------')
    print('\t 1- ¿Buscar DEA por código?')
    print('\t 2- ¿Buscar DEA por distancia?')
    print('\t------------------------------')

def create_dea(dea):
    new_dea = Dea(dea['codigo_dea'], int(dea['direccion_coordenada_x']), int(dea['direccion_coordenada_y']))
    return new_dea

def compare_distance(dea_list, pos_x, pos_y):
    maxi = 1000000000000
    result = 0
    prox_dea = None
    for dea in dea_list:
        new_dea = create_dea(dea)
        result = new_dea.calculate_distance(pos_x, pos_y)
        if result <= maxi:
            maxi = result
            prox_dea = dea
    return maxi, prox_dea

def dea_tostring(dea_list):
    for dea in dea_list:
        print(f'\tCódigo: {dea["codigo_dea"]}, Nombre: {dea["direccion_ubicacion"]}, Dirección: {dea["direccion_via_nombre"]} {dea["direccion_portal_numero"]}')

def read_data(path):
    with open(path, "r", encoding="utf8") as file: 
        return json.load(file)

def write_data(path,data):
    with open (path,"w", encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_user(path, name, password):        
    users =  read_data(path)
    users["data"].append({"name": name, "password": password})
    write_data(path, users)