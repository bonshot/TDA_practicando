def bolsas_supermercado(p, pesos):
    pesos_disponibles_bolsas = [p]
    bolsas_elementos = [[]]

    pesos_restantes_a_embolsar = list(pesos)

    while len(pesos_restantes_a_embolsar) > 0:
        se_agrego_peso = False
        for i in range(len(pesos_restantes_a_embolsar)):
            peso = pesos_restantes_a_embolsar[i]
            bolsa = len(pesos_disponibles_bolsas) - 1

            if pesos_disponibles_bolsas[bolsa] >= peso:
                pesos_disponibles_bolsas[bolsa] -= peso
                bolsas_elementos[bolsa].append(peso)
                se_agrego_peso = True
                pesos_restantes_a_embolsar.pop(i)
                break
        if not se_agrego_peso:
            pesos_disponibles_bolsas.append(p)
            bolsas_elementos.append([])

    return bolsas_elementos
    

    
print(bolsas_supermercado(5, [4, 2, 1, 3, 5]))

# Paso 1. bolsas: [ 4 ]
# Paso 2. bolsas: [ 4, 1 ]
# Paso 3. bolsas: [ 4, 1 ], [ 2 ]
# Paso 4. bolsas: [ 4, 1 ], [ 2, 3 ]
# Paso 5. bolsas: [ 4, 1 ], [ 2, 3 ], [ 5 ]

# Ejemplo no óptimo:
# p: 5, pesos: [ 3, 1, 2, 4 ]
# Solución greedy: [ 3, 1 ], [ 4 ], [ 2 ]
# Solución óptima: [ 4, 1 ], [ 3, 2 ]

# Reducción: aplicar subset sum, sacar esos elementos y ponerlos en una bolsa
# con el resultado voler a aplicar subset sum y asi y asi