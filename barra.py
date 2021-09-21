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
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        
        ni = self.ni
        nj = self.nj

        xi = reticulado.xyz[ni,:]
        xj = reticulado.xyz[nj,:]

        #print(f"Barra {ni} a {nj} xi = {xi} xj = {xj}") ??

        largo = np.linalg.norm(xi-xj)
 
        return largo

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        masa = self.calcular_largo(reticulado)*self.seccion.area()*ρ_acero
        gravedad = g_
        peso = masa*gravedad
        
        return peso
    
    def calcular_area(self, reticulado):
        """Devuelve el area de la barra.""" 
        
        area = self.seccion.area()
        
        return area
    
    def obtener_rigidez(self, ret):
        
        cosθx = Lx/L
        cosθy = Ly/L
        cosθz = Lz/L 
        
        ke =  self.seccion.area()*E_acero/L * T.T @ T

        return ke

    def obtener_vector_de_cargas(self, ret):
        
        """Implementar"""	
        
        return -W/2*array([0,1,0,1])

    def obtener_fuerza(self, ret):
        
        se = A*E_acero/L*T*u_e
        
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


