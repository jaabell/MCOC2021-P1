import numpy as np
from constantes import g_, ρ_acero, E_acero


class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, seccion,color=np.random.rand(3)):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.seccion = seccion
        self.color   = color
    

    def obtener_conectividad(self):
        return [self.ni, self.nj]

    def calcular_area(self):
        A = self.seccion.area
        return A

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra.
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        xi = reticulado.obtener_coordenada_nodal(self.ni)
        xj = reticulado.obtener_coordenada_nodal(self.nj)
        dij = xi-xj
        return np.sqrt(np.dot(dij,dij))

    def calcular_peso(self, reticulado):
        
        L = self.calcular_largo(reticulado)
        Peso = self.seccion.peso()
        print(Peso)
        return Peso * L


    def obtener_rigidez(self, ret):
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz ]).reshape((6,1))

        return E_acero * A / L * (Tθ @ Tθ.T )

    def obtener_vector_de_cargas(self, ret):
        
        W = self.calcular_peso(ret)

        return np.array([0, 0, -W, 0, 0, -W])


    def obtener_fuerza(self, ret):
        ue = np.zeros(6)
        ue[0:3] = ret.obtener_desplazamiento_nodal(self.ni)
        ue[3:] = ret.obtener_desplazamiento_nodal(self.nj)

        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz ]).reshape((6,1))

        return E_acero * A / L * (Tθ.T @ ue)



    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""   
        area = self.seccion.area()
        peso = self.seccion.peso()
        inercia_xx = self.seccion.inercia_xx()
        inercia_yy = self.seccion.inercia_yy()
        nombre = self.seccion.nombre()
        
        #Resistencia nominal
        Fn = area * σy_acero

        #Revisar resistencia nominal
        if abs(Fu) > ϕ*Fn:
            print(f"Resistencia nominal Fu = {Fu} ϕ*Fn = {ϕ*Fn}")
            return False

        L = self.calcular_largo(ret)

        #Inercia es la minima
        I = min(inercia_xx, inercia_yy)
        i = np.sqrt(I/area)

        #Revisar radio de giro
        if Fu >= 0 and L/i > 300:
            print(f"Esbeltez Fu = {Fu} L/i = {L/i}")
            return False

        #Revisar carga critica de pandeo
        if Fu < 0:  #solo en traccion
            Pcr = np.pi**2*E_acero*I / L**2
            if abs(Fu) > Pcr:
                print(f"Pandeo Fu = {Fu} Pcr = {Pcr}")
                return False
        
        """Implementar"""   
        #Si pasa todas las pruebas, estamos bien
        return True
        


    def rediseñar(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""   
        




    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        A = self.seccion.area()
        Fn = A * σy_acero

        return abs(Fu) / (ϕ*Fn)


