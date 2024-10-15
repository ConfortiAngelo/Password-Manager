# Funciones del Proyecto 

## Funciones en `access.py`

### login()
Solicita al usuario su nombre de usuario y contraseña, y verifica si las credenciales son correctas. Retorna un mensaje indicando si el acceso fue permitido o denegado.

### register()
Permite a un nuevo usuario crear una cuenta, solicitando un nombre de usuario y una contraseña. Retorna un mensaje indicando si el registro fue exitoso o si hubo un error (como contraseñas no coincidentes o nombre de usuario ya existente).

## Funciones en `password_generator.py`

### passoword_generator(lenght=16, special_characters=True)
Genera una contraseña aleatoria de una longitud especificada, incluyendo letras, números y caracteres especiales, si se indica. Retorna la contraseña generada.

## Funciones en `security.py`

### hash_password(password)
Recibe una contraseña y genera un hash utilizando el algoritmo SHA-256, añadiendo un "salt" aleatorio. Retorna el salt en formato hexadecimal y el hash de la contraseña.

### hash_verify(password, salt)
Verifica una contraseña proporcionada con su hash correspondiente y el salt utilizado durante la creación del hash. Retorna el hash calculado para su comparación.

## Funciones en `storage.py`

### create_database()
Crea una base de datos SQLite llamada `Users.db` con una tabla para almacenar usuarios, hashes y salts.

### insert_user(user_list)
Inserta una lista de usuarios en la base de datos. Cada usuario es una tupla que contiene el nombre, hash y salt.

### read_table()
Lee todos los registros de la tabla `Users` en la base de datos y retorna los datos en forma de lista.

### query_name(name)
Consulta la base de datos para verificar si un nombre de usuario ya está registrado. Retorna los datos del usuario si se encuentra.

