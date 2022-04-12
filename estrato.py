class Estrato():
    pe   = float #peso especifico del material
    af   = float #angulo de friccion del material
    C    = float #cohesion
    H    = float #altura del estrato 
    

    def __init__(self):
        self.pe   = 0
        self.af   = 0
        self.C    = 0
        self.H    = 0

    def EnterData(self):
        self.pe   = input("ingrese Peso específico: ")
        self.af   = input("ingrese Angulo de fricción: ")
        self.C    = input("ingrese Cohesión: ")
        self.H    = input("ingrese Altura del estrato: ")


