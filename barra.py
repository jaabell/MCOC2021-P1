import numpy as np

from constantes import g_, ρ_acero, E_acero


class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, seccion):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.seccion = seccion


    def obtener_conectividad(self):
        return [self.ni, self.nj]

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        
        # """Implementar"""	
        
        
        ni = self.ni
        nj = self.nj
        
        xi = reticulado.xyz[ni,:]
        xj = reticulado.xyz[nj,:]
        
        
        #print (xi)
        
        #print (f"Barra {ni} a {nj} xi = {xi} xj = {xj}")
        
        dist_ij = np.linalg.norm(-xi + xj)
        
        return dist_ij

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        
        """Implementar"""	
        
        Area = self.seccion.area()
        Largo = self.calcular_largo(reticulado)
        #print (Largo)
        #print (Area)
        Peso = g_ * Largo * Area * ρ_acero
        
        
        return Peso

    def obtener_rigidez(self, ret):
        

        L = self.calcular_largo(ret)
        
        ni = self.ni
        nj = self.nj
        
        xi = ret.xyz[ni,:]
        xj = ret.xyz[nj,:]
        
        Lx = (xi[0]-xj[0]) 
        Ly = (xi[1]-xj[1]) 
        Lz = (xi[2]-xj[2]) 
        cosθx = Lx/L
        cosθy = Ly/L
        cosθz = Lz/L
        
        T=np.array([[-cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz]])
        ke = self.seccion.area()*E_acero/L*(T.T@T)
        return ke

    def obtener_vector_de_cargas(self, ret):
        
        """Implementar"""	
        W = self.calcular_peso(ret)
        return -W/2*np.array([0,0,1,0,0,1]) 


    def obtener_fuerza(self, ret):
        
        """Implementar"""	
    
        u_e = [0,0,0,0,0,0]
        u_e[:3] = ret.obtener_desplazamiento_nodal(self.ni)
        u_e[3:] = ret.obtener_desplazamiento_nodal(self.nj)
        A = self.seccion.area()
        L = self.calcular_largo(ret)
        
        ni = self.ni
        nj = self.nj
        
        xi = ret.xyz[ni,:]
        xj = ret.xyz[nj,:]
        
        Lx = (xi[0]-xj[0]) 
        Ly = (xi[1]-xj[1]) 
        Lz = (xi[2]-xj[2]) 
        cosθx = Lx/L
        cosθy = Ly/L
        cosθz = Lz/L
        
        T=np.array([-cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz])
        
        se = A*E_acero/L * T.T @ u_e
        print (se)
        return se




    
    
    
    
    
    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0





    
    
    
    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


   

    
    
    
    def rediseñar(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0

