from matplotlib.pylab import *
import h5py

fid = h5py.File("ejemplo.h5", "r")



A = fid["A"][:, 1]

print(A)