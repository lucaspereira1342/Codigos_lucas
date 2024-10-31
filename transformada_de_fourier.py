import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as stl
import scipy.fftpack as sci
stl.use('ggplot')

tempo = np.linspace(0, 10, 500)
sinal = np.sin(3*np.pi*tempo)

ruido = np.random.normal(0, 1, tempo.shape)
sinal_ruidoso = sinal + ruido

dominio_da_frequencia = sci.fft(sinal_ruidoso)

PSD = dominio_da_frequencia*np.conjugate(dominio_da_frequencia)/len(dominio_da_frequencia) #Calcula a Densidade Espectral de Potência (PSD), que mostra como a potência do sinal é distribuída ao longo das frequências, e permite observar em quais frequências o sinal possui maior ou menor potência.

filtro = PSD >=25 #filtro dos valores da PSD (amplitude)
sinal_limpo = PSD*filtro #Sinal com o filtro aplicado

dominio_filtrado = filtro*dominio_da_frequencia #Domínio da frequência com as amplitudes filtradas
inversa = sci.ifft(dominio_filtrado)

plt.figure(figsize=(15, 13))

plt.subplot(3, 2, 1)
plt.xlim(0, 150)
plt.plot(sinal, color='magenta', linewidth=1.5)

plt.subplot(3, 2, 2)
plt.plot(sinal_ruidoso, color='green', linewidth=1.5)
plt.plot(sinal, color='magenta', linewidth=1.5)

plt.subplot(3, 2, 3)
plt.plot(dominio_da_frequencia, color='navy', linewidth=1.5)

plt.subplot(3, 2, 4)
plt.plot(PSD, color='black', linewidth=1.5)

plt.subplot(3, 2, 5)
plt.plot(sinal_limpo, color='blue', linewidth=1.5)

plt.subplot(3, 2, 6)
plt.xlim(0, 150)
plt.plot(inversa, color='yellow', linewidth=1.5)

plt.show()

vetor_sinal_limpo = abs(sinal_limpo)
frequencia = np.fft.fftfreq(len(sinal_limpo), d=1/fs)

amplitude = np.amax(vetor_sinal_limpo)
valor_amplitude = np.argmax(vetor_sinal_limpo)
valores = np.where(vetor_sinal_limpo == amplitude)[0]
print(valores)
#omega = vetor_frequencia[amplitude]

#print(vetor_sinal_limpo)
print('Amplitude:', amplitude)
print("Frequências:", np.where(frequencia >=0))

#plt.plot(omega, amplitude)
#plt.show()

print("Frequências:", omega)
print("Amplitudes PSD:", amplitude)
