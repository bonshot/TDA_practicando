monedas = [1, 6, 9]
cambio = dict()

def calcular_cambio(valor):
    cambio[0] = 0
    for i in range(1, valor + 1):
        menor = i
        for moneda in monedas:
            if moneda > i:
                continue
            cant = 1 + cambio[i - moneda]
            if cant < menor:
                menor = cant
        cambio[i] = menor
    return cambio[valor]

print(calcular_cambio(1))
print(calcular_cambio(6))
print(calcular_cambio(7))
print(calcular_cambio(9+9+9+9+6+6))
print(calcular_cambio(15))