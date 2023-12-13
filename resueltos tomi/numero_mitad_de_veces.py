def numero_mitad_de_veces(numeros):
    if len(numeros) == 1:
        return (numeros[0], 1)
    if len(numeros) == 2:
        if numeros[0] == numeros[1]:
            return (numeros[0], 2)
        return (None, None)

    mitad = int(len(numeros) / 2) 

    izq,cantidad_izq = numero_mitad_de_veces(numeros[0:mitad])
    der,cantidad_der = numero_mitad_de_veces(numeros[mitad : len(numeros)])

    if izq != None and izq == der:
        return izq

    if cantidad_der > len(numeros) // 2:
        return der
    
    if cantidad_der > len(numeros) // 2:
        return izq

    return (None, None)


print(numero_mitad_de_veces([1, 2, 3, 4, 1, 1, 1, 1]))
