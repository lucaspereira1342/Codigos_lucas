import numpy as np

fluxo = np.array([331564, 691005, 794387, 319817])
mag = np.array([13.919, 13.118, 12.955, 13.941])

m0 = mag + 2.5*np.log10(fluxo)
print(m0)

k = round(np.mean(m0), 3)
print(k)

desvio = np.std(m0)
print(desvio)

m_pluto = k - 2.5*np.log10(303893)
print(m_pluto)
