#/usr/bin/env python3

import string

#Script para cifrar texto empleando el cifrado del César hecho por m4t1

# Lista de letras del abecedario
listaAbecedario = list(string.ascii_uppercase)

# Leer el texto a cifrar
texto_a_cifrar = input("Introduce el texto a cifrar: ")

# Offset a meterle al texto cifrado
offset = int(input("Introduce el número de iteraciones: "))

# Cifrado utilizando el cifrado del César
texto_cifrado = ""

for char in texto_a_cifrar:

    # Si el carácter está en el abecedario:
    if char in listaAbecedario:

        # Calculamos el índice del carácter en el diccionario
        index = listaAbecedario.index(char)

        # Calculamos el índice cifrado, cogemos el índice en el abecedario, le sumamos el desplazamiento y aplicamos módulo 26
        indice_ciph = (index + offset) % 26

        # Agregamos a la cadena cifrada el valor del diccionario calculado
        letra_ciph = listaAbecedario[indice_ciph]
        texto_cifrado += letra_ciph
    else:
        # Si no está en el diccionario, lo agregamos tal cual
        encrypted_text += char

# Imprimimos el resultado del cifrado
print(f"Texto cifrado --> {texto_cifrado}")
