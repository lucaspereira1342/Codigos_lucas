import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.array([948.75, 1104.27, 1168.21, 1558.41, 1707.71])
y = np.array([1146.11, 845.44, 883.46, 598.96, 608.911])
RA_grau = np.array([275.33151176, 275.36081429, 275.35725221, 275.38541670, 275.38460068])
dec = np.array([-18.19257361, -18.1787021, -18.17197011, -18.13613816, -18.12220953])

RA_arcs = RA_grau*3600

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


RA_pluto = (a * 955 + b * 1185 + c)/15
dec_pluto = (d * 955 + e * 1185 + f)

def segundos_para_hora (seg):
    horas = seg // 3600
    minutos = (seg % 3600) // 60
    segundos = seg % 60

    return f"{horas}:{minutos}:{segundos}"


print(f"A ascensão reta de plutão é: {segundos_para_hora(RA_pluto)} e a declinação é {dec_pluto}")
