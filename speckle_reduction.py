import numpy as np
from astropy.io import fits
import scipy.fftpack as sci
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter

hdul_dark = fits.open(r"D:\22abr22\16020-1118-I-0075.fits")
header_dark = hdul_dark[0].header
image_dark = hdul_dark[0].data

master_dark = np.mean(image_dark, axis=0)

hdu = fits.PrimaryHDU(master_dark)
hdu.header.add_history("Master Dark calculado como a media de 1000 dark frames.")
hdu.writeto('Master_dark300-0003.fits', overwrite=True)

hdul = fits.open(r"D:\22abr22\16020-1118-V-0073.fits")
info = hdul.info()
header_data = hdul[0].header
image_data = hdul[0].data

num_frames, width, height = image_data.shape

PWS = np.zeros((width, height))

hdul_master_dark = fits.open(r"Master_dark300-0003.fits")
header_master_dark = hdul_master_dark[0].header
image_master_dark = hdul_master_dark[0].data

for i in range(num_frames):
    image = image_data[i] - image_master_dark # Pega a i-ésima imagem

    fft = sci.fft2(image) #Fazendo a transformada bidimensional
    fft_normalized = np.abs(fft) #Pegando os valores absolutos da FFT2
    fft_normalized /= fft_normalized.max() #Normalizando a FFT2 dividindo a FFT2 pelo seu valor máximo
    fft_shifted = sci.fftshift(fft_normalized)

    # Calcular o espectro de potência: |FFT|²
    PWS += fft_shifted ** 2

    # Mostrar progresso
    if i % 100 == 0:
        print(f"Processadas {i}/{num_frames} imagens...")

plt.imshow(np.log10(PWS), cmap='gray')
plt.colorbar()
plt.show()

hdu = fits.PrimaryHDU(PWS)
hdu.writeto('PWS-16020-1118-V-0073.fits', overwrite=True)

hdul_pws_I = fits.open(r"/media/usuario/HD_Lucas/22abr22/PWS/PWS-12415-4858_O-I-0010.fits")  # Mostra informações sobre as extensões do FITS
header_pws_I = hdul_pws_I[0].header
image_pws_I = hdul_pws_I[0].data  # Normalmente a imagem está na primeira extensão

hdul_psf_I = fits.open(r"/media/usuario/HD_Lucas/22abr22/PWS/PWS-12283-6146_O-I-0008.fits")  # Mostra informações sobre as extensões do FITS
header_psf_I = hdul_psf_I[0].header
image_psf_I = hdul_psf_I[0].data  # Normalmente a imagem está na primeira extensão

sci_image_I = image_pws_I / image_psf_I

fft_I = sci.fft2(sci_image_I) #Fazendo a transformada bidimensional
normalized_fft_I = np.abs(fft_I) #Pegando os valores absolutos da FFT2
normalized_fft_I /= normalized_fft_I.max() #Normalizando a FFT2 dividindo a FFT2 pelo seu valor máximo
ACF_I = sci.fftshift(normalized_fft_I)

plt.figure(figsize=(6,6))
plt.title('Função de Autocorrelação')
plt.imshow(ACF_I, cmap='gray')
plt.colorbar()

hdu = fits.PrimaryHDU(ACF_I)
hdu.writeto('ACF.fits', overwrite=True)

hdul_pws_R = fits.open(r"/media/usuario/HD_Lucas/22abr22/PWS/PWS-12415-4858_O-I-0010.fits")  # Mostra informações sobre as extensões do FITS
header_pws_R = hdul_pws_R[0].header
image_pws_R = hdul_pws_R[0].data  # Normalmente a imagem está na primeira extensão

hdul_psf_R = fits.open(r"/media/usuario/HD_Lucas/22abr22/PWS/PWS-12283-6146_O-I-0008.fits")  # Mostra informações sobre as extensões do FITS
header_psf_R = hdul_psf_R[0].header
image_psf_R = hdul_psf_R[0].data  # Normalmente a imagem está na primeira extensão

sci_image_R = image_pws_R / image_psf_R

fft_R = sci.fft2(sci_image_R) #Fazendo a transformada bidimensional
normalized_fft_R = np.abs(fft_R) #Pegando os valores absolutos da FFT2
normalized_fft_R /= normalized_fft_R.max() #Normalizando a FFT2 dividindo a FFT2 pelo seu valor máximo
ACF_R = sci.fftshift(normalized_fft_R)

plt.figure(figsize=(6,6))
plt.title('Função de Autocorrelação')
plt.imshow(ACF_R, cmap='gray')
plt.colorbar()

hdu = fits.PrimaryHDU(ACF_R) 
hdu.writeto('ACF.fits', overwrite=True)

hdul_pws_V = fits.open(r"/media/usuario/HD_Lucas/22abr22/PWS/PWS-12415-4858_O-I-0010.fits")  # Mostra informações sobre as extensões do FITS
header_pws_V = hdul_pws_V[0].header
image_pws_V = hdul_pws_V[0].data  # Normalmente a imagem está na primeira extensão

