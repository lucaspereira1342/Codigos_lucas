import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.array([948.75, 1104.27, 1168.21, 1558.41, 1707.71])
y = np.array([1146.11, 845.44, 883.46, 598.96, 608.911])
RA_t = np.array([66079.568, 66086.6051, 66085.7285, 66092.4792, 66092.2717])
dec = np.array([-65493.705, -65441.064, -65420.702, -65289.411, -65239.448])

RA_arcs = RA_t*15

A = np.vstack([x, y, np.ones(len(x))]).T

a, b, c = np.linalg.lstsq(A, RA_arcs, rcond=None)[0]
d, e, f = np.linalg.lstsq(A, dec, rcond=None)[0]

print(f"Coeficiente a: {a}")
print(f"Coeficiente b: {b}")
print(f"Coeficiente c: {c}")
print(f"Coeficiente d: {d}")
print(f"Coeficiente e: {e}")
print(f"Coeficiente f: {f}")

d_fit = a * x + b * y + c,
d_fit = d * x + e * y + f,


RA_pluto = round((a * 955 + b * 1185 + c)/15, 3)
dec_pluto = round((d * 955 + e * 1185 + f), 3)

print(f"A ascensão reta de plutão é: {RA_pluto} e a declinação é {dec_pluto}")
