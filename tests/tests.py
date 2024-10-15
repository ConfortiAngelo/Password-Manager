from password_manager.password_generator import * 
from password_manager.access import *
from password_manager.security import *
from password_manager.storage import *

usuario1 = "Angelo"
password = passoword_generator()
salt_password , hashing_password = hash_password(password)
salt_juan,hash_Juan = hash_password("123456789") 
Users_list = [(usuario1,hashing_password, salt_password),("Pedro","1234","1234")] 
list = [("Juan",hash_Juan,salt_juan)]
create_database()
insert_user(list)
insert_user(Users_list)
print(read_table())

print(login())
user = "Angelo"
print(login())