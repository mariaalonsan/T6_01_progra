"""
Escribe una función llamada _exponenciacion_ que acepte dos argumentos, la base _a_ y el exponente _n_. La función debe devolver el resultado de elevar la base a la potencia del exponente utilizando un bucle.** 

* Utiliza la función para calcular 2 elevado a la 10.
"""

# Primero definimos la función exponenciacion que calcula la potencia de un número
def exponenciacion(a, n):
    # Empezamos el resultado con 1, ya que cualquier número elevado a  0 es 1
    resultado = 1
    # Para multiplicar la base por sí misma n veces, vamos a utilizar un bucle for
    for _ in range(n):
        resultado *= a
    # Y terminamos el bucle devolviendo el resultado de la base elevada a la potencia del exponente
    return resultado

# Por ultimo utilizamos la función para calcular 2 elevado a la 10
resultado_potencia = exponenciacion(2, 10)

print("El resultado de 2 elevado a la 10 es " + str(resultado_potencia) + "\n")