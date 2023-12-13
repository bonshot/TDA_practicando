# SAT y 3-SAT
# El problema de SAT se basa en dar todas las soluciones a una expresion
# booleana descripta por la union de clausulas.
# Cada clasula se compone de la siguiente forma:
# C1 = X1 ∨ X2 ∨ ¬X3 ∨ ... ∨ Xn
# y la union serıa S = C1 ∧ C2 ∧ C3 ∧ ... ∧ Ck
# 3-SAT es el problema en el cual cada clasula tiene 3 literales solamente.
# (C1 = X1 ∨ X2 ∨ X3)

def is_satisfiable_assignment(formula, assignment):
    # Evalúa la fórmula booleana con la asignación dada
    for clause in formula:
        clause_eval = any(literal in assignment for literal in clause)
        if not clause_eval:
            return False
    return True

def brute_force_sat(formula, variables):
    # Genera todas las asignaciones posibles de valores de verdad
    all_assignments = product([False, True], repeat=len(variables))

    # Verifica cada asignación y devuelve la primera que satisface la fórmula
    for assignment in all_assignments:
        assignment_dict = dict(zip(variables, assignment))
        if is_satisfiable_assignment(formula, assignment_dict):
            return assignment_dict
    return None

# Dado un grafo no dirigido G y un entero positivo k, se busca determinar
# si existe un conjunto de k vertices en G tal que todos los vertices en ese
# conjunto esten conectados entre sı por una arista (es decir, si existe un
# subgrafo completo de tama˜no k vertices).

def is_clique(graph, nodes):
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[i] not in graph[nodes[j]]:
                return False
    return True

def find_clique(graph, current_clique, remaining_nodes, k):
    if len(current_clique) == k:
        if is_clique(graph, current_clique):
            return current_clique
        return None

    max_clique = []
    for node in list(remaining_nodes):
        new_clique = current_clique + [node]
        new_remaining = [n for n in remaining_nodes if n in graph[node]]
        result = find_clique(graph, new_clique, new_remaining, k)
        if result and len(result) > len(max_clique):
            max_clique = result

    return max_clique

def find_k_clique(graph, k):
    max_clique = []

    nodes = list(graph.keys())

    for start_node in nodes:
        result_clique = find_clique(graph, [start_node], nodes, k)
        if result_clique and len(result_clique) > len(max_clique):
            max_clique = result_clique

    return max_clique