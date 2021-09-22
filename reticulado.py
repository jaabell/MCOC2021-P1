import numpy as np
from scipy.linalg import solve, inv
import scipy.linalg as lin

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
        self.fuerzas = []
        """Implementar"""
        

    def agregar_nodo(self, x, y, z=0):
        self.xyz.resize((self.Nnodos + 1, 3))
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
        
        if nodo in self.restricciones: 
        
            self.restricciones[nodo].append([gdl, valor])

        else:
            self.restricciones[nodo]=[[gdl, valor]]
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        if nodo in self.cargas:

            self.cargas[nodo].append([gdl, valor])
        
        else:
            self.cargas[nodo]=[[gdl, valor]]	
        
        return 0



    def ensamblar_sistema(self, factor_peso_propio):
        #Ensambar riguidez y vector de cargas
        n=self.Nnodos*3
        self.k= np.zeros((n,n))
        self.u=np.zeros(n)
        self.f=np.zeros(n)
        factor_modificado=[]
        
        for p in range(2):
            for i in factor_peso_propio:
                factor_modificado.append(i)

        for e in self.barras: #aquí recorremos todas las barras
        #ni, nj nodos i y j consultamos a las barras
            ni= e.ni
            nj= e.nj
            ke=e.obtener_rigidez(self)

            fe=e.obtener_vector_de_cargas(self,factor_modificado)
            print(factor_peso_propio,factor_peso_propio)
            d= [3*ni, 3*ni+1, 3*ni+2, 3*nj, 3*nj+1, 3*nj+2]

            #Método de riguidez directa
            for i in range(6):
                p = d[i]
                for j in range(6):
                    q = d[j]
                    self.k[p,q]+=ke[i,j]
                self.f[p] += fe[i]

        #print(f"k = {self.k}")
        #Agregamos cargas puntuales
        #print(self.cargas)

        #for node in self.cargas:
            #print (self.cargas[node])
            #Ncargas=len(self.cargas[node])
            #print(Ncargas)
            #for carga in self.cargas[node]:
                #gdl=carga[0]
                #f=carga[1]
                #print(f"Agregando carga de {f} en GDL {gdl} ")
                #gld_global=3*node+gdl
                #print(f"f vale {f}")
                #F[gld_global]+=f
                #Vector de cargas externas??
        return 0

    def resolver_sistema(self):
        print(f"vector f= {self.f}")
        gdl_libres = np.arange(self.Nnodos*3)          #cant grados de libertad del sistema
        gdl_fijos=[]

        #Vemos las restricciones, gdl y valores
        for i in self.restricciones:
            for j in self.restricciones[i]:
                gdl = j[0]
                valor = j[1]
                gdl_global = gdl + i*3
                self.u[gdl_global] += valor
                gdl_fijos.append(gdl_global)

        gdl_fijos = np.array(gdl_fijos)
        gdl_libres = np.setdiff1d(gdl_libres, gdl_fijos)

        #Ahora con las cargas aplicadas al sistema (al igual como lo hicimos con ensamblar sistema)
        for n in self.cargas:
            for i in self.cargas[n]:
                gdl = i[0]
                valor = i[1]
                gdl_global = gdl + n*3
                self.f[gdl_global] += valor

        kff= self.k[np.ix_(gdl_libres, gdl_libres)]
        kcc= self.k[np.ix_(gdl_fijos, gdl_fijos)]
        kcf= self.k[np.ix_(gdl_fijos, gdl_libres)]
        kfc= self.k[np.ix_(gdl_libres, gdl_fijos)]

        uf = self.u[gdl_libres]
        uc = self.u[gdl_fijos]

        ff = self.f[gdl_libres]
        fc = self.f[gdl_fijos]
        print(f"vector ff = {ff}")
        print(f" Gdl libres= {gdl_libres}")
        print(f" Gdl fijos= {gdl_fijos}")

        r = solve(kff, ff-kfc@uc)
        
        self.u[gdl_libres] = r

        return 0

    def obtener_desplazamiento_nodal(self, n):
        gdl = [3*n, 3*n+1, 3*n+2]
        return self.u[gdl]	

    def obtener_fuerzas(self):
        contador = 0
        fz = np.zeros((len(self.barras)))
        for i in self.barras:
            fz[contador] = i.obtener_fuerza(self)
            self.fuerzas.append(fz[contador])
            contador +=1
        return fz


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

        #Nodos
        s = "nodos: \n"

        for i in range(len(self.xyz[0: self.Nnodos,:])):
            s += "  " + str(i) + ": " + "(" + str(self.xyz[i,0]) + ", " + str(self.xyz[i,1]) + ", " + str(self.xyz[i,2]) + ")"
            s+= "\n"
        #parte en 0 y llega hasta Nnodos tomando todos los valores que estan ahí (:)

        s += "\n"
        s += "\n"

        #Barras
        s+= "barras: \n"

        for i in range(len(self.barras)):
            s += "  " + str(i) + ": " + "[ " + str(self.barras[i].ni) + " " + str(self.barras[i].nj) + " ]"
            s += "\n"
        
        #Restricciones
        s += "\n"
        s+="restricciones: \n"

        for clave in self.restricciones:
            s += "  " + str(clave) + ": " + str(self.restricciones[clave]) + " " 
            s += "\n"
        s+="\n"

        #Cargas 
        #print(self.cargas)
        s+="Cargas: \n"
        for i in (self.cargas):
            s += "  " + str(i) + ": " + str(self.cargas[i]) + " " 
            s += "\n"             
        s+="\n"
        
        #Desplazamientos
        s+= "Desplazamientos: \n"
        lk=0
        Agrup=[]
        for i in range(len(self.u)):
            if lk>=(len(self.u)):
                break
            else:
                des=[]
                for l in range(3):
                    des.append(self.u[lk])
                    lk+=1
            Agrup.append(des) 
       
        for p in range(len(Agrup)):
             s += "  " + str(p) + ": " + "( " + str(Agrup[p][0])+", "+ str(Agrup[p][1])+", "+ str(Agrup[p][2]) + " )" 
             s+="\n"

                
        s+= "\n" 
    
    
        #Fuerzas
        s += "\n"
        s+="Fuerzas: \n"
        for i in range((len(self.fuerzas))):
            s += "  " + str(i) + ": " + str(self.fuerzas[i]) + " " 
            s += "\n"

        return s
