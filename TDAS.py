class Grafo:
    def __init__(self, dirigido = False):
        self.dirigido = dirigido
        self._vertices = set()
        self.adyacencias = dict()

    def vertices(self):
        return list(self._vertices)

    def agregar_vertice(self, vertice):
        self._vertices.add(vertice)
        self.adyacencias[vertice] = self.adyacencias.get(vertice, set())

    def unir(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        self.adyacencias[origen].add(destino)
        if not self.dirigido:
            self.adyacencias[destino].add(origen)

    def hay_arista(self, origen, destino):
        return destino in self.adyacencias[origen]

    def adyacentes(self, origen):
        return self.adyacencias[origen]
    
    def __iter__(self):
        return self._vertices.__iter__()