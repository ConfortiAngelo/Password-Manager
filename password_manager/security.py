import hashlib
import os
from storage import *

"""Funcion que me genera un hash SHA256 añadiendo "salt" a una contraseña ingresada por el usuario o por la funcion passoword_generator"""
def hash_password(password):
    #me genera un salt aleatorio de 16 bytes    
    salt = os.urandom(16)
    #le agregi mi salt a la contraseña y le hago el SHA-256
    hashing_password = hashlib.sha256(salt + password.encode("utf-8")).hexdigest()

    return salt.hex() ,hashing_password
""""FUNCION QUE VERIRICA EL HASH"""
def hash_verify(password, salt):
    # Convertir el salt a bytes si está en formato hexadecimal
    if isinstance(salt, str):  # Verifica si es string
        salt = bytes.fromhex(salt)  # Lo convierte a bytes
    
    # Realiza la concatenación con ambos objetos en formato bytes
    hash_password = hashlib.sha256(salt + password.encode("utf-8")).hexdigest()
    return hash_password
