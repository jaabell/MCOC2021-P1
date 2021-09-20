from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d
from constantes import *
from secciones import Circular



#Inicializar modelo
ret = Reticulado()

#Nodos
ret.agregar_nodo(0,0)
ret.agregar_nodo(1,0)
ret.agregar_nodo(1,1)

#Seccion
circular_200_40 = Circular(200*mm_, 4*mm_)

#Barras
b1 = Barra(0, 1, circular_200_40)
b2 = Barra(1, 2, circular_200_40)
b3 = Barra(0, 2, circular_200_40)

ret.agregar_barra(b1)
ret.agregar_barra(b2)
ret.agregar_barra(b3)

print(ret)

peso_total = ret.calcular_peso_total()

print(f"peso_total = {peso_total}")

ver_reticulado_2d(ret)
