import numpy as np
import scipy.constants as sci

comprimento = np.array([3737, 4260, 5010, 6990, 8660])
a_0 = np.array([0.1435, 0.1754, 0.2593, 0.4128, 0.5141])
a_1 = np.array([0.9481, 0.9740, 0.8724, 0.7525, 0.6497])
a_2 = np.array([-0.0920, -0.1525, -0.1336, -0.1761, -0.1657])
I_0 = np.array([42.0e13, 44.9e13, 40.3e13, 25.0e13, 15.5e13])
theta = np.array([0, 30, 45, 60, 90])

def temperatura(l, angulo, i, a, b, c):
    angulo_rad = np.radians(angulo)
    boltzmann = sci.k*1e07
    planck = sci.Planck*1e07
    velocidade_luz = sci.c*1e02
    Ang = comprimento*1e-08
    temperatura = ((sci.Planck*sci.c)/(l*sci.k))*(1/(np.log(((2*sci.Planck*sci.c*i)/(l*(a + b*np.cos(angulo_rad)+2*c*np.cos(angulo_rad)**2)))+1)))
    return temperatura

print(temperatura(comprimento, theta, I_0, a_0, a_1, a_2))
