import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as stl
import scipy.fftpack as sci
stl.use('ggplot')

N = 500
T = 1/50

tempo = np.linspace(0, N*T, N, endpoint=False)
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

dominio_da_frequencia = np.abs(sci.fft(sinal_ruidoso))
frequencia = sci.fftfreq(N, T)[:N//2] #Frequências associadas a transformada de Fourier, considerando apenas a metade positiva.


filtro = dominio_da_frequencia >=100 #filtro dos valores da amplitude
sinal_limpo = dominio_da_frequencia*filtro #Sinal com o filtro aplicado
amplitude_freq =  2/N*sinal_limpo[0:N//2] #Amplitude das frequências positivas

plt.figure(figsize=(15, 13))

plt.subplot(3, 1, 1)
plt.plot(frequencia , 2/N*dominio_da_frequencia[0:N//2], color='navy', linewidth=1.5)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 2)
plt.plot(frequencia, amplitude_freq, color='blue', linewidth=1.5)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')

plt.show()

dominio_filtrado = filtro*dominio_da_frequencia #Domínio da frequência com as amplitudes filtradas
inversa = sci.ifft(dominio_filtrado)

plt.figure(figsize=(6, 4))
plt.plot(tempo, np.real(inversa), color='red', linewidth=1.5)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Transformada Inversa')
plt.show()

amplitude = np.amax(amplitude_freq) #Valor máximo da amplitude
amp_max = np.argmax(amplitude_freq) #posição no array onde a amplitude é maxima
omega = frequencia[amp_max] #valor da frequência onde a amplitude é máxima

print('Amplitude:', amplitude)
print("Frequências:", omega)

nova_funcao = amplitude*np.sin(2*np.pi*omega*tempo)

plt.plot(tempo, nova_funcao, color='orange',linewidth=1.5, label='Nova Função')
plt.plot(tempo, sinal, color='b', linewidth=1.5, label='Função Original')
plt.legend()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()

phi = np.angle(inversa[amp_max])

nova_funcao = amplitude*np.sin(2*np.pi*(omega*tempo + phi))

plt.plot(tempo, nova_funcao, color='orange',linewidth=1.5, label='Nova Função')
plt.plot(tempo, sinal, color='b', linewidth=1.5, label='Função Original')
plt.legend()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()
