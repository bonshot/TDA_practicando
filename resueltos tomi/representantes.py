#Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más
#clubes, y de exactamente 1 partido político. Cada grupo de interés debe nombrar a un representante ante la nueva
#comisión de actividades culturales, con las siguientes restricciones: cada partido político no puede tener más de N/2
#simpatizantes en la comisión, cada persona puede representar a solo un club, cada club debe estar representado por
#un miembro. Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a
#qué partido pertenecen), nos dé una lista de representantes válidos. Indicar y justificar la complejidad del algoritmo
#implementado.

def representantes(dic_clubes, dic_partidos, cant_personas): #clubes club: personas, partidos partido: personas
    grafo = Grafo
    grafo.agregar_vertice("S")
    grafo.agregar_vertice("T")
    for key in dic_clubes.keys():
        grafo.agregar_vertice(key)
        grafo.agregar_arista_con_direccion("S", key, 1)
        for persona in dic_clubes[key]:
            if not grafo.vertice_pertenece(persona):
                grafo.agregar_vertice(persona)
            grafo.agregar_arista_con_direccion(key, persona, 1)
    for key in dic_partidos.keys():
        grafo.agregar_vertice(key)
        grafo.agregar_arista_con_direccion(key, "T", cant_personas//2)
        for persona in dic_partidos[key]:
            if not grafo.vertice_pertenece(persona): #persona que participe en 0 clubes
                grafo.agregar_vertice(persona)
            grafo.agregar_arista_con_direccion(persona, key, 1)
    flujo = grafo.ford_fulkerson("S", "T")
    participantes = []
    for arista in flujo.keys():
        if arista.origen in dic_partidos.values():
            participantes.append(arista.origen)
    return participantes        

#armar el grafo es O(V + E)
#ford fulkerson es O(V * E^2)
#la complejidad final es O(V + E + V * E^2) = O(V * E^2)