import sqlite3 as sql


"""Funcion para crear mi baso de datos"""
def create_database():
    conexion = sql.connect("Users.db")
    cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE Users (
                    name text,
                    hash text,
                    salt text
                    )"""
                )
    conexion.commit()
    conexion.close()

def insert_user(user_list):
    conexion = sql.connect("Users.db")
    cursor = conexion.cursor()
    intructions = f"INSERT INTO Users VALUES (?,?,?)"
    cursor.executemany(intructions,user_list)
    conexion.commit()
    conexion.close()

def read_table():
    conexion = sql.connect("Users.db")
    cursor = conexion.cursor()
    instructions = f"SELECT * FROM Users"
    cursor.execute(instructions)
    data = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return data

def query_name(name):
    conexion = sql.connect("Users.db")
    cursor = conexion.cursor()
    instructions = f"SELECT * FROM Users WHERE name = '{name}'"
    cursor.execute(instructions)
    data = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return data

