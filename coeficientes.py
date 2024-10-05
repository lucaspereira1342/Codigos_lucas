import numpy as np

def alfa_final (dec, alfa_i, m_0):
    angulo_radiano = np.radians(dec)
    mi_final = (2.8e-6 * m_0)/(np.cos(angulo_radiano) * 3600)
    alfa = alfa_i + mi_final * (2010.33 - 2000)

    return alfa


alfa_0 = np.array([275.33154738349805, 275.3609877860729, 275.3572577459368, 275.3853555258372, 275.38449726593615])
dec_0 = np.array([-18.19252038370346, -18.177972042098627, -18.172032489573315, -18.13608008826267, -18.121985603456988])
mi_0 = np.array([-1.1701096732618081, -5.698867522971696, -0.18189270469863025, 2.0098439224647, 3.3980514163793547])

print(alfa_final(dec_0, alfa_0, mi_0))
