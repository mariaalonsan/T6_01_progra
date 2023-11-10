"""
5) Escribe un programa en Python que realice las siguientes tareas:**

1) Pide al usuario que ingrese un número entero positivo.
2) Crea una función llamada convertir_a_binario_hexadecimal(numero) que tome el número entero ingresado como argumento.
3) Dentro de la función, convierte el número a su equivalente en binario y hexadecimal.
4) La función debe devolver una tupla con dos elementos: el valor en binario y el valor en hexadecimal.
5) Muestra los valores originales, en binario y en hexadecimal utilizando la función.

+ Asegúrate de manejar casos en los que el usuario ingrese un número negativo o cero y proporciona un mensaje de error apropiado.

__NOTA:__ Recuerda que puedes utilizar las funciones _bin()_ y _hex()_  para realizar la conversión de números a binario y hexadecimal.
"""

# Pedimos al usuario que ingrese un número entero positivo
numero_ejemplo = int(input("Introduce un número entero positivo: "))     

# Definimos la función para convertir un número a su representación binaria y hexadecimal
def convertir_a_binario_hexadecimal(numero):
    # Verificamos si el número es positivo. Si no lo es, devolvemos un mensaje de error
    if numero <= 0:
        return "Error: Por favor, ingresa un número entero positivo."
    # Convertimos el número a binario y hexadecimal
    binario = bin(numero)[2:]  # Usamos [2:] para quitar el prefijo '0b' del resultado
    hexadecimal = hex(numero)[2:]  # Usamos [2:] para quitar el prefijo '0x' del resultado
    # Devolvemos una tupla con las representaciones binaria y hexadecimal
    return (binario, hexadecimal)

# Llamamos a la función con el número de ejemplo y almacenamos el resultado
resultado_conversion = convertir_a_binario_hexadecimal(numero_ejemplo)

print("El número " + str(numero_ejemplo) + " en binario es '" + resultado_conversion[0] + "' y en hexadecimal es '" + resultado_conversion[1] + "'\n")