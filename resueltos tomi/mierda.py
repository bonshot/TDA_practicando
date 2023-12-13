class Mierda:
    def __init__(self, caca = 1):
        self.caca = caca
    
    def cagar(self):
        return "💩" * self.caca

mierda = Mierda(3)

print(mierda.cagar())
