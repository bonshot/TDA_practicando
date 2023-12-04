#Problema de scheduling 1
# Tengo un aula donde quiero dar charlas, que cada una tiene un horario
# de inicio y un horario de fin. Quiero dar la mayor cantidad de charlas
def problema_scheduling1(horarios):
    horarios.sort(key=lambda x: x[1])
    orden = []
    for horario in horarios:
        if len(orden) == 0 or not hay_intersection(orden[-1], horario):
            orden.append(horario)
    return orden

def hay_intersection(anterior, actual):
    if anterior[1] >= actual[0]:
        return True
    return False
    
# print(problema_scheduling1([(1,3), (4,8), (2,6), (7,15)]))
#La complejidad del algoritmo es O(n) por recorrer todos los horarios 
#de las clases
#Es greedy porque sigue una regla de a poco que es ver clase por clase
#e ir agregando a la lista siempre y cuando no haya interesction con
#el anterior hasta obtener la solucion final que es conseguir todas las clases
#a dar
#el algoritmo no es optimo ya que puede dar se la situacion que 
#tengamos clases que no podamos dar por intersecion con las anteriores pero
#podriamos cubrir mayor tiempo del dia
#por ej = [(1,3), (4,8), (2,6), (7,15)], donde nosotros solamente 
#agarrariamos la clase de (1,3) y de (4,8) pero las clases de (2,6) y y (7,15)
#cubren mas el dia. Todo depende de los horarios de las clases

#*************************************************************

#Problema del cambio
# Se tiene un sistema de monetario. Se quiere dar cambio de una deter-
# minada cantidad de plata. Implementar un algoritmo que devuelva el
# cambio pedido, usando la m ́ınima cantidad de monedas/billetes.
def problema_de_cambio(sistema, plata):
    sistema.sort(reverse=True)
    cant = {}
    for billete in sistema:
        if plata >= billete:
            cantidad = plata // billete
            cant[billete] = cantidad
            plata %= billete
    return cant
# print(problema_de_cambio([50,15,2,1,32], 182))
#El algoritmo es greedy porque mira en orden de mayor a menor el sistema
#monetario, va viendo por cada billete cuando puede aportar ese billete
#hasta obtener en el diccionario, el total de billetes, la menor
#cantidad posible 
#La complejidad del algoritmo es o(n), por recorre todo el sistema monetario
#e ir viendo por cada billete
#El algoritmo depende de que tan malo sea el sistema, porque llegado el caso el 
#el sistema monetario es muy malo, devolveria una gran cantidad de billete

#*************************************************************

# #Problema de la carga de combustible
# Un cami ́on debe viajar desde una ciudad a otra deteni ́endose a cargar
# combustible cuando sea necesario. El tanque de combustible le permite
# viajar hasta K kil ́ometros. Las estaciones se encuentran 
# distribuidas a lolargo de la ruta siendo di la distancia desde la 
# estacion i-1 a la estaci ́oni.
# Implementar un algoritmo que decida en qu ́e estaciones debe cargar com-
# bustible de manera que se detenga la menor cantidad de veces posible
def problema_combustible(paradas, K):
    n = len(paradas)
    combustible_actual = K
    ultima_parada = 0
    estaciones = []
    for i in range(n):
        distancia_restante = paradas[i] - ultima_parada
        if distancia_restante > combustible_actual:
            estaciones.append(ultima_parada)
            combustible_actual = K
        ultima_parada = paradas[i]
        combustible_actual -= distancia_restante
    return estaciones
# print(problema_combustible([25,50,80,120,155], 75))
#Este algoritmo es greedy porque mira de a cada parada y va guardando si puede evitar parada o 
#parar en esa hasta obtener el total de paradas minimias, de acuerdo a su capacidad de tanque
#La complejidad del algoritmo es O(n)
#El algoritmo no es optimo porque depende de las distancias de las paradas que puede ser el caso que pare
#menos de lo esperado y no pueda llegar mas lejos

#*************************************************************

