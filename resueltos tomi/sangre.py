#Se tiene como posibles grupos sanguíneos de personas O, A, B y AB. Alguien con sangre tipo O sólo puede recibir sangre
#tipo O. Alguien de sangre A sólo puede recibir sangre de tipo A u O. Alguien de sangre tipo B sólo puede recibir sangre
#de tipo B u O. Alguien con sangre tipo AB puede recibir sangre de cualquier tipo. Se tienen las cantidades de bolsas de
#sangre disponibles (SA, SB, SAB, SO) y la cantidad de personas a tratar (PA, PB, PAB, PO). Implementar un algoritmo
#greedy que determine cómo se puede satisfacer la demanda de sangre (o si no puede hacerse). Indicar el orden del
#algoritmo y justificar por qué el algoritmo propuesto es un algoritmo greedy.


def repartir_sangre(disponible, necesitada):
    disponible_actual = disponible
    repartis = [0,0,0,0]
    if disponible_actual[3] < necesitada[3]:
        print("NO ALCANZA 0")
        return False 
    repartis[3] = necesitada[3]
    disponible_actual[3] -=repartis[3]

    if disponible_actual[0] < necesitada[0]:
        falta = necesitada[0] - disponible_actual[0]
        repartis[0] = disponible_actual[0]
        disponible_actual[0] = 0
        if disponible_actual[3] < falta:
            return False
            print("NO ALCANZA A  ni 0")
        repartis[3] += falta
        disponible_actual[3] -=falta

    else:
        repartis[0] = necesitada[0]
        disponible_actual[0] -= repartis[0]
        print("dispongo de a", disponible_actual[0])

    if disponible_actual[1] < necesitada[1]:
        falta = necesitada[1] - disponible_actual[1]
        repartis[1] = disponible_actual[1]
        disponible_actual[1] = 0
        if disponible_actual[3] < falta:
            print("NO ALCANZA B y 0")
            return False
        repartis[3] += falta
        disponible_actual[3] -=falta

    else:
        repartis[1] = necesitada[1]
        disponible_actual[1] -= repartis[1]  

    
    if disponible_actual[2] < necesitada[2]:
        falta = necesitada[2] - disponible_actual[2]
        repartis[2] = disponible_actual[2]
        disponible_actual[2] = 0
        for i in range(4):
            if disponible_actual[i] > 0:
                if disponible_actual[i] > falta:
                    repartis[i] +=falta
                    disponible_actual[i] -= falta
                    break
                else:
                    repartis[i] += disponible_actual[i]
                    falta -= disponible_actual[i]
                    disponible_actual[i] = 0
    

    reparto = 0
    for i in range(4):
        reparto += repartis[i]
    necesito = 0
    for i in range(4):
        necesito += necesitada[i]
    
    if reparto < necesito:
        return False
    return repartis

sangre = [3,4,2,10]
necesito = [2,1,4,5]

print(repartir_sangre(sangre, necesito))