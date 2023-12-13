monedas = [1,6,9]
menor_moneda = min(monedas)

cambio = dict()

def calcular_cambio(valor):
    "Calcula la cantidad mínima de monedas necesarias para hacer el cambio de un valor"

    if valor == 0:
        return 0

    if valor == menor_moneda:
        return 1

    if valor in cambio:
        return cambio[valor]

    if valor < menor_moneda:
        return None

    menor = None
    for moneda in monedas:
        c = calcular_cambio(valor - moneda)
        if c == None:
            continue
        nuevo = 1 + c

        if not menor or nuevo < menor:
            menor = nuevo
    cambio[valor] = menor
    return menor


print(calcular_cambio(1))
print(calcular_cambio(6))
print(calcular_cambio(7))
print(calcular_cambio(9+9+9+9+6+6))
print(calcular_cambio(15))