"""
.. 1 ..
Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El
listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde
está ubicada cada una. Se desea ubicar la menor cantidad de patrullas policiales (en
las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a menos de
50 km.

Ejemplo:
    Ciudad      Bifurcación
    Castelli    185
    Gral Guido  249
    Lezama      156
    Maipú       270
    Sevigne     194

    Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero
    no Gral Guido y Maipú. Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral
    Guido. Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a
    todas las ciudades con distancia menor a 50km.

Proponer un algoritmo que lo resuelva. Justificar que la solución es óptima
"""
#lista = [("Castelli", 185), ("Gral Guido", 249), ("Lezama", 156), ("Maipú", 270), ("Sevigne", 194)]
def policias(lista):
    lista.sort(key=lambda x: x[1]) #(nlogn)
    patrullas_lista = []
    patrullas_lista.append(lista[0])
    for i in range(1, len(lista)):#(n)
        if lista[i][1] - patrullas_lista[-1][1] >= 50:
            patrullas_lista.append(lista[i])
    print(lista)
    return len(patrullas_lista)

#print(policias([("Castelli", 185), ("Gral Guido", 249), ("Lezama", 156), ("Maipú", 270), ("Sevigne", 207)]))
#El algoritmo tiene una complejidad de O(n), y el algoritmo es optimo porque recorre la lista y agrega patrulla
#de acuerdo si la ultima patrulla ubicada esta a mas de 50km que la nueva ubicacion. De esta manera, ubica las 
#patrullas lo mas lejos posible


# Los grupos sanguíneos de las personas son cuatro: A, B, O y AB. Los pacientes se clasifican según
# su grupo sanguíneo. Un paciente O sólo puede recibir sangre O, un paciente A sólo puede recibir
# sangre A u O, un paciente B sólo puede recibir sangre B u O, un paciente AB puede recibir cualquier
# grupo sanguíneo. Diseñar una estrategia greedy para resolver el siguiente problema: Sean Sa, Sb, So,
# Sab la sangre disponible de cada uno de los grupos y Pa, Pb, Po, Pab los pacientes de cada grupo que
# concurren al hospital para recibir una unidad de transfusión. Informar cómo se puede satisfacer la
# demanda de sangre de los pacientes (o si no se puede satisfacer). Justificar. 

def sangres(So,Sa,Sb,Sab,Po,Pa,Pb,Pab):
    #Sangre O
    if So > Po:
        So -= Po
        Po = 0
    else:
        Po -= So
        So = 0
    #Sangre A
    if Sa >= Pa:
        Sa -= Pa
        Pa = 0
    elif (Sa + So >= Pa):
        So -= (Pa - Sa)
        Sa = 0
        Pa = 0
    else:
        Pa -= Sa
        Pa -= So
        So = 0
        Sa = 0
    #Sangre B
    if Sb >= Pb:
        Sb -= Pb
        Pb = 0
    elif (Sb + So >= Pb):
        So -= (Pb - Sb)
        Sb = 0
        Pb = 0
    else:
        Pb -= Sb
        Pb -= So
        So = 0
        Sb = 0
    #Sangre AB
    if Sab >= Pab:
        Sab -= Pab
        Pab = 0
    elif (Sab + So >= Pab):
        So -= (Pab - Sab)
        Sab = 0
        Pab = 0
    elif (Sab + So + Sa >= Pab):
        Sa -= (Pab-Sab-So)
        Sab = 0
        So = 0
        Pab =0
    elif (Sab + So + Sa + Sb >= Pab):
        Sb -= (Pab-Sab-So-Sa)
        Sab = 0
        So = 0
        Pab =  0
        Sa = 0
    else:
        Pab -= Sab
        Pab -= So
        Pab -= Sa
        Pab -= Sb
        Sab = 0
        So = 0
        Sb =  0
        Sa = 0

    print(f"Sangre So: {So}, Sangre Sa: {Sa}, Sangre Sb: {Sb}, Sangre Sab: {Sab}")
    print(f"Pacientes O: {Po}, Pacientes A: {Pa}, Pacientes B: {Pb}, Pacientes AB, {Pab}")
    return Pab + Pb + Po + Pa == 0

#So,Sa,Sb,Sab,Po,Pa,Pb,Pab
#print(sangres(12,15,12,19,7,2,12,38))
#La complejidad del algoritmo es O(1), por realizar solamente comparaciones entre las sangres y los pacientes
#La idea para que se pueda dar sangre a la mayor cantidad de pacientes es hacerlo en el orden de menos a mas
#posibilidades de sangre, para satisfacer a la amyor cantidad posible, de esa manera el algoritmo seria optimo
#Es greedy porque agarra, para aquellos que tienen una disponibilidad reducida según lo que necesitan, toda la
#sangre disponible para ellos primero, y luego para los que tienen más de un tipo agota primero la de su tipo
#y si no se sació la totalidad agota la sangre alternativa, consumiendo así la primera sangre disponible para ese tipo


