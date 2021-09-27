from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d
from constantes import *
from math import sqrt
from secciones import Circular

L = 2.*m_

#Inicializar modelo
ret = Reticulado()

#Nodos
ret.agregar_nodo(0,0)
ret.agregar_nodo(L,0)
ret.agregar_nodo(2*L,0)
ret.agregar_nodo(L/2,sqrt(3)/L)
ret.agregar_nodo(3*L/2,sqrt(3)/L)

#Secciones de las barras
circular_200_4 = Circular(200*mm_, 4*mm_)
circular_200_8 = Circular(200*mm_, 8*mm_)

#Crear y agregar las barras
ret.agregar_barra(Barra(0, 1, circular_200_4)) #0
ret.agregar_barra(Barra(1, 2, circular_200_4)) #1
ret.agregar_barra(Barra(3, 4, circular_200_8)) #2
ret.agregar_barra(Barra(0, 3, circular_200_8)) #3
# ret.agregar_barra(Barra(3, 1, circular_200_4)) #4
ret.agregar_barra(Barra(1, 4, circular_200_4)) #5
ret.agregar_barra(Barra(4, 2, circular_200_8)) #6

#Crear restricciones
ret.agregar_restriccion(0, 0, 0)
ret.agregar_restriccion(0, 1, 0)
ret.agregar_restriccion(2, 1, 0)

#Fijar todos los nodos en Z
for n in range(ret.Nnodos):
	ret.agregar_restriccion(n, 2, 0.)

#Cargar el nodo 4 en la direccion 1 (Y)
ret.agregar_fuerza(4, 1, -100*KN_)

#Visualizar y comprobar las secciones
opciones_barras = {
	"ver_secciones_en_barras": True,
}
ver_reticulado_2d(ret,opciones_barras=opciones_barras)

#Resolver el problema
ret.ensamblar_sistema()
ret.resolver_sistema()
f = ret.obtener_fuerzas()

#Ver todo el reticulado en texto
print(ret)

#Visualizar resultados de fuerzas y nodos 
opciones_nodos = {
	"usar_posicion_deformada": True,
	"factor_amplificacion_deformada": 2e3,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato": f,
	"ver_fuerza_en_barras" : True
}

ver_reticulado_2d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras)

Kff = ret.Kff

from scipy.linalg import eigh

w,v = eigh(Kff)

print(w)
print(v)

modo = 0

ret.u[ret.gdl_libres] = v[:,modo]
opciones_nodos = {
	"usar_posicion_deformada": True,
	"factor_amplificacion_deformada": 0.4,
}
ver_reticulado_2d(ret, opciones_nodos=opciones_nodos)