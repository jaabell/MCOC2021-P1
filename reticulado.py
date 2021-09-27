import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 1

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        #print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.Ndimensiones=3
        self.restricciones = {}
    
    def agregar_nodo(self, x, y, z=0):
        #print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos
        self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:] = [x, y, z]
        self.Nnodos += 1
    
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
        if nodo not in self.restricciones:
            self.restricciones[nodo]=[]

        self.restricciones[nodo].append([gdl,valor])  
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        if nodo not in self.cargas: 
            self.cargas[nodo]=[]
        
        self.cargas[nodo].append([gdl,valor])  
               
        return 0


    def ensamblar_sistema(self,factor_peso_propio):
        
        Ngdl = self.Nnodos * self.Ndimensiones
  
        self.K = np.zeros((Ngdl,Ngdl), dtype=np.double)
        self.f = np.zeros((Ngdl), dtype=np.double)
        self.u = np.zeros((Ngdl), dtype=np.double)
          
        for i,b in enumerate(self.barras):
              
            k_e = b.obtener_rigidez(self)
            f_e = b.obtener_vector_de_cargas(self,factor_peso_propio) 
            ni = b.ni
            nj = b.nj
            
            if self.Ndimensiones == 2:
                d = [2*ni, 2*ni+1, 2*nj, 2*nj+1]
            else:
  			    
                d = [3*ni, 3*ni+1, 3*ni+2, 3*nj, 3*nj+1, 3*nj+2]
            for i in range(self.Ndimensiones*2):
                p = d[i]
                for j in range(self.Ndimensiones*2):
                    q = d[j]
                    self.K[p,q] += k_e[i,j]
                self.f[p] = f_e[i]  
        
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
        self.Kfc=self.K[np.ix_(gdl_libres,gdl_fijos)]
        self.Kcf=self.K[np.ix_(gdl_fijos,gdl_libres)]
        self.Kcc=self.K[np.ix_(gdl_fijos,gdl_fijos)]
        self.Kff=self.K[np.ix_(gdl_libres,gdl_libres)]
        self.uc=self.u[gdl_fijos]
        self.uf=self.u[gdl_libres]
        self.Ff=self.f[gdl_libres]-self.Kfc @ self.uc
        self.Fc=self.f[gdl_fijos]-self.Kcf @ self.uf
        #self.R= self.Kcc @ self.uc -self.Fc
        self.u=np.zeros(self.Nnodos*3)
        
        
        self.u[gdl_libres]=solve(self.Kff,self.Ff)
        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        d = [3*n, 3*n+1, 3*n+2]
        
        return self.u[d]


    def obtener_fuerzas(self): #####################
        f = []
        for b in self.barras:
            f.append(b.obtener_fuerza(self))
        print(np.array(f))
        return np.array(f)


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
        for i in self.restricciones:
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
    

