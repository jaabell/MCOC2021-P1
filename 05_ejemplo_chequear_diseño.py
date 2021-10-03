from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA
import math
L = 5.*m_
H = 3.*m_
B = 4.*m_

q = 400*kgf_/m_**2

F = B*L*q

#Inicializar modelo
ret = Reticulado()

"""Linea nodo 1"""
ret.agregar_nodo(0,0,0)

i=0
l=3.74
while i<=110:
    ret.agregar_nodo(l,0,0)
    l+=5
    i+=5
ret.agregar_nodo(117.48,0,0)

"""Linea nodos 2"""
i=0
l=3.74
ang=45
z=l*math.tan(math.radians(ang))
while i<=110:
    ret.agregar_nodo(l,0,-z)
    l+=5
    i+=5

"""Linea nodo 3"""
ret.agregar_nodo(0,4,0)

i=0
l=3.74
while i<=110:
    ret.agregar_nodo(l,4,0)
    l+=5
    i+=5
ret.agregar_nodo(117.48,4,0)

"""Linea nodos 4"""
i=0
l=3.74
ang=45
z=l*math.tan(math.radians(ang))
while i<=110:
    ret.agregar_nodo(l,4,-z)
    l+=5
    i+=5


#Secciones de las barras
seccion_grande_XL = SeccionICHA("H900x300x143.5", color="#3A8431")#, debug=True)
seccion_grande = SeccionICHA("H900x300x134.4", color="#3A8431")#, debug=True)
seccion_mediana = SeccionICHA("H800x300x126.5", color="#3A8431")#, debug=True)
seccion_chica_XL = SeccionICHA("H450x150x35.9", color="#3A8431")#, debug=True)
seccion_chica = SeccionICHA("[]12x12x0.3", color="#A3500B")
seccion_circular = SeccionICHA("o12.7x10.9", color="#A3500B")
seccion_circular_XS = SeccionICHA("O210x200", color="#A3500B")



"""Barras abajo"""
i=0
while i <= 23:
    ret.agregar_barra(Barra(i,i+1,seccion_grande))
    i+=1

i=25
while i<=46:
    ret.agregar_barra(Barra(i,i+1,seccion_grande_XL))
    i+=1

i=48
while i<=71:
    ret.agregar_barra(Barra(i,i+1,seccion_mediana))
    i+=1    


i=73
while i<=94:
    ret.agregar_barra(Barra(i,i+1,seccion_mediana))
    i+=1


"""Barras profundidad"""
i=0
p=48
while i<=24:
    ret.agregar_barra(Barra(i,p,seccion_chica))
    i+=1
    p+=1
    
i=25
p=73
while i<=47:
    ret.agregar_barra(Barra(i,p,seccion_chica))
    i+=1
    p+=1


"""Barras altura"""
ret.agregar_barra(Barra(0,25,seccion_grande))
i=1
p=25
while i<=23:
    ret.agregar_barra(Barra(i,p,seccion_chica_XL))
    i+=1
    p+=1


ret.agregar_barra(Barra(24,47,seccion_chica_XL))
ret.agregar_barra(Barra(48,73,seccion_chica_XL))


i=49
p=73
while i<=71:
    ret.agregar_barra(Barra(i,p,seccion_mediana))
    i+=1
    p+=1


ret.agregar_barra(Barra(72,95,seccion_chica_XL))


"""Diagonales planta"""
i=0
p=48
while i<24:
    if i%2==0:
        ret.agregar_barra(Barra(i,p+1,seccion_chica))
    else:
        ret.agregar_barra(Barra(i+1,p,seccion_chica))
    i+=1
    p+=1
    
    
"""Diagonales techo"""
i=25
p=73
while i<47:
    if i%2==0:
        ret.agregar_barra(Barra(i,p+1,seccion_chica))
    else:
        ret.agregar_barra(Barra(i+1,p,seccion_chica))
    i+=1
    p+=1


"""Barras diagonales laterales"""
i=1
p=25
while i<=22:
    if i%2==0:
        ret.agregar_barra(Barra(i+1,p,seccion_circular_XS))
    else:
        ret.agregar_barra(Barra(i+1,p,seccion_circular_XS))
    i+=1
    p+=1

i=49
p=73
while i<=70:
    if i%2==0:
        ret.agregar_barra(Barra(i+1,p,seccion_circular_XS))
    else:
        ret.agregar_barra(Barra(i+1,p,seccion_circular_XS))
    i+=1
    p+=1


"""Diagonales por puente"""
i=1
p=73
while i<=23:
    if i%2==0:
        ret.agregar_barra(Barra(i,p,seccion_circular))
    i+=1
    p+=1

i=49
p=25
while i<=71:
    if i%2!=0:
        ret.agregar_barra(Barra(i,p,seccion_circular))
    i+=1
    p+=1


#Crear restricciones
for nodo in [0,48]:
     ret.agregar_restriccion(nodo, 0, 0)
     ret.agregar_restriccion(nodo, 1, 0)
     ret.agregar_restriccion(nodo, 2, 0)

for nodo in [24,72]:
     ret.agregar_restriccion(nodo, 1, 0)
     ret.agregar_restriccion(nodo, 2, 0)
     

#Visualizar y comprobar las secciones
opciones_barras = {
	# "ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)


#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()


# Agregar fuerzas tablero
F1 = B*q*(3.74*m_)
ret.agregar_fuerza(0, 2, -F1/4)
ret.agregar_fuerza(48, 2, -F1/4)
ret.agregar_fuerza(24, 2, -F1/4)
ret.agregar_fuerza(72, 2, -F1/4)


#agregar fuerza a nodo inicial
Ft = F1/4 + F/4
ret.agregar_fuerza(1, 2, -Ft)
ret.agregar_fuerza(49, 2, -Ft)
ret.agregar_fuerza(23, 2, -Ft)
ret.agregar_fuerza(71, 2, -Ft)


#resto de nodos
i=2
while i<23:
    ret.agregar_fuerza(i,2,-F/2)
    i+=1
    
i=49+1
while i<71:
    ret.agregar_fuerza(i,2,-F/2)
    i+=1


#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
ret.resolver_sistema()
f_L = ret.obtener_fuerzas()


#Visualizar f_L en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_L
}

ver_reticulado_3d(ret, 
 	opciones_nodos=opciones_nodos, 
 	opciones_barras=opciones_barras,
 	titulo="Carga Viva")


#Visualizar f_L en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_D
}

ver_reticulado_3d(ret, 
 	opciones_nodos=opciones_nodos, 
 	opciones_barras=opciones_barras,
	titulo="Carga Muerta")


#Calcular carga ultima (con factores de mayoracion)
fu = 1.2*f_D + 1.6*f_L


#Visualizar combinacion en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":fu
}


ver_reticulado_3d(ret, 
 	opciones_nodos=opciones_nodos, 
 	opciones_barras=opciones_barras,
 	titulo="1.2D + 1.6L")



cumple = ret.chequear_diseño(fu, ϕ=0.9)

if cumple:
	print(":)  El reticulado cumple todos los requisitos")
else:
	print(":(  El reticulado NO cumple todos los requisitos")


#Calcular factor de utilizacion para las barras
factores_de_utilizacion = ret.obtener_factores_de_utilizacion(fu, ϕ=0.9)


#Visualizar FU en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
	# "factor_amplificacion_deformada": 1.,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":factores_de_utilizacion
}


ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Factor Utilizacion")


ret.guardar("05_ejemplo_chequear_diseño.h5")


