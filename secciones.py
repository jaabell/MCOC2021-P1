from numpy import pi, sqrt, nan
from numpy.random import rand
import pandas as pd
from constantes import g_, ρ_acero, mm_
 
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


class SeccionICHA(object):
    """Lee la tabla ICHA y genera una seccion apropiada"""

    def __init__(self, denominacion, base_datos="Perfiles ICHA.xlsx", debug=False, color=rand(3)):
        super(SeccionICHA, self).__init__()
        self.denominacion = denominacion
        self.color = color  #color para la seccion
        
    def area(self):
        return 0

    def peso(self):
        return 0

    def inercia_xx(self):
        return 0

    def inercia_yy(self):
        return 0

    def __str__(self): #  este es el print
       
        archivo = pd.ExcelFile('Perfiles ICHA.xlsx')

#############################
###### denominacion H #######
#############################

        if self.denominacion.find("H") == 0 and self.denominacion.find("R") == -1 : 
            df = archivo.parse("H",skiprows=11)
            H = list(df["H"])
            d = list(df["d"])
            bf = list(df["bf"])
            peso = list(df["peso"])
            area = list(df["A"])
            Ixx = list(df["Ix/10⁶"])
            Iyy = list(df["Iy/10⁶"])

            for i in range(len(H)-2):
                deno = str(H[i+2]) + str(int(d[i+2])) + "x" + str(int(bf[i+2])) + "x" + str(peso[i+2])
                if deno == self.denominacion:
                    print(deno+" encontrada A="+str(area[i+2]),"Ix="+str(Ixx[i+2]),"Iy="+str(Iyy[i+2]))
                    print("Seccion ICHA "+deno)
                    print("Area : "+str(area[i+2]))
                    print("Peso : "+str(peso[i+2]))
                    print("Ixx : "+str(Ixx[i+2]))
                    print("Iyy : "+str(Iyy[i+2]))
                    return ""
                elif i+2 == len(H)-1:
                    print("Tipo de seccion "+self.denominacion+". no encontrada en base de datos")
                    print("Seccion ICHA "+self.denominacion)
                    print("Area : nan")
                    print("Peso : nan")
                    print("Ixx : nan")
                    print("Iyy : nan")
                    return ""
#############################
###### denominacion PH ######
#############################

        elif self.denominacion.find("P") == 0 and self.denominacion.find("H") == 1 : 
            df = archivo.parse("PH",skiprows=11)
            PH = list(df["PH"])
            d = list(df["d"])
            bf = list(df["bf"])
            peso = list(df["peso"])
            area = list(df["A"])
            Ixx = list(df["Ix/10⁶"])
            Iyy = list(df["Iy/10⁶"])

            for i in range(len(PH)-2):
                deno = PH[i+2] + str(int(d[i+2])) + "x" + str(int(bf[i+2])) + "x" + str(peso[i+2])
                if deno == self.denominacion:
                    print(deno,"encontrada A="+str(area[i+2]),"Ix="+str(Ixx[i+2]),"Iy="+str(Iyy[i+2]))
                    print("Seccion ICHA "+deno)
                    print("Area : "+str(area[i+2]))
                    print("Peso : "+str(peso[i+2]))
                    print("Ixx : "+str(Ixx[i+2]))
                    print("Iyy : "+str(Iyy[i+2]))
                    return ""
                elif i+2 == len(PH)-1:
                    print("Tipo de seccion "+self.denominacion+". no encontrada en base de datos")
                    print("Seccion ICHA "+self.denominacion)
                    print("Area : nan")
                    print("Peso : nan")
                    print("Ixx : nan")
                    print("Iyy : nan")
                    return ""

#############################
#### denominacion HR o W ####
#############################

        elif self.denominacion.find("H") == 0 and self.denominacion.find("R") == 1 or self.denominacion.find("W") == 0 : #denominacion HR
            df = archivo.parse("HR",skiprows=11)
            W = list(df["W"])
            dnominal = list(df["dnominal"])
            peso_lbf = list(df["peso_lbf"])
            HR = list(df["HR"])
            d = list(df["d"])
            bf = list(df["bf"])
            peso = list(df["peso"])
            area = list(df["A"])
            Ixx = list(df["Ix/10⁶"])
            Iyy = list(df["Iy/10⁶"])

            for i in range(len(W)-2):
                deno = str(W[i+2]) + str(int(dnominal[i+2])) + "x" + str(peso_lbf[i+2])
                denoICHA = str(HR[i+2]) + str(int(d[i+2])) + "x" + str(int(bf[i+2])) + "x" + str(peso[i+2])
                if denoICHA == self.denominacion:
                    print(denoICHA,"encontrada A="+str(area[i+2]),"Ix="+str(Ixx[i+2]),"Iy="+str(Iyy[i+2]))
                    print("Seccion ICHA "+deno)
                    print("Area : "+str(area[i+2]))
                    print("Peso : "+str(peso[i+2]))
                    print("Ixx : "+str(Ixx[i+2]))
                    print("Iyy : "+str(Iyy[i+2]))
                    return ""
                elif deno == self.denominacion:
                    print(deno,"encontrada A="+str(area[i+2]),"Ix="+str(Ixx[i+2]),"Iy="+str(Iyy[i+2]))
                    print("Seccion "+deno)
                    print("Area : "+str(area[i+2]))
                    print("Peso : "+str(peso_lbf[i+2]))
                    print("Ixx : "+str(Ixx[i+2]))
                    print("Iyy : "+str(Iyy[i+2]))
                    return ""
                elif i+2 == len(W)-1:
                    print("Tipo de seccion "+self.denominacion+". no encontrada en base de datos")
                    print("Seccion ICHA "+self.denominacion)
                    print("Area : nan")
                    print("Peso : nan")
                    print("Ixx : nan")
                    print("Iyy : nan")
                    return ""

