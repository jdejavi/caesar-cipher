# Cifrado y Descifrado César

Este repositorio contiene scripts en Python para realizar el cifrado y descifrado utilizando el cifrado César. Hay dos scripts: uno para cifrar y otro para descifrar textos.

Hecho por Javier Matilla Martín aka. _m4t1_ espero que lo disfrutéis! >:)

## Cifrado

El archivo `caesar_encrypt.py` es un script que te permite cifrar un texto utilizando el cifrado César. El usuario proporciona un texto y un número de iteraciones para el cifrado.

### Modo de uso

Ejecuta el siguiente comando en tu terminal para cifrar un texto:


`python3 caesar_encrypt.py`

Sigue las instrucciones que aparecen en pantalla para ingresar el texto a cifrar y el número de iteraciones.

### Descifrado

El archivo `caesar_decrypt.py` es un script que te permite descifrar un texto cifrado utilizando el cifrado César. El usuario proporciona un texto cifrado y el script probará todas las posibles claves para obtener el texto original.

#### Modo de uso


- El script te pedirá que ingreses manualmente el texto cifrado, para ejecutarlo deberemos escribir por consola lo siguiente:

`python3 caesar_decrypt.py`

Sigue las instrucciones que aparecen en pantalla para descifrar el texto.

El archivo `caesar_decrypt.py` también permite descifrar un texto cifrado utilizando el cifrado César. El usuario proporciona un texto cifrado y el script probará todas las posibles claves para obtener el texto original.

### Modo de uso

Puedes ejecutar el script de dos formas diferentes:

- Proporcionando el texto cifrado como argumento de entrada desde un archivo de texto: `python3 caesar_decrypt.py archivo_cifrado.txt`

Asegúrate de tener un archivo llamado archivo_cifrado.txt en la misma ubicación que el script, y que contenga el texto cifrado.

- Si no proporcionas un archivo de texto, el script te pedirá que ingreses manualmente el texto cifrado:

`python3 caesar_decrypt.py`

Sigue las instrucciones que aparecen en pantalla para descifrar el texto.

