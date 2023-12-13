#implementar un algoritmo que en O(n log n), dado un arreglo de tamaño n números enteros devuelva true o false si algun 
#número se repite más de la mitad de las veces

def mas_de_la_mitad(numeros):
    if _mas_de_la_mitad(numeros):
        return True
    return False


def _mas_de_la_mitad(numeros):
    largo = len(numeros) -1
    print("MIRA LO LARGO QUE LA TENGO", largo)
    if largo == 0:
        return numeros[0]
    #caso base
    mitad = largo//2
    print("SOY LA MITAD", mitad)
    candidato_izquierda = _mas_de_la_mitad(numeros[0:mitad+1])
    print("SOY MASSA", candidato_izquierda)
    candidato_derecha = _mas_de_la_mitad(numeros[mitad+1:])
    print("SOY MILEI", candidato_derecha)
    cant_izquierda = 0
    cant_derecha = 0

    for i in range(largo):
        if numeros[i] == candidato_izquierda:
            cant_izquierda+=1
        if numeros [i] == candidato_derecha:
            cant_derecha+=1
    if cant_izquierda > mitad:
        return candidato_izquierda
    if cant_derecha > mitad:
        return candidato_derecha



lista_1 = [4,2,4,3,4,4,4,6,6,6,4,2,4,4]
resultado = mas_de_la_mitad(lista_1)
print(resultado)

