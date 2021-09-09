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

        xi = reticulado.xyz[ni,:]
        xj = reticulado.xyz[nj,:]
            
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


    def obtener_rigidez(self, ret):
        
        """Implementar"""	
        
        return 0

    def obtener_vector_de_cargas(self, ret):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerza(self, ret):
        
        """Implementar"""	
        
        return 0




    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0





    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


    def rediseñar(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


