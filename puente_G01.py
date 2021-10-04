# -*- coding: utf-8 -*-

from barra import Barra
import numpy as np
from secciones import SeccionICHA
from reticulado import Reticulado
from math import sqrt
from graficar3d import ver_reticulado_3d
from constantes import *
def Puente_Tipo_Golden() :
    
    # Unidades base
    m = 1.
    kg = 1.
    s = 1.

    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N

    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa

    #Parametros
    L = 5.0 *m
    F = 400*KN
    B = 2.0 *m


    #Inicializar modelo
    ret = Reticulado()

    #Nodos

    #Apoyos
    #West
    ret.agregar_nodo(10 , 0 , 100 )#0
    ret.agregar_nodo(10 , 4 , 100 )#1

    #Este
    ret.agregar_nodo(118 , 0 , 100 )#2
    ret.agregar_nodo(118 , 4 , 100 )#3

    #Anclajes
    #West
    ret.agregar_nodo(-25. ,0 ,100.0 )#4
    ret.agregar_nodo(-25. ,4 ,100.0 )#5
    #Este
    ret.agregar_nodo(118. ,0 ,100.0 )#6
    ret.agregar_nodo(118. ,4 ,100.0 )#7

    for i in range(8):# 0 - 7
        ret.agregar_restriccion(i, 0, 0)
        ret.agregar_restriccion(i, 1, 0)
        ret.agregar_restriccion(i, 2, 0)

    #Torres
    props_torres = SeccionICHA("[]350x150x37.8", color="#3A8431")

    ret.agregar_nodo(10 , 0 , 140 )#8
    ret.agregar_nodo(10 , 4 , 140 )#9
    ret.agregar_barra(Barra(0, 8,props_torres)) #0
    ret.agregar_barra(Barra(1, 9, props_torres)) #1

    #Este
    ret.agregar_nodo(108 , 0 , 140 )#10
    ret.agregar_nodo(108 , 4 , 140 )#11
    ret.agregar_barra(Barra(2, 10, props_torres)) #2
    ret.agregar_barra(Barra(3, 11, props_torres)) #3

    #Roadway
    props_road = SeccionICHA("[]350x150x37.8", color="#3A8431")
    for i in range(35):# 12 - 81
        ret.agregar_nodo(10. + 100.*(i+1)/36. , 0 , 100 )#12 + i
        ret.agregar_nodo(10. + 100.*(i+1)/36. , 4 , 100 )#13 + i
    ret.agregar_barra(Barra(0, 12, props_road)) #4
    ret.agregar_barra(Barra(1, 13, props_road)) #5
    for i in range(67): # 6 - 73
        ret.agregar_barra(Barra(12+i, 12+i+2, props_road))#6 + i
        ret.agregar_barra(Barra(13+i, 13+i+2, props_road))#7 + i
    ret.agregar_barra(Barra(80, 2, props_road))#74
    ret.agregar_barra(Barra(81, 3, props_road))#75


    #Cables

    #Cuadrático
    a = 24./9245.
    b = -1128./1849.
    c = 288150./1849.
    for i in range(35):# 82 - 149
        x = 10. + 100.*(i+1)/36.
        ret.agregar_nodo(x , 0 , a*x**2 + b*x + c )#82 + i
        ret.agregar_nodo(x , 4 , a*x**2 + b*x + c )#83 + i
    ret.agregar_barra(Barra(82, 8, props_road))#76
    ret.agregar_barra(Barra(83, 9, props_road))#77
    for i in range(67): # 78 - 149
        ret.agregar_barra(Barra(82+i, 82+i+2, props_road))#
        ret.agregar_barra(Barra(83+i, 83+i+2, props_road))#
    ret.agregar_barra(Barra(148, 10, props_road))#
    ret.agregar_barra(Barra(149, 11, props_road))#

    #Tensores
    props_tensor  = SeccionICHA("[]80x40x8", color="#A3500B")
    #West
    ret.agregar_barra(Barra(4, 8, props_tensor))
    ret.agregar_barra(Barra(5, 9, props_tensor))
    #Este
    ret.agregar_barra(Barra(6, 10, props_tensor))
    ret.agregar_barra(Barra(7, 11, props_tensor))

    #RoadWay
    props_cable_road  = SeccionICHA("[]80x40x8", color="#A3500B")
    for i in range(69): # 6 - 29
        ret.agregar_barra(Barra(82+i, 10+i+2, props_road))#6 + i
        ret.agregar_barra(Barra(83+i, 11+i+2, props_road))#7 + i
    #ret.agregar_barra(Barra(0, 1, *props_cable_road))
    for i in range(6,40):
        ret.agregar_barra(Barra(2*i, (2*i)+3, props_road))#6 + i
        ret.agregar_barra(Barra((2*i)+1, (2*i)+2, props_road))#7 + i
        
    ret.agregar_fuerza(4,2,-F)

    return ret


ver_reticulado_3d(Puente_Tipo_Golden())