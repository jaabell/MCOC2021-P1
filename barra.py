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

