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

    


    def area(self):
        

        palabras=[]
        palabra=''
        for i in self.denominacion:
            
            if i == 'H':
                continue
            elif i == 'R':
                continue
            elif i == '[':
                continue
            elif i == ']':
                continue
            elif i =='x':
                palabras.append(float(palabra))
                palabra=''

            else:
                palabra += i

        palabras.append(palabra)
        print(palabras)
        datos=pd.read_excel('Perfiles ICHA.xlsx', sheet_name='HR',header=None)

        for i in range(0,len(datos[5])):

            if datos[5][i] == palabras[0]:
                        
                if datos[7][i]==palabras[1]:
                            
                    if datos[9][i]==float(palabras[2]):

                        return datos[13][i]
                        
        datos1=pd.read_excel('Perfiles ICHA.xlsx', sheet_name='H',header=None) 

        for i in range(0,len(datos1[1])):

            if datos1[1][i] == palabras[0]:
                       
                if datos1[3][i] == palabras[1]:

                    if datos1[5][i] ==  float(palabras[2]):
                        
                        return datos1[9][i]
                        
        datos2=pd.read_excel('Perfiles ICHA.xlsx', sheet_name='Cajon',header=None)   

        for i in range(0,len(datos2[1])):

            if datos2[1][i] == palabras[0]:

                if datos2[3][i] == palabras[1]:
                    

                    if datos2[5][i] == float(palabras[2]):
                        
                        return datos2[8][i]

        

    def peso(self):
        palabras=[]
        palabra=''
        for i in self.denominacion:
            
            if i == 'H':
                continue
            elif i == 'R':
                continue
            elif i == '[':
                continue
            elif i == ']':
                continue
            elif i =='x':
                palabras.append(float(palabra))
                palabra=''

            else:
                palabra += i

        return(palabras[2])


    def inercia_xx(self):
        

        palabras=[]
        palabra=''
        for i in self.denominacion:
            
            if i == 'H':
                continue
            elif i == 'R':
                continue
            elif i == '[':
                continue
            elif i == ']':
                continue
            elif i =='x':
                palabras.append(float(palabra))
                palabra=''

            else:
                palabra += i

        palabras.append(palabra)
        print(palabras)
        
        datos=pd.read_excel('Perfiles ICHA.xlsx', sheet_name='HR',header=None)

        for i in range(0,len(datos[5])):

            if datos[5][i] == palabras[0]:
                        
                if datos[7][i]==palabras[1]:
                            
                    if datos[9][i]==float(palabras[2]):
                        
                        return datos[13][i]
                        
        datos1=pd.read_excel('Perfiles ICHA.xlsx', sheet_name='H',header=None)    

        for i in range(0,len(datos1[1])):

            if datos1[1][i] == palabras[0]:
                       
                if datos1[3][i] == palabras[1]:

                    if datos1[5][i] ==  float(palabras[2]):
                        
                        return datos1[9][i]
                        
        datos2=pd.read_excel('Perfiles ICHA.xlsx', sheet_name='Cajon',header=None) 

        for i in range(0,len(datos2[1])):

            if datos2[1][i] == palabras[0]:
                
                if datos2[3][i] == palabras[1]:
                    

                    if datos2[5][i] == float(palabras[2]):
                        
                        return datos2[9][i]
    def inercia_yy(self):
        

        palabras=[]
        palabra=''
        for i in self.denominacion:
            
            if i == 'H':
                continue
            elif i == 'R':
                continue
            elif i == '[':
                continue
            elif i == ']':
                continue
            elif i =='x':
                palabras.append(float(palabra))
                palabra=''

            else:
                palabra += i

        palabras.append(palabra)
        print(palabras)
        datos=pd.read_excel('Perfiles ICHA.xlsx', sheet_name='HR',header=None)

        for i in range(0,len(datos[5])):

            if datos[5][i] == palabras[0]:
                        
                if datos[7][i]==palabras[1]:
                            
                    if datos[9][i]==float(palabras[2]):
                        
                        return datos[13][i]
                        
        datos1=pd.read_excel('Perfiles ICHA.xlsx', sheet_name='H',header=None)

        for i in range(0,len(datos1[1])):

            if datos1[1][i] == palabras[0]:
                       
                if datos1[3][i] == palabras[1]:

                    if datos1[5][i] ==  float(palabras[2]):
                        
                        return datos1[9][i]
                        
        datos2=pd.read_excel('Perfiles ICHA.xlsx', sheet_name='Cajon',header=None)    

        for i in range(0,len(datos2[1])):

            if datos2[1][i] == palabras[0]:
                

                if datos2[3][i] == palabras[1]:
                    

                    if datos2[5][i] == float(palabras[2]):
        
                        return datos2[12][i]

    def __str__(self):
        

        return f"Seccion ICHA {self.denominacion} \n Area:  {SeccionICHA.area(self)}\n Peso:  {SeccionICHA.peso(self)}\n Ixx:  {SeccionICHA.inercia_xx(self)}\n Iyy:  {SeccionICHA.inercia_yy(self)}"