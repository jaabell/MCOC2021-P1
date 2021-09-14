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

        #print(f"Barra {ni} a {nj} xi = {xi} xj = {xj}")

        return np.linalg.norm(xj - xi)

    def calcular_area(self):
        return self.seccion.area()

    def calcular_peso(self, reticulado):
        """Implementar"""
        return ((self.calcular_area())*(self.calcular_largo(reticulado))*(ρ_acero)*(g_))


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


