from estrato import Estrato
import numpy as np 

num_estratos=int(input("ingrese el numero de estratos: "))
if __name__ == "__main__":

    esf_efec=[]
    esf_tot=[]
    list_ka=[]
    htot_list=[]
    f_list=[]
    htot=0
    count=0
    ftot=0
    zres=0

    for i in range(num_estratos):
        est=Estrato()
        est.EnterData()
        ka=np.tan(np.deg2rad(45-(est.af)/2))**2
        
        if len(esf_tot) != 0:
            se=est.pe*est.H + esf_efec[(count-1)]
        else:
            se=est.pe*est.H

        sa=ka*se - 2*(est.C)*(ka)**0.5
        su=est.pa*est.H
        st=sa+su
        esf_efec.append(se)
        esf_tot.append(st)
        list_ka.append(ka)
        htot=htot+est.H
        htot_list.append(htot)

        if len(esf_tot) > 1:
            sa0=(ka*esf_efec[(count-1)] - 2*(est.C)*(ka)**0.5)
            f1=sa0*est.H 
            f2=1/2*(st-sa0)*est.H
            f=f1+f2
            ftot=ftot+f
            zres=zres+f1*(htot-(est.H)/2)+f2*(htot-(est.H)+2/3*(est.H))
        else:
            ftot=1/2*st*est.H
            zres=ftot*(est.H)*(2/3)
            
        




        count=+1


    print(esf_efec,esf_tot,(zres/ftot))
    


