# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
# sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
# un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
# trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
# sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
# la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
# y justificar la complejidad del algoritmo.

#****************************************************************

# Resolver el problema del ejercicio 1 utilizando Backtracking.

#*****************************************************************
# 3. Se tiene como posibles grupos sanguíneos de personas O, A, B y AB. Alguien con sangre tipo O sólo puede recibir sangre
# tipo O. Alguien de sangre A sólo puede recibir sangre de tipo A u O. Alguien de sangre tipo B sólo puede recibir sangre
# de tipo B u O. Alguien con sangre tipo AB puede recibir sangre de cualquier tipo. Se tienen las cantidades de bolsas de
# sangre disponibles (SA, SB, SAB, SO) y la cantidad de personas a tratar (PA, PB, PAB, PO). Implementar un algoritmo
# greedy que determine cómo se puede satisfacer la demanda de sangre (o si no puede hacerse). Indicar el orden del
# algoritmo y justificar por qué el algoritmo propuesto es un algoritmo greedy.