#EJERCICIO DE CATEDRA DE CLASE
#Problema de la carga de combustible
estaciones = [("Castelli", 55), ("Gral Guido", 50), ("Lezama", 121), ("Maipú", 150), ("Sevigne", 120)]
# estaciones = [("Gral Guido", 25),("Castelli", 50), ("Lezama", 80), ("Maipú", 110), ("Sevigne", 120)]
def camion_combustible(K, estaciones):
    estaciones.sort(key=lambda x: x[1])
    paradas = []
    combustible_actual = K
    paradas_evi = []
    estacion_actual = ("salida", 0)
    for i in range(len(estaciones)):
        if len(paradas) == 0:
            if estaciones[i][1] < K:
                estacion_actual = estaciones[i]
            elif estaciones[i][1] == K and estaciones[i] not in paradas:
                paradas.append(estaciones[i])
                estacion_actual = estaciones[i]
            else:
                paradas.append(estacion_actual)
        else:
            if estaciones[i][1] - paradas[-1][1] <= K:
                estacion_actual = estaciones[i]
            elif estaciones[i][1] - paradas[-1][1] > K and estacion_actual not in paradas:
                paradas.append(estacion_actual)
            
    return paradas
# print(camion_combustible(50, estaciones))

# EJERCICIO DE FINAL
#Las bolsas de un supermercado se cobran por separado y soportan hasta
# un peso maximo P, por encima del cual se rompen. Implementar
# un algoritmo greeedy que, teniendo una lista de pesos de n productos
# comprados, encuentre la mejor forma de distribuir los productos en
# la menor cantidad posible de bolsas. El algoritmo implementado encuentra siemre
# el optimo ? justificar

def bolsas(P, productos):
    bolsas = []
    bolsa_actual = []
    for producto in productos:
        if sum(bolsa_actual)+producto < P:
            bolsa_actual.append(producto)
        else:
            bolsas.append(bolsa_actual)
            bolsa_actual = [producto]
    bolsas.append(bolsa_actual)
    return bolsas
# print(bolsas(7, [3,3,2,2,2,2]))
#El algoritmo no es optimo, ya que para el ejemplo [3,3,2,2,2,2]
#podria armar [3,2,2] y [3,2,2] pero devuelve 3 bolsas
#El algoritmo es greedy porque no da la cantidad optima de bolsas siempre,
#Busca los productos optimos para ponerlos en la bolsa, asi hasta 
#guardar todas los productos en la menor cantidad de bolsas posibles

#La complejidad del algoritmos es O(n)


#Respuesta para el ejercicio de submarinos
#El algoritmo no es optimo, ya que habra situaciones
#donde un submarino sea iluminado por mas de 1 faro. Se podria
#ubicar necesariamente un faro por submarino pero ya dejaria
#de ser la minima cantidad de faros

#Problema de la mochila
#(valor, volumen)
#objetos =[(10,5), (1,7), (3,5), (8,3), (1,1), (20,15)]
[(8,3),(10,5),(20,15),(1,1),(3,5),(1,7)]
#[2,0.14,0.6,2.66,1,1.33]
#PESO =15
def mochila(W, objetos):
    objetos.sort(key=lambda x: x[0]/x[1],reverse=True)
    print(objetos)
    mochila = []
    valor = 0
    for i in objetos:
        if sum(mochila) + i[1] <= W:
            mochila.append(i[1])
            valor += i[0]
    return mochila, valor

print(mochila(15, [(10,5), (1,7), (3,5), (8,3), (1,1), (20,15)]))

#La complejidad es O(n) y el algoritmo no es optimo,
#Porque siempre va a haber una situacion donde el objeto con mayor
#valor no entre a la mochila porque otros elemenos con mejor promedio pero menor valor
#vayan antes que ese objeto

#**************************************************************

# Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
# Implementar un algoritmo que Greedy que dé la cantidad mínima de faros que se necesitan para que todos los
# submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las
# diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la complejidad
# del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima?

def submarinos_del_orto2(matriz):
    faros_totales = {}
    lista = []
    submarinos_cubiertos_totales = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != "s":
                submarinos_cubiertos = revisar_radio_2(matriz, i, j)
                if len(submarinos_cubiertos) != 0:
                    faros_totales[(i,j)] = submarinos_cubiertos
                    
    for faro, submarinos in faros_totales.items():
        lista.append((faro, submarinos))
    lista.sort(key=lambda x: len(x[1]), reverse=True)
    
    # consigo la cantidad minima de faros que cubran todos los submarinos
    faros = 0
    faros_ubicados = []
    for faro in lista:
        if revisar_submarino_cubierto(submarinos_cubiertos_totales, faro[1]):
            for submarino in faro[1]:
                if submarino not in submarinos_cubiertos_totales:
                    submarinos_cubiertos_totales.append(submarino)
            faros +=1
            faros_ubicados.append(faro[0])

    print(faros_ubicados)
    print(faros)   

def revisar_submarino_cubierto(submarinos_cubiertos, submarinos_por_ver):
    for submarino in submarinos_por_ver:
        if submarino not in submarinos_cubiertos:
            return True
    return False

def revisar_radio_2(matriz, i, j):
    submarinos = []
    min_x, max_x = max(i - 2, 0), min(i + 2, len(matriz) - 1)
    min_y, max_y = max(j - 2, 0), min(j + 2, len(matriz[0]) - 1)
    for k in range(min_x, max_x +1):
        for l in range(min_y, max_y+1):
            if matriz[k][l] == "s":
                submarinos.append((k, l))
    return submarinos


# La solución propuesta es greedy porque a medida que recorre la matriz verifica que la posición cubra la mayor cantidad de faros posibles,
# pero no examina todas las posibilidades sino que se queda con la primera que encuentra.
# El algoritmo no es optimo porque habra situaciones que un faro cubre la mayor cantidad de submarinos pero por elegir esa posición puede estar perdiendose de
# cubrir a múltiples otros submarinos con menos faros, por esto es que el algoritmo al ser greedy y quedarse con la primera posición que encuentra no 
# es óptimo 