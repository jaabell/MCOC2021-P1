from numpy import pi, sqrt, nan
from numpy.random import rand
from constantes import g_, ρ_acero, mm_
import pandas as pd
import string
 
 
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
    # perfil = input("Ingresar perfil tipo: H, PH, HR, CAJON (C), CIRCULARES_MAYORES (CMA), CIRCULARES_MENORES (CME)  =" )     

    def __init__(self, denominacion, base_datos="Perfiles ICHA.xlsx", debug=False, color=rand(3)):
        super(SeccionICHA, self).__init__()
        self.denominacion = denominacion
        self.color = color  #color para la seccion
        
        perfil_tipo = self.denominacion.split('x')
        
        if perfil_tipo[0][0] == "H":
            if perfil_tipo[0][1]!="R":    
                self.seccion="H"
                ventana="H"
                self.d = str(perfil_tipo[0][1:len(perfil_tipo[0])])
                self.bf=perfil_tipo[1]
                self.peso=perfil_tipo[2]
            
            elif perfil_tipo[0][1]=="R":
                self.seccion="HR"
                ventana="HR"
                self.d = str(perfil_tipo[0][2:len(perfil_tipo[0])])
                self.bf=perfil_tipo[1]
                self.peso=perfil_tipo[2]
                
        if perfil_tipo[0][0]=="P":
            self.seccion="PH"
            ventana="PH"
            self.d = str(perfil_tipo[0][2:len(perfil_tipo[0])])
            self.bf=perfil_tipo[1]
            self.peso=perfil_tipo[2]

        if perfil_tipo[0][0]=="[":
            self.seccion="[]"
            ventana="Cajon"
            self.D = str(perfil_tipo[0][2:len(perfil_tipo[0])])
            self.B=perfil_tipo[1]
            self.peso=perfil_tipo[2]
            
        if perfil_tipo[0][0]=="O":
            self.seccion="O"
            ventana="Circulares Mayores"
            self.d = str(perfil_tipo[0][1:len(perfil_tipo[0])])
            self.dint=perfil_tipo[1]

        if perfil_tipo[0][0]=="o":
            self.seccion="o"
            ventana ="Circulares Menores"
            self.d = str(perfil_tipo[0][1:len(perfil_tipo[0])])
            self.dint=perfil_tipo[1]
            
        if perfil_tipo[0][0]=="W":
            self.seccion="W"
            ventana="HR"
            self.d = str(perfil_tipo[0][1:len(perfil_tipo[0])])
            self.bf=perfil_tipo[1]
            self.peso=perfil_tipo[2]
     
        self.datos=pd.read_excel(base_datos, sheet_name=ventana, header=11)
        self.verificador=True
        
        
        
        
        
        if self.seccion=="H" or self.seccion=="PH" or self.seccion=="W" or self.seccion=="HR":
            self.seccion_=[self.seccion,self.d,"x",self.bf,"x",self.peso]  
        if self.seccion=="o" or self.seccion=="O":
            self.seccion_=[self.seccion,self.d,"x",self.dint]
        if self.seccion=="[]":
            self.seccion_=[self.perfil,self.d,"x",self.B,"x",self.peso]
            

            
        

        if self.seccion =="H" or self.seccion =="PH":
            self.dt = self.datos.to_numpy().tolist()
            
            self.area = "nan"
            self.peso_ = "nan"
            self.Ixx = "nan"
            self.Iyy = "nan"
            
            for i in self.dt:
                    
                if str(i[1])==self.d and str(i[3])==self.bf and str(i[5])==self.peso:
                    self.area = i[9]/10**6
                    self.peso_ = i[5]
                    self.Ixx = i[10]
                    self.Iyy = i[14]
                    self.verificador=True
                
                                 
        if self.seccion == "W" or self.seccion == "HR":
            self.dt = self.datos.to_numpy().tolist()
            
            self.area = "nan"
            self.peso_ = "nan"
            self.Ixx = "nan"
            self.Iyy = "nan"
            
            for i in self.dt:
                    
                if str(i[5])==self.d and str(i[7])==self.bf and str(i[9])==self.peso:
                    self.area = i[13]/10**6
                    self.peso_ = i[9]
                    self.Ixx = i[14]
                    self.Iyy = i[18]
                    self.verificador=True
                
 
            
        if self.seccion=="O":
            self.dt = self.datos.to_numpy().tolist()
            
            self.area = "nan"
            self.peso_ = "nan"
            self.Ixx = "nan"
            self.Iyy = "nan"
            
            for i in self.dt:
                    
                if str(i[1])==self.d and str(i[3])==self.bf and str(i[5])==self.peso:
                    self.area = i[4]/10**6
                    self.peso_ = i[3]
                    self.I = i[5]
                    
                    self.verificador=True
                
  
                    
                    
        if self.seccion=="o":
            self.dt = self.datos.to_numpy().tolist()
            
            self.area = "nan"
            self.peso_ = "nan"
            self.Ixx = "nan"
            self.Iyy = "nan"
           
            for i in self.dt:
                    
                if str(i[1])==self.d and str(i[3])==self.bf and str(i[5])==self.peso:
                    
                    self.area = i[5]/10**6
                    self.peso_ = i[4]
                    self.I = i[6]
                
                    self.verificador=True
                 

                    
                    
        if self.seccion=="[]":
            self.dt = self.datos.to_numpy().tolist()
            
            self.area = "nan"
            self.peso_ = "nan"
            self.Ixx = "nan"
            self.Iyy = "nan"
            
            for i in self.dt:
                    
                if str(i[1])==self.D and str(i[3])==self.B and str(i[5])==self.peso:
                    self.area = i[8]/10**6
                    self.peso_ = i[5]
                    self.Ixx = i[9]
                    self.Iyy = i[13]
                    self.verificador=True
           

            
            
            
    def area(self, dt, bf,d,peso):
        
        # if self.verificador==True:
            # self.Ar = [self.area]/10**6
            
        return 0
  

    def peso(self):
        return 0

    def inercia_xx(self):
        return 0

    def inercia_yy(self):
        return 0

    def nombre(self):
        return self.denominacion

    def __str__(self):
       
        
        print ("  Area: ", self.area)           
        print ("  Peso: ", self.peso_)
        print ("  Ixx :", self.Ixx)
        print ("  Iyy :", self.Iyy)
        print ("")
        print ("")
        
        if self.area=="nan" and self.peso_=="nan" and self.Ixx=="nan" and self.Iyy=="nan":
        
            return f"Tipo de seccion {self.denominacion} no encontrada en base de datos A={self.area} Ix={self.Ixx} Iy={self.Iyy} \nSeccion ICHA {self.denominacion} "
            
        else:
            return f"{self.denominacion} encontrada. A={self.area} Ix={self.Ixx} Iy={self.Iyy} \nSeccion ICHA {self.denominacion} "

### AYUDANTE CORRECTOR
            # ESTE RETURN DEBIESE DE ESTAR ARRIBA DE LOS PRINT PARA QUE IMPRIMA ORDENADO.
            # PERO NO NOS FUNCIONO Y SE VE EN OTRO ORDEN. 
            # PERO LAS FUNCIONES CORREN PERFECTO, ESE FUE EL UNICO ERROR
        
        
        
        
        
        
