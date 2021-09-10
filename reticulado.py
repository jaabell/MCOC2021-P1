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
     
        coordenada_nodal = self.xyz[n]
        print(f"{n}: {coordenada_nodal}")
        return (coordenada_nodal)
        
        
        
        
    def calcular_peso_total(self):
        
        """Implementar"""	
        
        peso_total = 0
        for i in self.barras:
            peso_total += i.calcular_peso(self)
        return peso_total
        
        
        
        
        
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
        
        barras = self.obtener_barras()
        
        numero = 0
        print ("barras :")
        for k in barras :
            
            
            print  (str(numero) + " : " + str(((k.ni,k.nj))))
         
            numero +=1
        
        nodos = self.obtener_nodos()
        numero = 0
        k = 0
        
      
        while k < len(self.xyz):
            
            print ("nodo" + str(numero) + " = " + str(nodos[numero]))
            
            k += 1
            numero +=1
