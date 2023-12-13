# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
# sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
# un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
# trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
# sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
# la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
# y justificar la complejidad del algoritmo.

def bodegon(W, familias):
    n = len(familias)
    mesa = [[0]*(W+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if familias_chotas[i-1] > j:
                mesa[i][j] = mesa[i-1][j]
            else:
                mesa[i][j] = max(mesa[i-1][j], mesa[i-1][j-familias_chotas[i-1]] + familias_chotas[i-1])
    res = []
    i,j = n,W
    while i >0 and j > 0:
        if mesa[i][j] != mesa[i-1][j]:
            res.append(familias[i-1])
            j -= familias[i-1]
        i-=1
    return res[::-1]



# print(bodegon(11, [7,10,2,1,9,3]))
#La compejidad del algortimo O(N,W)
#ya que el llenar la mesa requiere dos ciclos anidados, por el largo de las familias
#y por el tamaño de la mesa
#****************************************************************

# Resolver el problema del ejercicio 1 utilizando Backtracking.
def bodegon_backtracking(W, familias, indice, asignacion_actual, mejor):
    if indice == len(familias):
        if sum(asignacion_actual) > sum(mejor):
            mejor = asignacion_actual
        return mejor
    else:
        if sum(asignacion_actual) + familias[indice] <= W:
            mejor = bodegon_backtracking(W, familias, indice+1, asignacion_actual + [familias[indice]], mejor)
        mejor = bodegon_backtracking(W, familias, indice+1, asignacion_actual, mejor)
    return mejor


# W=15
# familias = [5,2,1,6,4,3,15]
# print(sum(bodegon_backtracking(W,familias,indice=0, asignacion_actual=[], mejor=[])))
# La complejidad es O(2**n), donde n es el largo de las familias.
# La justificación se basa en la naturaleza de la recursión 
# y la cantidad de subproblemas que se deben resolver.
#*****************************************************************
# 3. Se tiene como posibles grupos sanguíneos de personas O, A, B y AB. Alguien con sangre tipo O sólo puede recibir sangre
# tipo O. Alguien de sangre A sólo puede recibir sangre de tipo A u O. Alguien de sangre tipo B sólo puede recibir sangre
# de tipo B u O. Alguien con sangre tipo AB puede recibir sangre de cualquier tipo. Se tienen las cantidades de bolsas de
# sangre disponibles (SA, SB, SAB, SO) y la cantidad de personas a tratar (PA, PB, PAB, PO). Implementar un algoritmo
# greedy que determine cómo se puede satisfacer la demanda de sangre (o si no puede hacerse). Indicar el orden del
# algoritmo y justificar por qué el algoritmo propuesto es un algoritmo greedy.

#El algoritmo es greedy porque siguiendo la regla entre las personas con menos posibilidades
#a mas posibilidades de sangre a recibir, vamos dando sangre y si sobra, le puede servir 
#al siguiente grupo y asi ver si se puede satisfacer la mayor cantidad posible.
#La complejidad del algoritmo es O(1) porque los llamados condicionales 
#respecto a las sangres y sus cantidades y las actualizaciones de las sangres

