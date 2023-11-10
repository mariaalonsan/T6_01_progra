"""
3) Crea una función llamada suma_serie_geometrica que reciba tres argumentos: _a_ (el primer término de la serie), _r_ (la razón de la serie) y _n_ (el número de términos a sumar). La función debe calcular y devolver la suma de los primeros n términos de una serie geométrica con primer término a y razón r.** 

Una secuencia geométrica es una secuencia de números en la que cada término después del primero se obtiene multiplicando el término anterior por una constante fija, que se llama "razón". La razón se denota generalmente como "r".

La fórmula general para una serie geométrica infinita es:

$$S=a+ar+ar^2+ar^3+…=\sum_{n=0}^{\infty} ​ar^n$$

Donde:  
_S_ es la suma de la serie.  
_a_ es el primer término de la serie.  
_r_ es la razón común entre los términos sucesivos.  
_n_ es un índice que varía desde 0 hasta infinito.

* Prueba la función para sumar los primeros 10 términos de una serie con a = 5 y r = 4.
"""


# Empezamos definiendo la función para calcular la suma de los primeros n términos de una serie geométrica
def suma_serie_geometrica(a, r, n):
    # Iniciamos la suma en 0
    suma = 0
    # Utilizamos un bucle for para calcular cada término de la serie y sumarlo a la suma total
    for i in range(n):
        # Calculamos el término actual elevando la razón r a la potencia del índice actual
        termino_actual = a * (r ** i)
        # Sumamos el término actual a la suma total
        suma += termino_actual
    return suma

# Probamos la función con a = 5, r = 4 y los primeros 10 términos
resultado = suma_serie_geometrica(5, 4, 10)

# Printeamos el resultado
print("El resultado de sumar los primeros 10 términos de una serie con a = 5 y r = 4 es " + str(resultado) + "\n")