# Problema de la mochila
# Tenemos una mochila con una capacidad W (peso, volumen). Hay ele-
# mentos a guardar. Cada elemento tiene un peso y un valor. Queremos
# maximizar el valor de lo que nos llevamos sin pasarnos de la capacidad
def problema_mochila(productos, W):
    productos.sort(key=lambda x: x[0]/x[1], reverse=True)
    mochila = []
    peso = 0
    valor = 0
    for producto in productos:
        if peso + producto[1] <= W:
            mochila.append(producto)
            peso += producto[1]
            valor += producto[0]
    return mochila, peso, valor
print(problema_mochila([(5,2), (3,3), (7,6), (1,5), (4,1)], 12))
#El algoritmo es greedy porque siguiendo la regla de tener los productos ordenados por valor/peso de mayor
#a menor, vamos agregando la mochila siempre y cuando entre y vamos guardando el valor de la mochila
#hasta devolver la mochila total, con su peso y con su valor, aprovechando lo maximo posible
#El algoritmo es o(n) por recorrer cada producto de los productos y resolver el problema propuesto
#El algoritmo no es optimo del todo porque puede haber productos con mejor valor pero con un peso altisimo
#que no entraria en la mochila y obtendriamos una mochila con un valor muy bajo

#*************************************************************

#Problema de compra con inflacion
# Tenemos n productos en un arreglo R, donde R[i] representa el precio
# del producto i. Cada d ́ıa debemos comprar un solo pr ́oducto, y cada dia
# aumentan los precios. El precio del producto i el dia j es R[i]j+1 
# (con j comenzando en 0).
# Implementar un algoritmo que nos indique el precio m ́ınimo al que pode-
# mos comprar todos los productos
def precio_minimo_compra(productos):
    if not productos or not productos[0]:
        return None  # No hay productos o días

    num_dias = len(productos[0])
    precio_minimo_global = 0  # Inicializar con un valor infinito

    for dia in range(num_dias):
        precio_minimo_dia = max(producto[dia] for producto in productos)
        print(precio_minimo_dia)
        # Actualizar el precio mínimo global si encontramos uno más bajo en el día actual
        if precio_minimo_dia > precio_minimo_global:
            precio_minimo_global = precio_minimo_dia

    return precio_minimo_global

# Ejemplo de uso
productos = [
    [10, 15, 20],  # Precios del producto 1 para los días 0, 1, 2
    [12, 18, 24],  # Precios del producto 2 para los días 0, 1, 2
    [8, 16, 32]    # Precios del producto 3 para los días 0, 1, 2
]

print(precio_minimo_compra(productos))
#el algoritmo es greedy porque va mirando el precio maximo de cada producto, para saber cual es el minimo
#precio que tiene que poner para comprar todos los productos, sabiendo que va a comprar todo
#Es o(n)
#No es optimo porque dependiendo del sistema inflatorio del pais, los precios para el dia siguiente pueden subir 
#mas rapido y no podriamos conseguir comprar todo con el precio minimo global 

#*************************************************************

#Problema de scheduling 2
# Ahora tenemos tareas con una duraci ́on y un deadline, pero pueden
# hacerse en cualquier momento, siempre que se hagan antes del deadline.
# Para este problema, buscamos minimizar la latencia en el que las tareas
# se ejecuten. Es decir, si definimos que una tarea i empieza en si, entonces
# termina en fi = si + ti, y su latencia es li = fi −di (si fi > di, sino 0).

#*************************************************************

#Problema de scheduling 3
# Contamos con un conjunto de n actividades. Cada actividad x tiene una
# fecha de inicio ix y una fecha de finalizaci ́on fx. Adem ́as contamos con
# un n ́umero r de recursos donde se pueden llevar a cabo estas actividades.
# Determinar si es posible cumplir con todas las actividades utilizando la
# menor cantidad de recursos posibles. Adem ́as, dar una programaci ́on
# posible para llevarlas a cabo.

#*************************************************************

# Problema del Cache
# # Podemos tener hasta k elementos de memoria bien a mano, el resto
# tendrıamos que ir a RAM. Hay que decidir que guardamos en la memoria
# cache.
# Tenemos un conjunto de datos U en memoria general (n en total), una
# memoria cache de k < n elementos. Tenemos una secuencia de pedidos
# de datos di. Si di esta en la cache, accedemos muy r apido. 
# Si no esta
# → cache miss + ahora la tenemos que traer a la cache (y si la cache
# est ́a llena, tenemos que evictear un dato previo). Queremos minimizar
# la cantidad de cache misses