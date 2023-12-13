# 2. Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una
# misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso
# está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. Por problemas presupuestarios, sólo
# pueden pintar los colectivos de k colores diferentes (por ejemplo, k = 4, pero podría se otro valor). Como no quieren
# parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber si es posible
# cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color
# coincidiendo en la misma parada). Considerando que se tiene la información de todas las paradas de colectivo y qué
# líneas paran allí, modelar el problema utilizando grafos e implementar un algoritmo que determine si es posible resolver
# el problema. Indicar la complejidad del algoritmo implementado.

# 3. Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
# utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
# Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1**2, por lo que siempre existe solución.

# Sin embargo, la expresión 10 = 3**2 + 1**2

# es una manera más económica de escribirlo para n = 10, pues sólo tiene dos
# términos. Además, tener en cuenta que no se piden los términos, sino la cantidad mínima de términos cuadráticos
# necesaria.

# 4. Realizar una reducción polinomial del problema del ejercicio 3 a otro de los vistos durante la cursada. Ayuda: pensar en
# alguno de los vistos de programación dinámica.

# 5. Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta la capacidad a una artista, permita
# obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. Indicar y justificar la complejidad del algoritmo
# implementado.