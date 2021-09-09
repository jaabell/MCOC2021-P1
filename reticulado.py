import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    def __init__(self):
        super(Reticulado, self).__init__()       
        """Implementar"""
        #
        #self.Reticulado=Reticulado
        #
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype = np.double)
        self.Nnodos = 0	
        self.barras = []
        self.cargas = {}
        self.restricciones = {}


    def agregar_nodo(self, x, y, z=0):
        """Implementar"""	

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
        """Implementar"""
        peso=0
        for b in self.barras:
            peso+=b.calcular_peso(self)	 
        return peso

    def obtener_nodos(self):
        
        return self.xyz[0:self.Nnodos,:].copy()

    def obtener_barras(self):	
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        """Implementar"""	
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        """Implementar"""	
        
        return 0


    def ensamblar_sistema(self):
        """Implementar"""	
        
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
