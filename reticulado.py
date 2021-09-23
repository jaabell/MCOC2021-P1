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
    
    def agregar_nodo(self, x, y, z=0):
        #print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos
        if self.Nnodos+1 > Reticulado.__NNodosInit__:
            self.xyz.resize((self.Nnodos+1,3))
            self.xyz[self.Nnodos,:] = [x, y, z]
            self.Nnodos += 1
            if z != 0.:
                self.Ndimensiones = 3
    
    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        if n >= self.Nnodos:
            return 
        return self.xyz[n, :]
        return 0

    def calcular_peso_total(self):
        peso = 0.
        for b in self.barras:
            peso += b.calcular_peso(self)
            return peso 
        
        return 0

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        #if no_esxiste_restriccion_para _el_nodo: #?????
        #self.restricciones[nodo]
        #self.restricciones[nodo].append(gdl,valor)  
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""   
        
        return 0


    def ensamblar_sistema(self):
        
        """Implementar"""   
        
        return 0



    def resolver_sistema(self):
        
        gdl_libres = [x for x in range(self.Nnodos*3)]
        gdl_fijos = []
        
        for node in self.restricciones:
            for R in self.restricciones[node]:
                gdl = R[0]
                gdl_fijos.append(node*3+gdl)
                
        gdl_libres = list(set(gdl_libres)-set(gdl_fijos))
        
        #for e in self.barras:
        self.Kcc=self.K[np.ix_(gdl_fijos,gdl_fijos)]
        self.Kff=self.K[np.ix_(gdl_libres,gdl_libres)]
        self.Kfc=self.K[np.ix_(gdl_libres,gdl_fijos)]
        self.Kcf=self.K[np.ix_(gdl_fijos,gdl_libres)]
        self.u=np.zeros(self.Nnodos*3)
        self.uf=self.u[gdl_libres]
        self.uc=self.u[gdl_fijos]
        self.uc=solve(self.Kff,self.Ff)
        self.Ff=self.f[gdl_libres]-self.Kfc @ self.uc
        self.Fc=self.f[gdl_fijos]-self.Kcf @ self.uf
        self.R= self.Kcc @ self.uc -self.Fc
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
        for i in range(len(self.xyz)):
            s+= f"\t {i}: ({self.obtener_coordenada_nodal(i)}) \n"
        
        s+="\n"
        s += "barras: \n"
        for i,j in enumerate(self.barras,start=0):
            s+= f"\t {i}: [{j.ni} {j.nj}] \n"
        
        s+="\n"
        s += "restricciones: \n"
        fod i in self.restricciones:
            s+= f"\t {i}: {self.restricciones[i]}\n"
        
        s+="\n"
        s += "cargas: \n"
        for i in self.cargas:
            s+= f"\t {i}: {self.cargas[i]}\n"
        return s

        s+="\n"
        s += "desplazamiento: \n"
        x=0
        y=0
        while x < (len(self.u)):
            s+=f"\t {y}: ({(self.u[x])}, {(self.u[x+1])}, {(self.u[x+2])}) \n"
            x+=3
            y+=1
        
        s+="\n"
        s+="fuerzas: \n" 
        for i,j in enumerate(self.barras,start=0):
            s+=f"\t {i}: {j.agregar_fuerza(self)} \n"
            
        s+="\n"
        
        return s
    

