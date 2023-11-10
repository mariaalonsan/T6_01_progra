"""
1) Crea una función llamada "volumen_de_esfera" que reciba un argumento "radio" (un número real) y calcule el volumen de una esfera utilizando la fórmula:**

$$Volumen = \frac{4}{3} \pi r^3$$

* La función debe devolver el volumen de la esfera.
* Luego, solicita al usuario que ingrese el valor del radio y utiliza la función para calcular el volumen de la esfera. 
* Muestra el resultado.

__Nota__: Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:
```python
import math
print(math.pi)
> 3.1415...
```
"""


"""PRIMERA MANERA: sin usar bibliotecas"""


# Primero vamos a pedir al usuario que ingrese un valor para el radio y poder empezar a hacer los calculos
radio = int(input("Introduce el radio de la esfera: "))
print("El radio de la esfera es " + str(radio) + "\n")


# Definimos la función con el nombre volumen_de_esfera para calcular el volumen de la esfera 
def volumen_de_esfera(radio):
    # Definimos pi como 3.14159 (como dice el enunciado)
    pi = 3.14159
    # Aplicamos la fórmula (4/3) * pi * radio^3 para calcular el volumen
    return (4.0 / 3.0) * pi * (radio ** 3)


# Después llamamos a la función con el valor del radio y almacenamos el resultado en 'volumen'
volumen = volumen_de_esfera(radio)

# Y por último printeamos el resultado
print("El volumen de una esfera es " + str(volumen) + "\n")



"""SEGUNDA MAMERA: usando la biblioteca import math"""

import math  # Importamos la biblioteca math para tener acceso a pi con más decimales y otras funciones matemáticas

# Pedimos al usuario que ingrese un valor para el radio y poder empezar a hacer los calculos
radio = int(input("Introduce el radio de la esfera: "))
print("El radio de la esfera es " + str(radio) + "\n")

# Definimos la función
def volumen_de_esfera(radio):
    # Utilizamos la fórmula dada (4/3) * pi * radio^3 para calcular el volumen
    return (4.0/3.0) * math.pi * (radio ** 3)

volumen = volumen_de_esfera(radio)

print("El volumen de una esfera es " + str(volumen) + "\n") 
# El volumen da mas porque import math usa para pi mas decimales que 3.14159
