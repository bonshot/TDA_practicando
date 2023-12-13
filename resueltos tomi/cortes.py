cortes = dict()


def calcular_cortes(n):
    if cortes.get(n) != None:
        return cortes[n]

    m = 0
    for i in range(1, n):
        valor = i * calcular_cortes(n - i)
        if valor > m:
            m = valor
    
    if n > m:
        m = n
    
    cortes[n] = m

    return m

print(calcular_cortes(10))
print(calcular_cortes(11))