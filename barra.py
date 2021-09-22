import numpy as np
from constantes import g_, ρ_acero, E_acero


class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, seccion, color=np.random.rand(3)):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.seccion = seccion
        self.color = color


    def obtener_conectividad(self):
        return [self.ni, self.nj]


    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimension (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimension (3,) con coordenadas del nodo j
        """
        
        ni = self.ni
        nj = self.nj

        xi = reticulado.xyz[ni,:] # [xi,yi]
        xj = reticulado.xyz[nj,:] # [xj,yj]
            
        largo = np.sqrt(np.sum((xi - xj)**2))
        
        #print(f"Barra {ni} a {nj} xi = {xi} xj = {xj}")

        return largo
    
    
    def calcular_area(self):
        """Devuelve el area de la barra. """
        
        seccion = self.seccion
        area = seccion.area()
    
        return area


    def calcular_peso(self, reticulado):
        """Devuelve el peso de la barra"""
        
        seccion = self.seccion
        peso = seccion.peso()
        largo = self.calcular_largo(reticulado)
        
        return peso*largo


#Se creo la función obtener la matriz de transformacion para evitar la repeteticion de codigo continuamente
    def obtener_T(self,ret):
        
        """Implementar"""
        
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimension (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimension (3,) con coordenadas del nodo j
        """
        
        ni = self.ni
        nj = self.nj

        xi = ret.xyz[ni,:] # [xi,yi]
        xj = ret.xyz[nj,:] # [xj,yj]
            
        L = self.calcular_largo(ret)
        
       # cosx = ()/largo
        cos_theta_neg_x = (xi[0]-xj[0])/L
        cos_theta_neg_y = (xi[1]-xj[1])/L
        cos_theta_neg_z = (xi[2]-xj[2])/L
        #T = array([-cos(θ)x, -cos(θ)y, -cos(θ)z, cos(θ)x, cos(θ)y, cos(θ)z])
        T = np.array([[cos_theta_neg_x,cos_theta_neg_y,cos_theta_neg_z,-cos_theta_neg_x,-cos_theta_neg_y,-cos_theta_neg_z]])
        
        return T


    def obtener_rigidez(self, ret):
        
        """Implementar"""
        
        
        T = self.obtener_T(ret)
        L = self.calcular_largo(ret)
        
        ke = (self.seccion.area()*E_acero/L) * T.T @ T
        
        return ke #definir cosenos en funcion de los nodos y el largo 
    

    def obtener_vector_de_cargas(self, ret):
        
        """Implementar"""
        W = self.calcular_peso(ret)      
        return -W/2*np.array([0,0,1,0,0,1]) #definir W


    def obtener_fuerza(self, ret):
        
        """Implementar"""
        
        ni = self.ni
        nj = self.nj
        
        A = self.calcular_area()
        L = self.calcular_largo(ret)
        T = self.obtener_T(ret)
        
        u = ret.u
        
        u_e = np.array([[u[3*ni], u[3*ni+1], u[3*ni+2], u[3*nj], u[3*nj+1], u[3*nj+2]]])
        se = A*E_acero/L * T @ u_e.T
        
        return se[0][0]


    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


    def rediseñar(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


