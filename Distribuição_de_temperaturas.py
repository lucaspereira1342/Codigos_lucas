import numpy as np
import scipy.constants as sci
import matplotlib.pyplot as plt

comprimento = np.array([3737, 4260, 5010, 6990, 8660])
a_0 = np.array([0.1435, 0.1754, 0.2593, 0.4128, 0.5141])
a_1 = np.array([0.9481, 0.9740, 0.8724, 0.7525, 0.6497])
a_2 = np.array([-0.0920, -0.1525, -0.1336, -0.1761, -0.1657])
I_0 = np.array([42.0e13, 44.9e13, 40.3e13, 25.0e13, 15.5e13])
theta = np.linspace(0, np.pi/2, 90)

tau = np.cos(theta)


def temperatura(l, angulo, i, a, b, c1):
    bolt = sci.k*1e07
    P = sci.Planck*1e07
    vel_luz = sci.c*1e02
    comp_cm = l*1e-08
    temperatura = P*vel_luz/(comp_cm*bolt)*(1/(np.log(((2*P*vel_luz**2)/((comp_cm**5)*(i)*(a + b*angulo+2*c1*angulo**2)))+1)))
    return temperatura


T_1 = temperatura(comprimento[0], tau, I_0[0], a_0[0], a_1[0], a_2[0])
T_2 = temperatura(comprimento[1], tau, I_0[1], a_0[1], a_1[1], a_2[1])
T_3 = temperatura(comprimento[2], tau, I_0[2], a_0[2], a_1[2], a_2[2])
T_4 = temperatura(comprimento[3], tau, I_0[3], a_0[3], a_1[3], a_2[3])
T_5 = temperatura(comprimento[4], tau, I_0[4], a_0[4], a_1[4], a_2[4])

#print(T_1)
#print(T_2)
#print(T_3)
#print(T_4)

plt.figure(figsize=(10, 8))
plt.plot(tau, T_1, label=r'3737 $\AA$')
plt.plot(tau, T_2, label=r'4260 $\AA$')
plt.plot(tau, T_3, label=r'5010 $\AA$')
plt.plot(tau, T_4, label=r'6990 $\AA$')
plt.plot(tau, T_5, label=r'8660 $\AA$')
plt.title('Temperatura versus Profundidade Óptica')
plt.xlabel(r'$\tau_\lambda$')
plt.ylabel('Temperatura [K]')
plt.legend()
plt.show()

#plt.savefig('Q5_AE.png', dpi=300)
