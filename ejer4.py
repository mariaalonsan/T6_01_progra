"""
4) Crea una función llamada "factorial" que reciba un número entero "n" como argumento y calcule el factorial de ese número. El factorial de un número entero positivo "n" se define como el producto de todos los enteros positivos desde 1 hasta "n".**

La fórmula del factorial es la siguiente:

$n!=n×(n−1)×(n−2)×…×1$

* La función debe devolver el resultado del cálculo del factorial.

* Utiliza esta función para calcular el factorial de un número que el usuario ingrese por teclado.
"""

# Definimos la función que calcula el factorial de un número entero positivo n
def factorial(n):
    # Iniciamos el factorial en 1, ya que el factorial de 0 es 1
    resultado = 1
    # Utilizamos un bucle for para calcular el producto de todos los enteros positivos hasta n
    for i in range(1, n + 1):
        resultado *= i
    # Devolvemos el resultado del cálculo factorial
    return resultado

# Aquí definimos numero_ejemplo y le ponemos un número de ejemplo para calcular su factorial
numero_ejemplo = 5

# Calculamos el factorial del número de ejemplo usando la función definida
resultado_factorial = factorial(numero_ejemplo)

print("El factorial de " + str(numero_ejemplo) + " es " + str(resultado_factorial) + "\n")

