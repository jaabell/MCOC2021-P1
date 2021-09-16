import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self): 
        super(Reticulado, self).__init__()
        
        #print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        """Implementar"""	
        
        

    def agregar_nodo(self, x, y, z=0):

        #print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1

        return 0

    def agregar_barra(self, barra):

        self.barras.append(barra)	

        return 0

    def obtener_coordenada_nodal(self, n):

        if n>= self.Nnodos:
            return
        return self.xyz[n, :]
    	
    def calcular_peso_total(self):
        peso=0
        for b in self.barras:
            peso+=b.calcular_peso(self)	 
        return peso

    def obtener_nodos(self):
        
        return self.xyz

      
    def obtener_barras(self):	
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        #agrego restricción y consulto en el nodo
        
        if no_existe_restriccion_en_nodo:
        
            self.restricciones[nodo]
        
        self.restricciones[nodo].append(gdl, valor)
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        if no_existe_fuerza_en_nodo:
            self.carga[nodo]
        
        self.carga[nodo].append(gdl, valor)	
        
        return 0



    def ensamblar_sistema(self, factor_peso_propio=0):
        #Ensambar riguidez y vector de cargas
        for e in self.barras: #aquí recorremos todas las barras
        #ni, nj nodos i y j consultamos a las barras
            ni= e.ni
            nj= e.nj
            ke=e.obtener_riguidez()
            fe=e.obtener_vector_de_carga()
            d= [3*ni, 3*ni+1, 3*ni+2, 3*nj, 3*nj+1, 3*nj+2]	

        #Método de riguidez directa
        for i in range(6):
            p=d[i]
            for j in range(6):
                q= d[j]
                k[p,q]+=k_e[i,j]
            f[p]+=f_e[i]

        #Agregamos cargas puntuales

        for node in cargas:
            print(node)
            Ncargas= len(cargas[node])
            print(Ncargas)
        return 0

    def resolver_sistema(self):
        """Implementar"""	
        
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

        s = "nodos: \n"

        for i in range(len(self.xyz[0: self.Nnodos,:])):
            s += "  " + str(i) + ": " + "(" + str(self.xyz[i,0]) + ", " + str(self.xyz[i,1]) + ", " + str(self.xyz[i,2]) + ")"
            s+= "\n"
        #parte en 0 y llega hasta Nnodos tomando todos los valores que estan ahí (:)

        s += "\n"
        s += "\n"

        s+= "barras: \n"

        for i in range(len(self.barras)):
            s += "  " + str(i) + ": " + "[ " + str(self.barras[i].ni) + " " + str(self.barras[i].nj) + " ]"
            s += "\n"

        return s
