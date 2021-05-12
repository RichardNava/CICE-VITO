import bcrypt

password = input('Contraseña: ').encode()
password_encriptada = bcrypt.hashpw(password, bcrypt.gensalt())
print(password_encriptada)
veredict = True if bcrypt.checkpw(password, password_encriptada) else False
if veredict:
    print('Puedes acceder')
else:
    print('No puedes acceder')