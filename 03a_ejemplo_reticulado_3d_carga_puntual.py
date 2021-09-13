from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import Circular

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
circular_200_4 = Circular(200*mm_, 4*mm_, color="#3E701D")
circular_200_8 = Circular(200*mm_, 8*mm_, color="#A3500B")

#Crear y agregar las barras
ret.agregar_barra(Barra(0, 1, circular_200_4)) #0
ret.agregar_barra(Barra(1, 2, circular_200_4)) #1
ret.agregar_barra(Barra(3, 4, circular_200_8)) #2
ret.agregar_barra(Barra(0, 3, circular_200_8)) #3
ret.agregar_barra(Barra(3, 1, circular_200_4)) #4
ret.agregar_barra(Barra(1, 4, circular_200_4)) #5
ret.agregar_barra(Barra(4, 2, circular_200_8)) #6
ret.agregar_barra(Barra(5, 6, circular_200_4)) #7
ret.agregar_barra(Barra(6, 7, circular_200_4)) #8
ret.agregar_barra(Barra(5, 3, circular_200_8)) #9
ret.agregar_barra(Barra(3, 6, circular_200_4)) #10
ret.agregar_barra(Barra(6, 4, circular_200_4)) #11
ret.agregar_barra(Barra(4, 7, circular_200_8)) #12
ret.agregar_barra(Barra(0, 5, circular_200_4)) #13
ret.agregar_barra(Barra(1, 6, circular_200_4)) #14
ret.agregar_barra(Barra(2, 7, circular_200_4)) #15
ret.agregar_barra(Barra(0, 6, circular_200_4)) #15
ret.agregar_barra(Barra(1, 5, circular_200_4)) #15
ret.agregar_barra(Barra(6, 2, circular_200_4)) #15
ret.agregar_barra(Barra(1, 7, circular_200_4)) #15




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




#Resolver el problema
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0.])
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
	"dato":f
}


ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras)
