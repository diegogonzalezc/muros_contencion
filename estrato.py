class Estrato():
    pe   = float #peso especifico del material
    af   = float #angulo de friccion del material
    C    = float #cohesion
    H    = float #altura del estrato
    pa  =float #peso específico del agua

    

    def __init__(self):
        self.pe   = 0
        self.af   = 0
        self.C    = 0
        self.H    = 0
        self.nf   = 0
        self.pa   = 0

    def EnterData(self):
        self.pe   = float(input("ingrese Peso específico: "))
        self.af   = float(input("ingrese Angulo de fricción: "))
        self.C    = float(input("ingrese Cohesión: "))
        self.H    = float(input("ingrese Altura del estrato: "))
        self.pa   = float(input("ingrese Peso despecífico del agua si en este estrato hay presencia NF: "))
        print("-------------------------------")


