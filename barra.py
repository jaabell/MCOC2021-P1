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
    
    def obtener_rigidez(self, ret): ############################
        
        L = self.calcular_largo(ret)

        ni = self.ni
        nj = self.nj

        xi = ret.xyz[ni,:]
        xj = ret.xyz[nj,:]

        Lx = xj[0]-xi[0]
        Ly = xj[1]-xi[1]
        Lz = xj[2]-xi[2]

        cosθx = Lx/L
        cosθy = Ly/L
        cosθz = Lz/L 

        T = np.array([-cosθx,-cosθy,-cosθz,cosθx,cosθy,cosθz]).reshape((6,1))

        ke =  self.seccion.area()*E_acero/L * (T @ T.T)

        return ke

    def obtener_vector_de_cargas(self, ret, factor_peso_propio): ######################
        
        W = self.calcular_peso(ret)

        return -W/2*np.array([factor_peso_propio[0],factor_peso_propio[1],factor_peso_propio[2],factor_peso_propio[0],factor_peso_propio[1],factor_peso_propio[2]])

    def obtener_fuerza(self, ret):  #################################

        
        A = self.seccion.area()
        L = self.calcular_largo(ret)
        
        ni = self.ni
        nj = self.nj

        u_e = np.zeros(6)
        u_e[0:3] = ret.obtener_desplazamiento_nodal(ni) #Arreglar aca
        u_e[3:6] = ret.obtener_desplazamiento_nodal(nj)
        
        xi = ret.xyz[ni,:]
        xj = ret.xyz[nj,:]
        Lx = xj[0]-xi[0]
        Ly = xj[1]-xi[1]
        Lz = xj[2]-xi[2]
        
        cosθx = Lx/L
        cosθy = Ly/L
        cosθz = Lz/L 

        T = np.array([-cosθx,-cosθy,-cosθz,cosθx,cosθy,cosθz]).reshape((6,1))

        se = A*E_acero/L*(T.T @ u_e)
        
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

