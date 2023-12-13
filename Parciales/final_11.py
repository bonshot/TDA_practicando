# 1. Implementar un algoritmo que, por backtracking, obtenga todos los posibles ordenamientos topológicos de un grafo
# dirigido y acíclico.

# 3. Dada una soga de n metros (n ≥ 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla
# (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El
# algoritmo debe devolver el valor del producto máximo alcanzable. Indicar y justificar la complejidad del algoritmo.
# Ejemplos:
# n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
# n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
# n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
# n = 10 -> Debe devolver 36 (producto máximo es 3 * 3 * 4)

# 4. Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
# Implementar un algoritmo que Greedy que dé la cantidad mínima de faros que se necesitan para que todos los
# submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las
# diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la complejidad
# del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima?