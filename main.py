from estrato import Estrato
import numpy as np 

num_estratos=input("ingrese el numero de estratos: ")
if __name__ == "__main__":

    al=[]

    for i in range(num_estratos):
        a=Estrato()
        a.EnterData()
        ka=np.sin(np.deg2rad(45-a.af))
        al.append(a)

    print(al[0].pe)
    

