# MCOC2020 - Proyecto 2
# ==========================================================
# ver_reticulado_2d
#
# Funciones sencillas para visualizar reticulados en 2d. 
#
# 2020 - www.joseabell.com 
# Facultad de Ingeniería y Ciencias Aplicadas
# Universidad de los Andes
# ==========================================================

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Opciones para nodos
opc_nodos_default = {
    "marcador_nodos": "o", 
    "ver_numeros_de_nodos": True,
    "color_nodos": "k",
    "color_borde_nodos": [0.7,0.7,0.7],
    "usar_posicion_deformada": False,
    "factor_amplificacion_deformada": 1.,
    "datos_desplazamientos_nodales": None,
}

#Opciones para nodos
opc_barras_default = {
    "estilo_barras" : "-",
    "color_barras" : [138/255,89/255,0/255],#8F652F
    "grosor_barras" : 2,
    "ver_numeros_de_barras" : True,
    "color_barras_por_dato" : False,
    "ver_dato_en_barras" : False,
    "formato_dato_en_barras" : "4.2f",
    "color_barra_min" : np.array([1, 0, 0]),
    "color_barra_max" : np.array([0, 0, 1]),
    "color_barra_cero" : np.array([0, 0, 0]),
    "color_fondo" : np.array([1, 1, 1, 0.5]),
    "usar_posicion_deformada": False,
    "factor_amplificacion_deformada": 1.,
    "datos_desplazamientos_nodales": None,
    "ver_secciones_en_barras": False,
    "color_barras_por_seccion": False,
}

def graficar_nodos(ret, fig, opciones):

    for key in opc_nodos_default:
        if key not in opciones:
            opciones[key] = opc_nodos_default[key]


    # plt.figure(fig)
    # Nodos
    xyz = ret.obtener_nodos().copy()

    if opciones["usar_posicion_deformada"]: 
        if opciones["datos_desplazamientos_nodales"] is None:
            u = ret.u
        else:
            u = opciones["datos_desplazamientos_nodales"]
        factor = opciones ["factor_amplificacion_deformada"]
        uvw = u.reshape((-1,3))
        xyz = xyz +  factor*uvw
    
    ax = fig.gca()

    ax.plot(xyz[:,0], xyz[:,1], xyz[:,2],
        marker=opciones["marcador_nodos"],
        markerfacecolor=opciones["color_nodos"],
        markeredgecolor=opciones["color_borde_nodos"],
        linestyle="",
        )

    if opciones["ver_numeros_de_nodos"]:
        for n in range(xyz.shape[0]):
            ax.text(xyz[n,0], xyz[n,1], xyz[n,2], f"{n}", color=opciones['color_nodos'])


def graficar_barras(ret, fig, opciones):

    ax = fig.gca()

    for key in opc_barras_default:
        if key not in opciones:
            opciones[key] = opc_barras_default[key]

    xyz = ret.obtener_nodos()[:,0:3].copy()

    if opciones["usar_posicion_deformada"]: 
        if opciones["datos_desplazamientos_nodales"] is None:
            u = ret.u
        else:
            u = opciones["datos_desplazamientos_nodales"]
        factor = opciones ["factor_amplificacion_deformada"]
        uvw = u.reshape((-1,3))
        xyz +=  factor*uvw

    if opciones["color_barras_por_dato"]:
        f = opciones["dato"]
        fmax = f.max()
        fmin = f.min()
        c_min = opciones["color_barra_min"]
        c_max = opciones["color_barra_max"]
        c_cero = opciones["color_barra_cero"]

    c = opciones["color_barras"]
    fmt = opciones["formato_dato_en_barras"]
    txt_case = int(opciones["ver_numeros_de_barras"]) + 2*int(opciones["ver_dato_en_barras"])
    
    for i,b in enumerate(ret.obtener_barras()):
        nodos = b.obtener_conectividad()
        x =  xyz[nodos,0]
        y =  xyz[nodos,1]
        z =  xyz[nodos,2]

        if opciones["color_barras_por_dato"]:
            if f[i] < 0:
                xi = 1-(f[i]-fmin)/(0 - fmin)
                c = xi*c_min + (1-xi)*c_cero
            else:
                xi = 1-(fmax - f[i])/(fmax - 0)
                c = xi*c_max + (1-xi)*c_cero

        if opciones["color_barras_por_seccion"]:
            c = b.seccion.color

        ax.plot(x,y,z,
            linestyle=opciones["estilo_barras"],
            color=c,
            linewidth=opciones["grosor_barras"],
            )

        if txt_case > 0:
            x0 = x.mean()
            y0 = y.mean()
            z0 = z.mean()
            th = 0#np.rad2deg(np.arctan2(y[1]-y[0],x[1]-x[0]))
            if txt_case == 1:
                if opciones["ver_secciones_en_barras"]:
                    txt = ("{0} : {1}").format(i,b.seccion.nombre())
                else:
                    txt = f"{i}"
            elif txt_case == 2:
                txt = ("{0:"+fmt+"}").format(f[i])
            else:
                txt = ("{0} : {1:"+fmt+"}").format(i,f[i])
            ax.text(x0, y0, z0, txt , 
                color=c, 
                rotation=th,
                horizontalalignment="center",
                verticalalignment="center",
                backgroundcolor=opciones["color_fondo"],
                )

def ver_reticulado_3d(ret, fig=1, 
    ver_nodos=True,
    ver_barras=True,
    opciones_nodos = opc_nodos_default,
    opciones_barras = opc_barras_default,
    #Otras opciones
    llamar_show=True,
    ver_grilla=True,
    axis_Equal=True,
    nueva_figura=True,
    tamaño_nueva_figura = [8, 6],
    zoom = 100,
    deshabilitar_ejes=False,
    titulo=""
    ):

    if nueva_figura:
        fig = plt.figure()
        fig.set_size_inches(tamaño_nueva_figura, forward=True)
        ax = fig.add_subplot(111, projection='3d')

    if ver_nodos:
        graficar_nodos(ret, fig, opciones_nodos)

    if opciones_nodos["usar_posicion_deformada"]:
        opciones_barras["usar_posicion_deformada"]=opciones_nodos["usar_posicion_deformada"]
        opciones_barras["factor_amplificacion_deformada"]=opciones_nodos["factor_amplificacion_deformada"]
        opciones_barras["datos_desplazamientos_nodales"]=opciones_nodos["datos_desplazamientos_nodales"]

    if ver_barras:
        graficar_barras(ret, fig, opciones_barras)

    
    plt.grid(ver_grilla)

    if axis_Equal:
        # ax.set_box_aspect([1,1,1])
        # ax.axis('equal')
        x_limits = ax.get_xlim3d()
        y_limits = ax.get_ylim3d()
        z_limits = ax.get_zlim3d()

        x_range = abs(x_limits[1] - x_limits[0])
        x_middle = np.mean(x_limits)
        y_range = abs(y_limits[1] - y_limits[0])
        y_middle = np.mean(y_limits)
        z_range = abs(z_limits[1] - z_limits[0])
        z_middle = np.mean(z_limits)

        # The plot bounding box is a sphere in the sense of the infinity
        # norm, hence I call half the max range the plot radius.
        plot_radius = 50./zoom*max([x_range, y_range, z_range])

        ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
        ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
        ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

    if deshabilitar_ejes:
        ax = plt.gca()
        ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
        ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
        ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
        ax.set_axis_off()

    plt.title(titulo)

    if llamar_show:
        plt.show()
