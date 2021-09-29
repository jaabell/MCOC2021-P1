
from scipy.linalg import solve
from barra import Barra
import numpy as np
from scipy.linalg import solve
from barra import Barra
#bar = Barra()
class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()

        print("Constructor de Reticulado")

        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}




    def agregar_nodo(self, x, y, z=0):



        print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1

        return 0

    def agregar_barra(self, barra):

        self.barras.append(barra)

        return 0

    def obtener_coordenada_nodal(self, n):

        corn = self.xyz[n,:]


        #print(f"la posicion del nodo {n} es en las cordenadas =  {corn}")
        return corn
    def calcular_peso_total(self):
        pesototalbarras = 0
        for barra in self.barras:
            w_barra= barra.calcular_peso(self)
            pesototalbarras+= w_barra

        return pesototalbarras

    def obtener_nodos(self):

        return self.xyz

    def obtener_barras(self):

        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        print(f"Agregando una restriccion en: ({nodo} {gdl} {valor})")

        if nodo in self.restricciones:  #Si el nodo no está en las restricciones, se agrega

            self.restricciones[nodo] = []
            self.restricciones[nodo].append([gdl, valor])
            return 0
        else :
            self.restricciones[nodo] = ([gdl, valor])
            return 0

        #print (restricciones)


        return 0

    def agregar_fuerza(self, nodo, gdl, valor):

        print(f"Agregando una fuerza en: ({nodo} {gdl} {valor})")

        if nodo in self.cargas: #Si no existe el nodo, se agrega.

            self.cargas[nodo] = []
            self.cargas.append([gdl, valor])
            return 0
        else:

            self.cargas[nodo] = ([gdl, valor])
            return 0

        #print (cargas)

    #Actualizacion de fn agregar_restriccion/fuerza funcionando    


    #emsamblar sistema parcialmente realizado
    def ensamblar_sistema(self, factor_peso_propio=0):
        factor_peso_propio=0


        Nm = self.Nnodos*3 #según las dimensiones
        self.K = np.zeros((Nm,Nm),dtype=np.float32)
        self.f = np.zeros(Nm)
        self.u = np.zeros(Nm)

        for e in (self.barras):

            ke = e.obtener_rigidez(self)
            fe = e.obtener_vector_de_cargas(self)
            wbarra = e.calcular_peso(self)
            ni,nj = e.obtener_conectividad(self)

            if factor_peso_propio == 0:
                factor_peso_propio [0, 0, 0]
                f = np.zeros(6)
            d = [3*ni,3*ni+1, 3*ni+2,3*nj,3*nj+1,3*nj+2]

            for i in range(6):
                p = d[i]
                for j in range(6):
                    q = d[j]
                    self.K[p,q] += ke[i,j]
                self.f[p] += fe[i]
            for n in range(self.Nnodos):
                for carga in self.cargas(n):
                    if len(carga)!= 0:
                        self.f[n*N_dimensiones+carga[0]] += carga[1]
            self.F.append(f)


            return 0




    # -----------------------------EJEMPLO CLASE PROFE--------------------------



    #       for e in self.barras: #recore las barras #barras tiene [N°barra | ni | nj]
    #           ni = self.barras[1]
    #           nj = self.barras[2]
    #
    #           ke = e.obtener_rigidez()
    #           fe = e.obtener_vector_de_carga()
    #           d = [3*ni,3*ni+1, 3*ni+2,3*nj,3*nj+1,3*nj+2]
    #
#3           for i in range(6):
    #               p = d[i]
    #               for j in range(6):
    #                   q = d[j]
    #                   K[p,q] += k_e[i,j]
    #               f[p] += f_e[i]
    #
    #           #agregar cargas puntuales
    #
    #3           for nodo in cargas:
        #                   print(nodo)
        #                   Ncargas = len(cargas[nodo])
        #                   print(Ncargas)
        #
        #                   for carga in range :
        #
        #                       gdl = cargas[nodo][0]
        #                       f = cargas[nodo][1]
        #                      print(f"Agregando carga de {f} en GDL {gdl}")
        #
        #                      gdl_global = 3*node + gdl
        #                      F[gdl_global] += f
        #
        #
        #

        #self.K #matriz rigidez
        #self.u # grados de libertad

        #---------------------FIN EJEMPLO PROFE----------------------------------------


        def resolver_sistema(self):

            """Implementar"""
            # A DEFININIR

            #self.Ff
            #self.Fc
            #self.Kcc
            #self.Kff
            #self.Kfc
            #self.Kcf

            #self.u
            #self.uf
            #self.uc

            #self.R REACCIONES

            #para graficar ret.u

            return 0

        def obtener_desplazamiento_nodal(self, n):

            """Implementar"""

            return 0


        def obtener_fuerzas(self):

            """Implementar"""

            return 0


        def obtener_factores_de_utilizacion(self, f):

            """Implementar"""

            return 0

        def rediseñar(self, Fu, ϕ=0.9):

            """Implementar"""

            return 0



        def chequear_diseño(self, Fu, ϕ=0.9):

            """Implementar"""

            return 0







        def __str__(self):

            s = "Soy un reticulado :) \n"

            s += "Nodos: \n"

            for i in range(self.Nnodos):
                s += f"{i} : ({self.xyz[i][0]}, {self.xyz[i][1]}, {self.xyz[i][2]})\n"
                i += 1

            s += "Barras: \n"

            h = 0
            for i in self.barras:
                s += f"{h} : [{self.barras[h].ni} {self.barras[h].nj}]\n"
                h += 1

            return s


import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        """Implementar"""	
        


    def agregar_nodo(self, x, y, z=0):
        
        """Implementar"""	

        print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1
        
        return 0

    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        
        """Implementar"""	
        
        return 0

    def calcular_peso_total(self):
        
        """Implementar"""	
        
        return 0

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        """Implementar"""	
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""	
        
        return 0


    def ensamblar_sistema(self, factor_peso_propio=0.):
        
        """Implementar"""	
        
        return 0



    def resolver_sistema(self):
        
        """Implementar"""	
        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        
        fuerzas = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            fuerzas[i] = b.obtener_fuerza(self)

        return fuerzas


    def obtener_factores_de_utilizacion(self, f, ϕ=0.9):
        
        FU = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            FU[i] = b.obtener_factor_utilizacion(f[i], ϕ)

        return FU


    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        cumple = True
        for i,b in enumerate(self.barras):
            if not b.chequear_diseño(Fu[i], self, ϕ):
                print(f"----> Barra {i} no cumple algun criterio. ")
                cumple = False
        return cumple


    def guardar(self, nombre):

        """Implementar"""   

        return 0

    def abrir(self, nombre):

        """Implementar"""   

        return 0



    def __str__(self):

        s = "Soy un reticulado :)"

        s += "\n"
        
        s += str(self.xyz[0 : self.Nnodos,:])

        return s
