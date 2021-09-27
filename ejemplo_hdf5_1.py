from matplotlib.pylab import *
import h5py


A = array([
	[1,2,3],
	[4,5,6],
	[7,8,9],
	], dtype=double)


fid = h5py.File("ejemplo.h5", "w")


fid["A"] = A