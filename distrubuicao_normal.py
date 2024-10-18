import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

media = 100
desvio = np.sqrt(10)
data_points = 8
N = 100000

amostra = np.random.normal(media, desvio, (N, data_points))
media_da_amostra = np.mean(amostra, axis=1)

plt.figure(figsize=[10,8])
sns.histplot(media_da_amostra, bins=50, kde=True)
plt.xlabel('Média da amostra')
plt.ylabel('f(x) densidades')
plt.title('Distribuição da média amostral')

plt.savefig('Questão_1_ATST.png', dpi=300)
