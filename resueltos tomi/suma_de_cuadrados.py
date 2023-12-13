optimos = dict()
import math


def suma_cuadrados(n):
    if n == 1:
        return [1]

    if n in optimos:
        return optimos[n]

    min_valor = None
    for i in range(1, math.ceil(n ** (1 / 2))):
        valor = i**2
        cant = len(suma_cuadrados(n - valor))
        if min_valor == None or cant < len(min_valor):
            min_valor = [*suma_cuadrados(n - valor), valor]
    optimos[n] = min_valor
    return min_valor

print(suma_cuadrados(545))

# Complejidad:
# n^sqrt(n)