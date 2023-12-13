class Grafo:
    def __init__(self, nodos, aristas):
        self.nodos = set(nodos)
        self.adyacencias = dict()
        for arista in aristas:
            s = arista[0]
            d = arista[1]

            w = 1
            if len(arista) == 3:
                w = arista[2]

            if not s in nodos:
                raise Exception(f"{s} no es un nodo del grafo")
            if not d in nodos:
                raise Exception(f"{d} no es un nodo del grafo")
            if self.adyacencias.get(s) == None:
                self.adyacencias[s] = set()

            self.adyacencias[s].add((d, w))

    def aristas(self):
        resultado_ariastas = []
        for s, aristas in self.adyacencias.items():
            for d, w in aristas:
                resultado_ariastas.append((s, d, w))
        return resultado_ariastas

    def adyacentes(self, nodo):
        return self.adyacencias.get(nodo) or set()

    def hay_arista(self, s, d):
        ady = self.adyacentes(s)
        for a in ady:
            if a[1] == d:
                if len(a) == 3:
                    return a[2]
                return 1
        return 0

    def agregar_arista(self, s, d, w=1):
        adyacentes = self.adyacencias.get(nodo)

        if not adyacentes:
            adyacentes = set()
            self.adyacencias[s] = adyacentes

        for a in adyacentes:
            if a[1] == d:
                aw = 1
                if len(a) == 3:
                    aw = a[2]
                aw += w
                adyacentes.remove(a)
                if aw != 0:
                    adyacentes.add((s, d, aw))
                return aw
        adyacentes.add((s, d, w))
        return w

    def eliminar_arista(self, s, d):
        peso = self.hay_arista(s, d)
        self.agregar_arista(s, d, -peso)
        return peso
