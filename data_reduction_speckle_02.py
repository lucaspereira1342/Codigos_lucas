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
plt.imshow(shift_fft, cmap='gray')
plt.colorbar()

def fluxo_maximo(img):
    flux_max = np.amax(img)
    y_max, x_max = np.unravel_index(np.argmax(shift_fft), shift_fft.shape) # Encontra as coordenadas do máximo
    return flux_max, (x_max, y_max)

def fluxo_secundário(img, num_picos):
    max_pos = np.unravel_index(np.argmax(shift_fft), shift_fft.shape)
    magnitude_no_max = shift_fft.copy() # Gera uma máscara para o código abaixo zerar o pico central
    magnitude_no_max[max_pos] = 0  # Zerar o pico principal
    filtered = maximum_filter(magnitude_no_max, size=10)  # Encontra as regiões de máximo local
    peaks = (magnitude_no_max == filtered)  # Gera uma matriz booleana com os máximos locais
    fluxo = img[peaks]
    y_coord, x_coord = np.where(peaks)
    indices = np.argsort(fluxo)[::-1] # Ordena os valores do fluxo em ordem crescente
    picos_ordenados = list(zip(fluxo[indices], x_coord[indices], y_coord[indices]))

    return picos_ordenados[:num_picos]

fluxo_max, (x_max, y_max) = fluxo_maximo(shift_fft)
picos_secundários = fluxo_secundário(shift_fft, 2)

print(f"Fluxo máximo: {fluxo_max}")
print(f"Posição do pico: (x={x_max}, y={y_max})")

print("Fluxos e posições dos principais picos:")
for i, (fluxo, x, y) in enumerate(picos_secundários):
    print(f"Pico {i+1}: Fluxo = {fluxo}, Posição = (x={x}, y={y})")

plt.figure(figsize=(6,6))
plt.imshow(shift_fft, cmap='gray', origin='upper')
plt.colorbar(label="Intensidade de brilho")
plt.scatter(x_max, y_max, color='red', marker='x', label=f"Máx: {fluxo_max:.2f}")
plt.imshow(shift_fft, cmap='gray', origin='upper')
for fluxo, x, y in picos_secundários:
    plt.scatter(x, y, color='blue', marker='x', label=f"Fluxo: {fluxo:.2f}")
plt.title("Imagem com Picos de Fluxo Destacados")
plt.show()
 
altura, largura = signal.shape[:2]

centro_x = largura/2
centro_y = altura/2

print(f'As coordenadas do centro da imagem são ({centro_x}, {centro_y})')

def distancia(x_c, y_c, x, y):
    d_x = x - x_c
    d_y = y - y_c
    d = np.sqrt((d_x**2) + (d_y)**2)
    return d

print(distancia(130, 140, 136, 134))
