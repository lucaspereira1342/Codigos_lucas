import imageio
import numpy as np
import scipy.fftpack as sci
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter

signal = imageio.v2.imread('exemplo_01.png', pilmode='L')

fft = sci.fft2(signal) #Fazendo a transformada bidimensional
normalized_fft = np.abs(fft) #Pegando os valores absolutos da FFT2
normalized_fft /= normalized_fft.max() #Normalizando a FFT2 dividindo a FFT2 pelo seu valor máximo
shift_fft = sci.fftshift(normalized_fft)

plt.figure(figsize=(8,8))
plt.title('Função de Autocorrelação')
plt.imshow(shift_fft, cmap='gray', vmax=1)
plt.colorbar()

max_pos = np.unravel_index(np.argmax(shift_fft), shift_fft.shape) # Encontra as coordenadas do máximo

magnitude_no_max = shift_fft.copy() # Gera uma máscara para o código abaixo zerar o pico central
magnitude_no_max[max_pos] = 0  # Zerar o pico principal

# Aplica um filtro de máximo local para encontrar picos secundários
filtered = maximum_filter(magnitude_no_max, size=10)  # Tamanho da vizinhança
peaks = (magnitude_no_max == filtered)  # Matriz booleana de picos

# Obtem as coordenadas dos picos secundários
peaks_indices = np.argwhere(peaks)

# Filtra os picos mais relevantes
num_picos = 2
peak_values = magnitude_no_max[peaks]  # Valores dos picos
top_indices = peaks_indices[np.argsort(peak_values)[-num_picos:]]  # Top picos

# Mostrar o espectro e marcar os picos
plt.figure(figsize=(6,6))
plt.imshow(shift_fft, cmap="gray", vmax=1)
plt.scatter(max_pos[1], max_pos[0], color='red', marker='x', label="Pico Principal")
plt.scatter(top_indices[:,1], top_indices[:,0], color='blue', marker='x', label="Picos Secundários")
#plt.axhline(y = 146, linestyle = '--')
plt.legend()
plt.title("Posição das Estrelas na FFT")
plt.show()

print(f'Coordenadas do pico máximo:')
print(f'({max_pos[1]}, { max_pos[0]})')
print("Coordenadas do picos secundários:")
for y, x in top_indices:
    print(f"({x}, {y})")
