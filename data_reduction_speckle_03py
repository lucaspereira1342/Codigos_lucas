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

    filtro = maximum_filter(magnitude_no_max, size=10)  # Encontra as regiões de máximo local
    picos = (magnitude_no_max == filtro)  # Gera uma matriz booleana com os máximos locais
    
    fluxo = img[picos]
    y_coord, x_coord = np.where(picos)
    
    indices = np.argsort(fluxo)[::-1] # Ordena os valores do fluxo em ordem crescente
    fluxos_ordenados = fluxo[indices]  
    posicoes_ordenadas = np.column_stack((x_coord[indices], y_coord[indices])) # Gera um array 2D com os dados das posições dos picos secundários

    return fluxos_ordenados[:num_picos], posicoes_ordenadas[:num_picos]

fluxo_max, (x_max, y_max) = fluxo_maximo(shift_fft)
fluxos_sec, posicoes_sec = fluxo_secundário(shift_fft, 2)

print(f"Fluxo máximo: {fluxo_max}")
print(f"Posição do pico: (x={x_max}, y={y_max})")

print(f"Fluxo dos picos secundários: {fluxos_sec}")
print(f"Posição dos picos secundários  (x, y):{posicoes_sec}")

plt.figure(figsize=(8,8))
plt.imshow(shift_fft, cmap='gray', origin='upper')
plt.colorbar(label="Intensidade de brilho")
plt.scatter(x_max, y_max, color='red', marker='x', label=f"Máx: {fluxo_max:.2f}")
plt.imshow(shift_fft, cmap='gray', origin='upper')
for i in range(len(fluxos_sec)):
    plt.scatter(posicoes_sec[i, 0], posicoes_sec[i, 1], color='b', marker='x', label=f"Fluxo: {fluxos_sec[i]:.2f}")
plt.legend()
plt.title("Imagem com Picos de Fluxo Destacados")
plt.show()

altura, largura = signal.shape[:2]

centro_x = largura/2
centro_y = altura/2

def distancia(x_c, y_c, x, y):
    d_x = x - x_c
    d_y = y - y_c
    d = np.sqrt((d_x**2) + (d_y)**2)
    return d

def dif_mag(f_1, f_2):
    diferenca_de_magnitude = 2.5*np.log10((f_2/f_1))
    return diferenca_de_magnitude

print(f'A distânica do ponto 1 ao centro da imagem é: {distancia(centro_x, centro_y, posicoes_sec[1, 0], posicoes_sec[1, 1])}')
print(f'A diferença de magnitude entre as estrelas principal e secundária é: {dif_mag(fluxo_max, fluxos_sec[1])}')
