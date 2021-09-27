import numpy as np
from scipy.linalg import solve
import h5py

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 1

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        self.K = None
        self.F = None
        self.u = None
        
        self.Kcc = None
        self.Kff = None
        self.Kcf = None
        self.Kfc = None
        
        self.uc = None
        self.uf = None
        
        self.Ff = None
        self.Fc = None
        self.R = None

    def agregar_nodo(self, x, y, z=0):
        
        
        numero_de_nodo_actual = self.Nnodos
        self.xyz.resize((numero_de_nodo_actual+1,3))
        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1
        
        return 0

    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        
        return np.array(self.xyz[n,:])

    def calcular_peso_total(self):
        res = 0
        
        for i in self.barras: res+= i.calcular_peso(self);
            
        return res

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        if nodo in self.restricciones:
            self.restricciones[nodo].append([gdl,valor])
        else:
            self.restricciones[nodo] = [[gdl,valor]]
            
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        if nodo in self.cargas:
            self.cargas[nodo].append([gdl,valor])
        else:
            self.cargas[nodo] = [[gdl,valor]]	
        
        return 0


    def ensamblar_sistema(self, factor_peso_propio=0.):
        n = (self.Nnodos)*3 
        self.K = np.zeros((n,n)) 
        self.F = np.zeros(n) #nodo [-1]*3 (dimension de K y f)
        
        
        
        for e in self.barras:
            
            d = [3*e.ni, 3*e.ni + 1, 3*e.ni + 2, 3*e.nj, 3*e.nj +1, 3*e.nj +2]
            ke = e.obtener_rigidez(self)
            fe = e.obtener_vector_de_cargas(self)
            if factor_peso_propio != [0.,0.,0.]:
                    
                    I1 = abs(factor_peso_propio[0])
                    I2 = abs(factor_peso_propio[1])
                    I3 = abs(factor_peso_propio[2])
                    valor = fe[2]
                    fe = [I1*valor, I2*valor, I3*valor, I1*valor, I2*valor, I3*valor ]
                    
            else:
                fe = np.zeros(6)
                
            for i in range (6):
                p = d[i]
                for j in range (6):
                    q = d[j]
                    self.K[p,q]+=ke[i,j]
                self.F[p] += fe[i]    
                
                    
            
                
                
                
        for node in self.cargas:
            for puntual in self.cargas[node]:
                gdl = puntual[0]
                valor = puntual[1]
                self.F[node*3 + gdl] = valor
                
        
        
        
              
        return 0



    def resolver_sistema(self):
        
        gdl_libres = [x for x in range(self.Nnodos*3)]
        gdl_fijos = []
        
        for node in self.restricciones:
            for apoyo in self.restricciones[node]:
                gdl = apoyo[0]
                gdl_fijos.append(node*3+gdl)
                
        gdl_libres = list(set(gdl_libres)-set(gdl_fijos))
        
        self.Kff = self.K[np.ix_(gdl_libres,gdl_libres)]
        self.Kcc = self.K[np.ix_(gdl_fijos,gdl_fijos)]
        self.Kcf = self.K[np.ix_(gdl_fijos,gdl_libres)]
        self.Kfc = self.K[np.ix_(gdl_libres,gdl_fijos)]
        
        self.u = np.zeros(self.Nnodos*3)
        
        self.uc = self.u[gdl_fijos]
        
        self.Ff = self.F[gdl_libres] - self.Kfc @ self.uc 
        
        self.u[gdl_libres]=solve(self.Kff,self.Ff)
        
        self.uf = self.u[gdl_libres]

        self.R=self.Kcf @ self.uf + self.Kcc @ self.uc - self.F[gdl_fijos]
        
        
        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        
        """Implementar"""	
        fuerzas_totales = []
        for i in self.barras:
            fuerzas_totales.append(i.obtener_fuerza(self))
        
        return np.array(fuerzas_totales)


    def obtener_factores_de_utilizacion(self, f):
        
        """Implementar"""	
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


    
    def guardar(self, nombre):
        fid=h5py.File(nombre,"w")
        
        fid.create_dataset("xyz", data = self.xyz)
        #fid.create_dataset("xyz", dtype=np.double)
        
        
        fid.create_dataset("barras", data = np.array([barra.obtener_conectividad() for barra in self.barras]))
        #fid.create_dataset("barras", dtype=np.int32)
        
        #data=[]
        #for barra in self.barras:
        #    data.append(barra.conec)
        #data=np.array(data)
        
        
        fid.create_dataset("secciones", data = np.array([np.string_(barra.seccion.nombre()) for barra in self.barras]))
        #fid.create_dataset("secciones", dtype=h5py.string_dtype())
        
        
        rests = []
        for nodo in self.restricciones:
            for rest in self.restricciones[nodo]:
                rests.append([nodo,rest[0]])
        fid.create_dataset("restricciones", data = np.array(rests))
        #fid.create_dataset("restricciones", dtype=np.int32)
        
        
        rests_val = []
        for nodo in self.restricciones:
            for rest in self.restricciones[nodo]:
                rests_val.append(rest[1])
        fid.create_dataset("restricciones_val", data = np.array(rests_val))
        #fid.create_dataset("restricciones_val", dtype=np.double)
        
        
        cargas = []
        for nodo in self.cargas:
            for carg in self.cargas[nodo]:
                cargas.append([nodo,carg[0]])
        fid.create_dataset("cargas", data = np.array(cargas))
        #fid.create_dataset("cargas", dtype=np.int32)
        
        
        cargas_val = []
        for nodo in self.cargas:
            for cargval in self.cargas[nodo]:
                cargas_val.append(cargval[1])
        fid.create_dataset("cargas_val", data = np.array(cargas_val))
        #fid.create_dataset("cargass_val", dtype=np.double)
        
        
        
        
        fid.close()

    def abrir(self):
        pass

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
        
