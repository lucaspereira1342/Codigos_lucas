import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as stl
import scipy.fftpack as sci
stl.use('ggplot')

N = 500
fs = 1/50

tempo = np.linspace(0, N*fs, N, endpoint=False)
sinal = np.sin(3*np.pi*tempo)

ruido = np.random.normal(0, 1, tempo.shape)
sinal_ruidoso = sinal + ruido

plt.figure(figsize=(15, 13))

plt.subplot(2, 1, 1)
plt.plot(tempo, sinal, color='magenta', linewidth=1.5)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal')

plt.subplot(2, 1, 2)
plt.plot(tempo, sinal_ruidoso, color='green', linewidth=1.5, label='Ruido')
plt.plot(tempo, sinal, color='magenta', linewidth=1.5, label='Sinal')
plt.legend()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal e Ruido')
plt.show()

transformada = sci.fft(sinal_ruidoso)
frequencia = sci.fftfreq(N, fs)[:N//2] #Frequências associadas a transformada de Fourier, considerando apenas a metade positiva.

phi = np.angle(transformada)
transformada_em_fase = np.abs(transformada)*np.exp(1j*phi)

sinal_limpo = np.where(np.abs(transformada_em_fase) >= 100, transformada_em_fase, 0) # Aplica o filtro na transformada em fase, zerando valores com amplitude menor que 100

amplitude_positiva = 2/N*transformada_em_fase[0:N//2] #Amplitude das frequências positivas
amplitude_positiva_limpo =  2/N * np.abs(sinal_limpo[0:N//2]) #Aplitudes positivas com o sinal limpo

plt.figure(figsize=(15, 13))

plt.subplot(3, 1, 1)
plt.plot(np.abs(transformada_em_fase), color='black', linewidth=1.5)
plt.plot
plt.subplot(3, 1, 2)
plt.plot(frequencia , np.abs(amplitude_positiva), color='navy', linewidth=1.5)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 3)
plt.plot(frequencia, amplitude_positiva_limpo, color='blue', linewidth=1.5)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')

plt.show()

inversa = sci.ifft(sinal_limpo)

plt.figure(figsize=(6, 4))
plt.plot(tempo, np.real(inversa), color='red', linewidth=1.5)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Transformada Inversa')
plt.show()

amplitude = np.amax(amplitude_positiva_limpo) #Valor máximo da amplitude
amp_max = np.argmax(amplitude_positiva_limpo) #posição no array onde a amplitude é maxima
omega = frequencia[amp_max] #valor da frequência onde a amplitude é máxima

print('Amplitude:', amplitude)
print("Frequências:", omega)

fase = np.angle(inversa[amp_max], deg=False)
print('Fase', fase)

nova_funcao = amplitude*np.sin(2*np.pi*(omega*tempo + fase))

plt.figure(figsize=(12, 10))
plt.subplot(2, 1, 1)
plt.plot(tempo, nova_funcao, color='orange',linewidth=1.5, label='Nova função')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(tempo, sinal, color='b', linewidth=1.5, label='Função original')
plt.legend()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()
