import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('exo_limpios.csv')
sns.scatterplot(data=df, x='pl_bmasse', y='pl_rade',hue='discoverymethod')
plt.xscale('log')
plt.xlabel('Masa')
plt.yscale('log')
plt.ylabel('Radio')
plt.title('Gráfico Radio VS Masa')
plt.savefig('radio_vs_masa.png')
