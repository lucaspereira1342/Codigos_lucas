import numpy as np
import matplotlib.pyplot as plt 

def calcular_coeficientes(x, y):
    x = np.array(x) - 1
    y = np.array(y)
    
    n = len(x)
    
    # Cálculo dos coeficientes
    a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
    b = (np.sum(y) - a * np.sum(x)) / n
    
    return a, b

log_p = np.array([0.421469, 0.470427, 0.491519, 0.497456, 0.536402, 0.546887, 0.679885, 0.837489, 0.840331, 0.941457, 0.946628, 0.959466, 1.112251, 1.142118, 1.152657, 1.152786, 1.158115, 1.166636, 1.210289, 1.272209, 1.353098, 1.356342, 1.367445, 1.416910, 1.424235, 1.492039, 1.537311, 1.552820, 1.566167, 1.574986, 1.595153, 1.625350, 1.655215, 1.675637, 1.684646, 1.896354])
mag_v = np.array([-2.41, -2.71, -2.53, -2.42, -2.79, -2.63, -3.25, -4.10, -3.06, -3.74, -3.62, -4.29, -4.36, -4.39, -4.69, -4.17, -4.14, -4.41, -4.50, -4.72, -4.82, -5.06, -5.11, -5.08, -4.77, -5.71, -5.87, -5.55, -5.27, -5.75, -5.90, -5.95, -5.21, -6.32, -6.02, -6.18])

coef_a, coef_b = calcular_coeficientes(log_p, mag_v)

print(f"Coeficiente a: {coef_a}")
print(f"Coeficiente b: {coef_b}")

plt.figure()
plt.scatter(log_p, mag_v)
plt.show()
