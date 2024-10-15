from storage import *
from password_generator import * 
from security import *


"""Funcion para logear un usuario"""
#Esta funcion pide usuario y contraseña, Luego busca al "usuario" en la BD,en caso de que no se encuentre en la BD  retorna un comentario.
#Caso contrario,  procede a comparar el valor del hash y del salt con el de la BD , esto lo hace llamando a una funcion que a la password ingresada le aplica el salt, y veririca si coincide el hash.
#En caso de que la contraseña no coincida, le permite ingresar un maximo de 2 veces mas, si en ninguna coincide, diniega el acceso no permitiendo hacer ataques de fuerza bruta

def login():
    usuario = str(input("Ingrese su usuario: "))
    password = str(input("Ingrese su contraseña: "))
    data = query_name(usuario)
    intentos = 0
    if len(data) > 0:
        run = True
        while run:
            if intentos <= 2:
                if data[0][1] == hash_verify(password,data[0][2]):
                    intentos = 2
                    return "Acceso permitido"
                elif data[0][1] != hash_password(password,data[0][2]) and intentos < 2:
                    print("Contraseña incorrecta!!, Vuelva a intentar")
                    password = str(input("Ingrese su contraseña: "))
                intentos += 1
            else:
                run = False
                return "Acceso denegado, Limite de intentos superado!!"
    else:
        return "Usuario no registrado"

""""FUNCION REGISTER"""
#Esta funcion pide usuario, verifica que el usuario no exista en la BD, en caso de que exista pide volver a intentar con otro usuario.
#En caso de que no exista, pide una contraseña, verifica que cumpla la condicion de que tenga mas de 16 caracteres, en caso de que no cumpla pide volver a intentar. Si cumple la condicion pide que repita la contraseña
#Si las contraseñas coinciden , registra al usuario exitosamente, en caso contrario  pide volver a intentar
def register():
    usuario = str(input('Ingrese un nombre de usuario: '))
    name = query_name(usuario)
    if len(name) == 0:
        password = str(input("Ingrese una contraseña: "))
        if len(password) >= 16:
            repetir_password = str(input("Repita la contraseña: "))
        else:
            return "La contraseña es demaciado corta, vuelva a intentar!!"
        if password == repetir_password:
            salt , hash = hash_password(password)
            insert_user([(usuario,hash,salt)])
            return "Usuario registrado"
        else:
            return "Las contraseñas no coinciden, vuelva a intentar"
    else:
        return "El usuario ya existe!"