hdul_psf_V = fits.open(r"/media/usuario/HD_Lucas/22abr22/PWS/PWS-12283-6146_O-I-0008.fits")  # Mostra informações sobre as extensões do FITS
header_psf_V = hdul_psf_V[0].header
image_psf_V = hdul_psf_V[0].data  # Normalmente a imagem está na primeira extensão

sci_image_V = image_pws_V / image_psf_V

fft_V = sci.fft2(sci_image_V) #Fazendo a transformada bidimensional
normalized_fft_V = np.abs(fft_V) #Pegando os valores absolutos da FFT2
normalized_fft_V /= normalized_fft_V.max() #Normalizando a FFT2 dividindo a FFT2 pelo seu valor máximo
ACF_V = sci.fftshift(normalized_fft_V)

plt.figure(figsize=(6,6))
plt.title('Função de Autocorrelação')
plt.imshow(ACF_V, cmap='gray')
plt.colorbar()

hdu = fits.PrimaryHDU(ACF_V)
hdu.writeto('ACF.fits', overwrite=True)

hdul_acf = fits.open(r"/media/usuario/HD_Lucas/22abr22/ACF/ACF-14145-2914-I-0056.fits")  # Mostra informações sobre as extensões do FITS
header_acf = hdul_acf[0].header
image_acf = hdul_acf[0].data  # Normalmente a imagem está na primeira extensão

altura, largura = image_acf.shape

# Cortar a imagem para pegar apenas o primeiro e segundo quadrante (metade superior da imagem)
imagem_quadrantes = image_acf[:altura//2, :largura]


def fluxo_maximo(img):
    flux_max = np.amax(img)
    y_max, x_max = np.unravel_index(np.argmax(img), img.shape) # Encontra as coordenadas do máximo
    return flux_max, (x_max, y_max)

def fluxo_secundário(img, num_picos):
    max_pos = np.unravel_index(np.argmax(img), img.shape)

    magnitude_no_max = img.copy() # Gera uma máscara para o código abaixo zerar o pico central
    magnitude_no_max[max_pos] = 0  # Zerar o pico principal

    filtro = maximum_filter(magnitude_no_max, size=10)  # Encontra as regiões de máximo local
    picos = (magnitude_no_max == filtro)  # Gera uma matriz booleana com os máximos locais
    
    fluxo = img[picos]
    y_coord, x_coord = np.where(picos)
    
    indices = np.argsort(fluxo)[::-1] # Ordena os valores do fluxo em ordem crescente
    fluxos_ordenados = fluxo[indices]  
    posicoes_ordenadas = np.column_stack((x_coord[indices], y_coord[indices])) # Gera um array 2D com os dados das posições dos picos secundários

    return fluxos_ordenados[:num_picos], posicoes_ordenadas[:num_picos]

fluxo_max, (x_max, y_max) = fluxo_maximo(image_acf)
fluxos_sec, posicoes_sec = fluxo_secundário(imagem_quadrantes, 2)

print(f"Fluxo máximo: {fluxo_max}")
print(f"Posição do pico: (x={x_max}, y={y_max})")

print(f"Fluxo dos picos secundários: {fluxos_sec}")
print(f"Posição dos picos secundários  (x, y):{posicoes_sec}")

plt.figure(figsize=(10,10))
plt.imshow(image_acf, cmap='gray', origin='upper')
plt.colorbar(label="Intensidade de brilho")
plt.scatter(x_max, y_max, color='red', marker='x', label=f"Máx: {fluxo_max:.2f}")
plt.imshow(image_acf, cmap='gray', origin='upper')
for i in range(len(fluxos_sec)):
    plt.scatter(posicoes_sec[i, 0], posicoes_sec[i, 1], color='b', marker='x', label=f"Fluxo: {fluxos_sec[i]:.2f}")
plt.legend()
plt.title("Imagem com Picos de Fluxo Destacados")
plt.show()

altura, largura = image_acf.shape[:2]

centro_x = largura/2
centro_y = altura/2

def distancia(x_c, y_c, x, y):
    d_x = x - x_c
    d_y = y - y_c
    d = np.sqrt((d_x**2) + (d_y)**2)
    theta = np.degrees(np.arctan(np.abs(d_y)/d_x))

    return d, theta

def dif_mag(f_1, f_2):
    diferenca_de_magnitude = -2.5*np.log10((f_2/f_1))
    return diferenca_de_magnitude

dis, angulo = distancia(centro_x, centro_y, posicoes_sec[1, 0], posicoes_sec[1, 1])

print(f'A distânica do ponto 1 ao centro da imagem é: {dis}')
print(f'A ângulo da estrela é: {angulo}')
print(f'A diferença de magnitude entre as estrelas principal e secundária é: {dif_mag(fluxo_max, fluxos_sec[1])}')
