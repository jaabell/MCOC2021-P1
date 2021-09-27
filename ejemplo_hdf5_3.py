from matplotlib.pylab import *
import h5py

#creacion del archivo
fid = h5py.File("ejemplo_3.h5", "w")


#creacion del dataset
barras = fid.create_dataset("barras", 
	shape=(10, 2), 
	maxshape=(None, 2), #ilimitado en la dimension 0)
	dtype=int32 )


secciones = fid.create_dataset("secciones", shape=(1, ), 
	maxshape=(None,), #ilimitado en la dimension 0)
	dtype=h5py.string_dtype() )

for i in range(100):
	barras.resize((i+1,2))  #hago crecer el dataset
	barras[i,:] = [2*i, 2*i+1]   #puedo escribir

	secciones.resize((i+1,))  #hago crecer el dataset
	secciones[i] = f"sec {i}"





