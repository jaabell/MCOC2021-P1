from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA

L = 2.*m_
H = 2.*m_
B = 1.*m_

#Inicializar modelo
ret = Reticulado()

#Nodos
ret.agregar_nodo(0    ,0,0)
ret.agregar_nodo(L    ,0,0)
ret.agregar_nodo(2*L  ,0,0)
ret.agregar_nodo(L/2  ,B/2,sqrt(3)/H)
ret.agregar_nodo(3*L/2,B/2,sqrt(3)/H)
ret.agregar_nodo(0    ,B,0)
ret.agregar_nodo(L    ,B,0)
ret.agregar_nodo(2*L  ,B,0)

#Secciones de las barras
seccion_grande = SeccionICHA("[]350x150x37.8", color="#3A8431")#, debug=True)
seccion_chica = SeccionICHA("[]80x40x8", color="#A3500B")


#Crear y agregar las barras
ret.agregar_barra(Barra(0, 1, seccion_chica)) #0
ret.agregar_barra(Barra(1, 2, seccion_chica)) #1
ret.agregar_barra(Barra(3, 4, seccion_grande)) #2
ret.agregar_barra(Barra(0, 3, seccion_grande)) #3
ret.agregar_barra(Barra(3, 1, seccion_chica)) #4
ret.agregar_barra(Barra(1, 4, seccion_chica)) #5
ret.agregar_barra(Barra(4, 2, seccion_grande)) #6
ret.agregar_barra(Barra(5, 6, seccion_chica)) #7
ret.agregar_barra(Barra(6, 7, seccion_chica)) #8
ret.agregar_barra(Barra(5, 3, seccion_grande)) #9
ret.agregar_barra(Barra(3, 6, seccion_chica)) #10
ret.agregar_barra(Barra(6, 4, seccion_chica)) #11
ret.agregar_barra(Barra(4, 7, seccion_grande)) #12
ret.agregar_barra(Barra(0, 5, seccion_chica)) #13
ret.agregar_barra(Barra(1, 6, seccion_chica)) #14
ret.agregar_barra(Barra(2, 7, seccion_chica)) #15
ret.agregar_barra(Barra(0, 6, seccion_chica)) #15
ret.agregar_barra(Barra(1, 5, seccion_chica)) #15
ret.agregar_barra(Barra(6, 2, seccion_chica)) #15
ret.agregar_barra(Barra(1, 7, seccion_chica)) #15




#Crear restricciones
for nodo in [0,5]:
	ret.agregar_restriccion(nodo, 0, 0)
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)

for nodo in [2,7]:
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)


#Cargar el nodo 4 en la direccion 1 (Y)
ret.agregar_fuerza(4, 2, -100*KN_)

#Visualizar y comprobar las secciones
opciones_barras = {
	"ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)


ret.guardar("04a_ejemplo_reticulado_guardar.h5")
