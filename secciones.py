from numpy import pi, sqrt, nan
from numpy.random import rand
from constantes import g_, ρ_acero, mm_
import pandas as pd
 
class Circular(object):
    """define una seccion Circular"""

    def __init__(self, D, Dint, color=rand(3)):
        super(Circular, self).__init__()
        self.D = D
        self.Dint = Dint
        self.color = color  #color para la seccion

    def area(self):
        return pi*(self.D**2 - self.Dint**2)/4

    def peso(self):
        return self.area()*ρ_acero*g_

    def inercia_xx(self):
        return pi*(self.D**4 - self.Dint**4)/4

    def inercia_yy(self):
        return self.inercia_xx()

    def nombre(self):
        return f"O{self.D*1e3:.0f}x{self.Dint*1e3:.0f}"

    def __str__(self):
        return f"Seccion Circular {self.nombre()}"

        
#Mas adelante, no es para P1E1

class SeccionICHA(object):
    """Lee la tabla ICHA y genera una seccion apropiada"""

    def __init__(self, denominacion, base_datos="Perfiles ICHA.xlsx", debug=False, color=rand(3)):
        super(SeccionICHA, self).__init__()
        self.denominacion = denominacion
        self.color = color  #color para la seccion
        
        tipo=self.denominacion.split("x")
        if tipo[0][0] == "H":
            if tipo[0][1].isdigit():    
                self.perfil="H"
                planilla="H"
                i=1
                d=""
                while i<len(tipo[0]):
                    d+=str(tipo[0][i])
                    i+=1
                    
                bf=tipo[1]
                peso=tipo[2]
            
            if tipo[0][1]=="R":
                self.perfil="HR"
                planilla="HR"
                i=2
                d=""
                while i<len(tipo[0]):
                    d+=str(tipo[0][i])
                    i+=1
                
                bf=tipo[1]
                peso=tipo[2]
                
        if tipo[0][0]=="P":
            self.perfil="PH"
            planilla="PH"
            i=2
            d=""
            while i<len(tipo[0]):
                d+=str(tipo[0][i])
                i+=1
                
            bf=tipo[1]
            peso=tipo[2]

        if tipo[0][0]=="[":
            self.perfil="[]"
            planilla="Cajon"
            i=2
            d=""
            while i<len(tipo[0]):
                d+=str(tipo[0][i])
                i+=1
                
            B=tipo[1]
            peso=tipo[2]
            
        if tipo[0][0]=="O":
            self.perfil="O"
            planilla="Circulares Mayores"
            i=1
            d=""
            while i<len(tipo[0]):
                d+=str(tipo[0][i])
                i+=1
                
            Dint=tipo[1]

        if tipo[0][0]=="o":
            self.perfil="o"
            planilla="Circulares Menores"
            i=1
            d=""
            while i<len(tipo[0]):
                d+=str(tipo[0][i])
                i+=1
            
            Dint=tipo[1]
            
        if tipo[0][0]=="W":
            self.perfil="W"
            plantilla="HR"
            i=1
            d=""
            while i<len(tipo[0]):
                d+=str(tipo[0][i])
                i+1
            
            bf=tipo[1]
            peso=tipo[2]
        
        self.datos=pd.read_excel(base_datos, sheet_name=planilla, header=11)
        tndr=False
        
        if self.perfil=="H" or self.perfil=="PH" or self.perfil=="W" or self.perfil=="HR":
            sec=[self.perfil,d,"x",bf,"x",peso]  
        if self.perfil=="o" or self.perfil=="O":
            sec=[self.perfil,d,"x",Dint]
        if self.perfil=="[]":
            sec=[self.perfil,d,"x",B,"x",peso]        
            
        if self.perfil=="H" or self.perfil=="PH":
            d1=self.datos["d"].tolist()
            bf1=self.datos["bf"].tolist()
            pes=self.datos["peso"].tolist()
            i=0
            while i<len(d1):
                if (d1[i])==float(sec[1]):
                    if (bf1[i])==float(sec[3]):
                        if (pes[i])==float(sec[5]):
                            tndr=True
                            break
                        else:
                            i+=1
                    else:
                        i+=1
                else:
                    i+=1
            self.i=i
            
        if self.perfil=="HR" or self.perfil=="W":
            d1=self.datos["d"].tolist()
            bf1=self.datos["bf"].tolist()
            pes=self.datos["peso"].tolist()
            i=0
            while i<len(d1):
                if (d1[i])==float(sec[1]):
                    if (bf1[i])==float(sec[3]):
                        if (pes[i])==float(sec[5]):
                            tndr=True
                            break
                        else:
                            i+=1
                    else:
                        i+=1
                else:
                    i+=1
            self.i=i
        
        if self.perfil=="O" or self.perfil=="o":
            d1=self.datos["d"].tolist()
            Dint1=self.datos["Dint"].tolist()
            i=0
            while i<len(d1):
                if d1[i]==float(sec[1]):
                    if Dint1[i]==float(sec[3]):
                        tndr=True
                        break
                    else:
                        i+=1
                else:
                    i+=1
            self.i=i
        
        if self.perfil=="[]":
            D1=self.datos["D"].tolist()
            B1=self.datos["B"].tolist()
            pes=self.datos["peso"].tolist()
            i=0
            while i<len(D1):
                if D1[i]==float(sec[1]):
                    if B1[i]==float(sec[3]):
                        if pes[i]==float(sec[5]):
                            tndr=True
                            break
                        else:
                            i+=1
                    else:
                        i+=1
                else:
                    i+=1
            self.i=i
        
        self.sec=sec
        self.tndr=tndr
        
    def area(self):
        if self.tndr==True:
            DF=self.datos["A"].tolist()
            A = DF[self.i]/10**6
        if self.tndr==False:
            A="nan"
            
        self.A=A
        return str(self.A)
    
    def peso(self):
        if self.tndr==True:
            DF=self.datos["peso"].tolist()
            P = DF[self.i]
        if self.tndr==False:
            P="nan"

        self.P=P
        return str(self.P)

    def inercia_xx(self):
        if self.perfil=="o" or self.perfil=="O":
            if self.tndr==True:
                DF=self.datos["I/10⁶"].tolist()
                Ixx = DF[self.i]
            if self.tndr==False:
                Ixx="nan"
        else:
            if self.tndr==True:
                DF=self.datos["Ix/10⁶"].tolist()
                Ixx = DF[self.i]
            if self.tndr==False:
                Ixx="nan"
            
        self.Ixx=Ixx
        
        return str(self.Ixx)

    def inercia_yy(self):
        if self.perfil=="o" or self.perfil=="O":
            pass
        
        else:
            if self.tndr==True:
                DF=self.datos["Iy/10⁶"].tolist()
                Iyy = DF[self.i]
            if self.tndr==False:
                Iyy="nan"
        
        self.Iyy=Iyy
        return str(self.Iyy)

    def nombre(self):
        return self.denominacion

    def __str__(self):
        if self.perfil=="o" or self.perfil=="O":
            if self.area()=="nan" or self.peso()=="nan" or self.inercia_xx()=="nan":
                s=f"Tipo de seccion {self.denominacion} no encontrada en base de datos \n"
            
            if self.area()!="nan" and self.peso()!="nan" and self.inercia_xx()!="nan":
                s=f"{self.denominacion} encontrada. A={self.area()} I={self.inercia_xx()} \n"
                
            s+=f"Seccion ICHA {self.denominacion} \n"
            s+=f"\t Area: {self.area()} \n"
            s+=f"\t Peso: {self.peso()} \n"
            s+=f"\t I: {self.inercia_xx()} \n"
        
        
        else:
            if self.area()=="nan" or self.peso()=="nan" or self.inercia_xx()=="nan" or self.inercia_yy()=="nan":
                s=f"Tipo de seccion {self.denominacion} no encontrada en base de datos \n"

            if self.area()!="nan" and self.peso()!="nan" and self.inercia_xx()!="nan" and self.inercia_yy()!="nan":
                s=f"{self.denominacion} encontrada. A={self.area()} Ix={self.inercia_xx()} Iy={self.inercia_yy()} \n"
            
            s+=f"Seccion ICHA {self.denominacion} \n"
            s+=f"\t Area: {self.area()} \n"
            s+=f"\t Peso: {self.peso()} \n"
            s+=f"\t Ixx: {self.inercia_xx()} \n"
            s+=f"\t Iyy: {self.inercia_yy()} \n"
        
        return s
