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

        busc = self.buscador()

        dfs = pd.read_excel(base_datos, sheet_name = busc[0])

        v = 0
        for i in dfs.index:
            if str(dfs.iloc[i,0]) != 'nan':
                v = i
                break

        pos_titulo_1 = v
        pos_titulo_2 = pos_titulo_1 + 2
        pos_titulo_3 = pos_titulo_2 + 4

        if busc[0] == "H" or busc[0] == "PH":
            dfs.columns = [dfs.loc[pos_titulo_2]]
        
            self.row_fin = dfs.iloc[0,:]
            for index, row in dfs.iterrows():
                if (row['d'] == busc[1]) and (row['bf'] == busc[2]) and (row['peso'] == busc[3]):
                    self.row_fin = dfs.loc[index,:]
            #print(self.row_fin)

        elif busc[0] == "HR":
            dfs.iloc[pos_titulo_2, 3] = "peso (lbf/pie)"
            dfs.columns = [dfs.loc[pos_titulo_2]]
        
            self.row_fin = dfs.iloc[0,:]
            for index, row in dfs.iterrows():
                if (row['d'] == busc[1]) and (row['bf'] == busc[2]) and (row['peso'] == busc[3]):
                    self.row_fin = dfs.loc[index,:]
            #print(self.row_fin)

        elif busc[0] == "Cajon":
            dfs.columns = [dfs.loc[pos_titulo_2]]
        
            self.row_fin = dfs.iloc[0,:]
            for index, row in dfs.iterrows():
                if (row['D'] == busc[1]) and (row['B'] == busc[2]) and (row['peso'] == busc[3]):
                    self.row_fin = dfs.loc[index,:]
            #print(self.row_fin)

        elif busc[0] == "Circulares Mayores":
            pos_titulo_2 -= 1
            dfs.columns = [dfs.loc[pos_titulo_2]]

            self.row_fin = dfs.iloc[0,:]
            for index, row in dfs.iterrows():
                if (row['D'] == busc[1]) and (row['Dint'] == busc[2]) and (row['t'] == busc[3]):
                    self.row_fin = dfs.loc[index,:]
            #print(self.row_fin)

        elif busc[0] == "Circulares Menores":
            pos_titulo_2 -= 1
            dfs.columns = [dfs.loc[pos_titulo_2]]

            self.row_fin = dfs.iloc[0,:]
            for index, row in dfs.iterrows():
                if (row['D'] == busc[1]) and (row['Dint'] == busc[2]) and (row['t'] == busc[3]):
                    self.row_fin = dfs.loc[index,:]
            #print(self.row_fin)
        
    def area(self):
        return self.row_fin['A']/(1e6)

    def peso(self):
        return self.row_fin['peso']

    def inercia_xx(self):
        if 'Ix/10⁶' in self.row_fin:
            return self.row_fin['Ix/10⁶']
        else:
            return self.row_fin['I/10⁶']

    def inercia_yy(self):
        if 'Iy/10⁶' in self.row_fin:
            return self.row_fin['Iy/10⁶']
        else:
            return self.row_fin['I/10⁶']

    def buscador(self):
        #Lista del tipo [HR, 1118, 405, 517,7]
        deno = self.denominacion
        for index, letter in enumerate(deno, 0):
            if letter.isdigit():
                deno = [deno[:index],deno[index:]]
                break

        den = []
        den.append(deno[0])
        deno2 = deno[1].split('x')
        for i in deno2:
            den.append(float(i))

        return den


    def __str__(self):

        value = True

        for i in self.row_fin.values:
            if str(i) != 'nan':
                value = True
                break
            else:
                value = False

        if value:
            s = f"{self.denominacion} encontrada. A={self.area()} Ix={self.inercia_xx()} Iy={self.inercia_yy()}\n"
        else:
            s = "Tipo de seccion " + self.denominacion + " no encontrada en base de datos\n"

        s += f"Seccion ICHA {self.denominacion}\n"
        s += f"  Area : {self.area()}\n"
        s += f"  peso : {self.peso()}\n"
        s += f"  Ixx  : {self.inercia_xx()}\n"
        s += f"  Iyy  : {self.inercia_yy()}\n"

        return s