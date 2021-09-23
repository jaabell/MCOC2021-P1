import numpy as np
from scipy.linalg import solve
import scipy.linalg as lin
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

  ##################################################  ENTREGA 3  
    
    
    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        
        if nodo in self.restricciones:
            self.restricciones[nodo].append = ([gdl, valor])
        
        else:
            self.restricciones[nodo] = [[gdl, valor]]
        
        return 0
        
     
        

    def agregar_fuerza(self, nodo, gdl, valor):
        
               
        if nodo in self.cargas:
            self.cargas[nodo].append = ([gdl, valor])
        
        else:
            self.cargas[nodo] = [[gdl, valor]]
     
        return 0

        # if no_existe_fuerza_pal_nodo:
        #     self.cargas[nodo] = []
            
        # self.cargas[nodo].append(gdl, valor)
        
        # return 0


    def ensamblar_sistema(self, factor_peso_propio=0.):
        
        """Implementar"""	
        
        #Deben quedar definidas al terminar esta funcion

        
        return 0

        

    def resolver_sistema(self):
        
        numero_grado_libertad = self.Nnodos * self.Ndimensiones
        gdl_libres = np.arange(numero_grado_libertad)
        gdl_fijos = []
        
        for i in self.restricciones:
             for restriccion in self.restricciones[i]:
                  grado, valor = restriccion[0], restriccion[1]
                  gdl_general = grado + self.Ndimensiones*i
                  self.u[gdl_general] = valor
                  gdl_fijos.append(gdl_general)
        
        gdl_fijos = np.array(gdl_fijos)
        gdl_libres = np.setdiff1d(gdl_libres, gdl_fijos)
        
        for k in self.cargas:
            for z in self.cargas[k]:
                grado, valor = z[0], z[1]
                gdl_general = grado + self.Ndimensiones*k
                self.f[gdl_general] = valor
      
        Kff = self.K[np.ix_(gdl_libres, gdl_libres)]
        Kcc = self.K[np.ix_(gdl_fijos,gdl_fijos)]
        Kfc = self.K[np.ix_(gdl_libres,gdl_fijos)]
        Kcf = self.K[np.ix_(gdl_fijos,gdl_libres)]
        uf, uc = self.u[gdl_libres], self.u[gdl_fijos]
        ff, fc = self.f[gdl_libres], self.f[gdl_fijos]
        uf = solve(Kff, ff - Kfc @ uc)
        R = Kcf@uf+Kcc@uc-fc
        
        ### FINALMENTE ###
        self.u[gdl_libres] = uf
        self.R = R
        self.Kff = Kff
        self.Kcc = Kcc
        self.Kfc = Kfc
        self.Kcf = Kcf
       

        return 0

    

 
    def obtener_desplazamiento_nodal(self, n):
        
        if self.Ndimensiones == 2:
            dofs = [2*n, 2*n+1]
        elif self.Ndimensiones == 3:
            dofs = [3*n, 3*n+1, 3*n+2]
        
        return self.u[dofs]
        


    def obtener_fuerzas(self):
        
        """Implementar"""	
        
        return 0

    #################################################
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
        
        s="nodos: \n"
        for i in range(self.Nnodos):
            s+=f"\t {i}: ({self.xyz[i][0]} {self.xyz[i][1]} {self.xyz[i][2]}) \n"
        s+="\n"
        
        s+="barras: \n"
        for i,j in enumerate(self.barras,start=0):
            s+=f"\t {i}: [{j.ni} {j.nj}] \n"
        s+="\n"
        
        s+="restricciones: \n"
        for i in self.restricciones:
            s+=f"\t {i}: {self.restricciones[i]} \n"
        s+="\n"
        
        s+="cargas: \n"
        for i in self.cargas:
            s+=f"\t {i}: {self.cargas[i]} \n"
        s+="\n"
        
        s+="desplazamientos: \n"
        i=0
        j=0
        while i < (len(self.u)):
            s+=f"\t {j}: ({(self.u[i])}, {(self.u[i+1])}, {(self.u[i+2])}) \n"
            i+=3
            j+=1
        s+="\n"
        
        s+="fuerzas: \n" 
        for i,j in enumerate(self.barras,start=0):
            s+=f"\t {i}: {j.obtener_fuerza(self)} \n"
        s+="\n"
        
        
        return s