#############################
###### denominacion [] ######
#############################

        elif self.denominacion.find("[") == 0 and self.denominacion.find("]") == 1 : #denominacion cajon
            df = archivo.parse("Cajon",skiprows=11)
            cajon = list(df["[]"])
            D = list(df["D"])
            B = list(df["B"])
            peso = list(df["peso"])
            area = list(df["A"])
            Ixx = list(df["Ix/10⁶"])
            Iyy = list(df["Iy/10⁶"])

            for i in range(len(cajon)-2):
                deno = cajon[i+2] + str(int(D[i+2])) + "x" + str(int(B[i+2])) + "x" + str(peso[i+2])
                if deno == self.denominacion:
                    print(deno,"encontrada A="+str(area[i+2]),"Ix="+str(Ixx[i+2]),"Iy="+str(Iyy[i+2]))
                    print("Seccion ICHA "+deno)
                    print("Area : "+str(area[i+2]))
                    print("Peso : "+str(peso[i+2]))
                    print("Ixx : "+str(Ixx[i+2]))
                    print("Iyy : "+str(Iyy[i+2]))
                    return ""
                elif i+2 == len(cajon)-1:
                    print("Tipo de seccion "+self.denominacion+". no encontrada en base de datos")
                    print("Seccion ICHA "+self.denominacion)
                    print("Area : nan")
                    print("Peso : nan")
                    print("Ixx : nan")
                    print("Iyy : nan")
                    return ""

#############################
###### denominacion O #######
#############################

        elif self.denominacion.find("O") == 0 : #denominacion circulares mayores
            df = archivo.parse("Circulares Mayores",skiprows=10)
            D = list(df["D"])
            Dint = list(df["Dint"])
            peso = list(df["peso"])
            area = list(df["A"])
            I = list(df["I/10⁶"])

            for i in range(len(D)-2):
                deno = "O" + str(int(D[i+2])) + "x" + str(int(Dint[i+2]))
                if deno == self.denominacion:
                    print(deno,"encontrada A="+str(area[i+2]),"I="+str(I[i+2]))
                    print("Seccion ICHA "+deno)
                    print("Area : "+str(area[i+2]))
                    print("Peso : "+str(peso[i+2]))
                    print("I : "+str(I[i+2]))
                    return ""
                elif i+2 == len(D)-1:
                    print("Tipo de seccion "+self.denominacion+". no encontrada en base de datos")
                    print("Seccion ICHA "+self.denominacion)
                    print("Area : nan")
                    print("Peso : nan")
                    print("I : nan")
                    return ""
#############################
###### denominacion o #######
#############################

        elif self.denominacion.find("o") == 0 : #denominacion circulares menores
            df = archivo.parse("Circulares Menores",skiprows=10)
            D = list(df["D"])
            Dint = list(df["Dint"])
            peso = list(df["peso"])
            area = list(df["A"])
            I = list(df["I/10⁶"])

            for i in range(len(D)-2):
                deno = "o" + str(D[i+2]) + "x" + str(Dint[i+2])
                if deno == self.denominacion:
                    print(deno,"encontrada A="+str(area[i+2]),"I="+str(I[i+2]))
                    print("Seccion ICHA "+deno)
                    print("Area : "+str(area[i+2]))
                    print("Peso : "+str(peso[i+2]))
                    print("I : "+str(I[i+2]))
                    return ""
                elif i+2 == len(D)-1:
                    print("Tipo de seccion "+self.denominacion+". no encontrada en base de datos")
                    print("Seccion ICHA "+self.denominacion)
                    print("Area : nan")
                    print("Peso : nan")
                    print("I : nan")
                    return ""

#############################
# denominacion no encontrada #
#############################  

        else:
            print("Tipo de seccion "+self.denominacion+". no encontrada en base de datos")
            print("Seccion ICHA "+self.denominacion)
            print("Area : nan")
            print("Peso : nan")
            print("Ixx : nan")
            print("Iyy : nan")
            return ""
