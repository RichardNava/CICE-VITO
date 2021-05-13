from models_dea import Dea
import json
import bcrypt
import geocoder
import utm

def menu():
    print('----------------')
    print('1- Crear Usuario')
    print('2- Acceder')
    print('3- Admins')
    print('0- Salir')
    print('----------------')

def choose(tab=''):
    resp= input(f'{tab}Elija una opción: ')
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

def dea_by_code(data):
    resp = input('\tIntroduzca el código DEA: ')
    dea_cp = [dea for dea in data if dea['codigo_dea'] == resp]
    if len(dea_cp) == 0:
        print('\n\tNo existen coincidencias con el código introducido.')
    else:
        dea_tostring(dea_cp)

def dea_by_distance(data):
    #pos_x = int(input('\tIndique su coordenada X: '))
    #pos_y = int(input('\tIndique su coordenada Y: '))
    geo_me = geocoder.ip('me') #'83.45.28.167'
    pos_me = utm.from_latlon(geo_me.latlng[0],geo_me.latlng[1],30,'T')
    min_distance, dea_prox = compare_distance(data, pos_me[0], pos_me[1])
    print(f'\n\tCÓDIGO: {dea_prox["codigo_dea"]}, NOMBRE: {dea_prox["direccion_ubicacion"]}, DIRECCIÓN: {dea_prox["direccion_via_nombre"]} {dea_prox["direccion_portal_numero"]}')
    print(f'\tEl DEA se encuentra a una distancia de: {round(min_distance,2)} metros.') # y: 4475691 x: 439444
    #userlatlong = utm.to_latlon(pos_x, pos_y, 30,'T')
    latlong = utm.to_latlon(int(dea_prox['direccion_coordenada_x']),int(dea_prox['direccion_coordenada_y']),30,'T')
    print(f'\tDESTINO EN MAPS --> https://www.google.com/maps/search/?api=1&query={latlong[0]},{latlong[1]}')
    print(f'\tRUTA EN MAPS ---> https://www.google.com/maps/dir/{pos_me[0]},+{pos_me[1]}/{latlong[0]},{latlong[1]}')
    
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

def create_user(path,users_list):
    name, password = log_input()
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    if next(map(lambda user: user["name"] == name, users_list),False):
        print('El usuario ya existe.')
    else:
        add_user(path, name, password.decode())

def log_input():
    name = input('\tIntroduzca su nombre: ').capitalize()
    password = input('\tIntroduzca su password: ').encode()  
    return name, password

def log_in(users_list):
    name, password = log_input()
    user_comp =  next(filter(lambda user: user["name"] == name, users_list),False)
    password_pass = user_comp["password"] if user_comp else False
    veredict = False
    if password_pass:
        veredict = True if bcrypt.checkpw(password, password_pass.encode()) else veredict
    return veredict

def menu2_functions(data):
    menu2()
    user = choose('\t')
    if user == '1':
        dea_by_code(data)
    elif user == '2':
        dea_by_distance(data)  