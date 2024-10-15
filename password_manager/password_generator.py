import random 
import string


"""Funcion que me genera contraseñas seguras"""
def passoword_generator(lenght = 16 ,special_characters = True):
    if lenght >= 16:
        #ascii_letters me genera todas las letras mayusculas y minusculas
        #digits me genera todos los numeros del 0 - 9
        chars = string.ascii_letters + string.digits
        if special_characters:
            #punctuation me genera todos los simbolos especiales
            chars += string.punctuation        
        #join me une todos los elementos a una lista, .choice me selecciona elementos de "chars" , mi for repite esto dependiendo de mi lenght
        password = ''.join(random.choice(chars) for _ in range(lenght))
        return password
    else:
        return "La longitud de la contraseña debe de ser mayor o igual a 16"




