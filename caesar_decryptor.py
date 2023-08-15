#/usr/bin/env python3

# Decryptor para cifrado del César hecho por m4t1
import string, sys

# Lista de letras del abecedario
listaAbecedario = list(string.ascii_uppercase)

# Leer el texto cifrado
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        ciphert = file.read().strip()
else:
    ciphert = input("Introduce el texto cifrado: ")

# Descifrado utilizando el cifrado del César
for offset in range(1, 25):

    #Inicializamos una cadena de texto decyphered para cada iteracion
    decrypted_text = ""

    #Para cada letra en el texto cifrado
    for char in ciphert:

        #Si la letra está en el abecedario:
        if char in listaAbecedario:

            #Calculamos el índice de la letra en el diccionario
            index = listaAbecedario.index(char)

            #Calculamos su offset, cogemos el indice en el abecedario, le restamos el offset y fuera
            decrypted_index = (index - offset) % 26

            #Añadimos a la cadena vacía el valor del diccionario calculado
            decrypted_char = listaAbecedario[decrypted_index]
            decrypted_text += decrypted_char
        else:
            #Si no está contemplado en el diccionario, lo añadimos tal cual
            decrypted_text += char

    #Imprimimos el resultado de la decodificación de cada iteración
    print(f"Iteración {offset} --> {decrypted_text}")
