# -*- coding: utf-8 -*-
"""Consumo_de_Cerveja_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gVder6zlPJ9YqsiNojF_QbQuhCnOH6ul
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv('consumo_cerveja.csv',sep=';')

df

df.shape # verificar quantidade de dados

df.isna().any()

df.isna().sum()

df.head(8) # lê as primeiras linhas do seu DataFrame

df.describe().round() # describe = dá as principais estatísticas como Min, Max, Média, Count, volumes para cada quartil, round= permite arredondar um número

df.corr().round(4) # corr()é usado para encontrar a correlação de pares de todas as colunas no dataframe.

correlacoes = df.corr().round(2)
correlacoes.to_csv('correlacoes.csv', index=True) # salvar arquivo especifico

fig, ax = plt.subplots(figsize = (20,6)) # subplots são uma forma de exibir vários gráficos em uma única figura

ax.set_title('Consumo de cerveja ao longo de 365 dias', fontsize=14)

ax.set_ylabel('Consumo (litros)', fontsize=14)
ax.set_xlabel('Tempo (dias)', fontsize=14)

ax = df['consumo'].plot(fontsize=14)

from matplotlib import text
ax = sns.boxplot(data=df["consumo"], orient='v', width=0.2)  #verificando somente consumo

ax.figure.set_size_inches(12,6)

ax.set_title('Consumo de cerveja', fontsize = 14)

ax.set_ylabel('Consumo (litros)', fontsize = 14)
text(0,0.5, 'consumo (litros)')

# O boxplot é uma ferramenta útil para identificar valores extremos e assimetrias nos dados, além de permitir a comparação de diferentes conjuntos de dados.
ax = sns.boxplot(data=df, y='consumo', x='fds', orient='v', width=0.5) #

ax.figure.set_size_inches(6,3)

ax.set_title('Consumo de cerveja no final de Semana', fontsize=14)

ax.set_ylabel('Consummo (litros)', fontsize = 14)
ax.set_xlabel('Final de Semana', fontsize = 14)

ax = sns.displot(df['consumo'], kde=True, bins=20)

ax.figure.set_size_inches(6,3)

ax.set(title='Distribuição de Frequencia no consumo de cerveja')

ax.set(ylabel='Consumo (litros)')
ax.set(xlabel='Frequencia')

media_consumo = df['consumo'].mean()
plt.axvline(media_consumo, color='red', linestyle = '--', label=f'media = {media_consumo:.2f}') #matplotlib.pyplot. axvline Adiciona uma linha vertical através dos eixos.
plt.legend() #legend() é usada para colocar uma legenda nos eixos.

ax = sns.pairplot(df, y_vars='consumo', x_vars=['fds', 'temp_max', 'chuva', 'temp_min', 'temp_media']) #Relação do consumo com as demais variaveis, y variavel dependente
ax.fig_subtitle('Disperção entre as variaveis', fontsize = 14, y=1.1 )

ax = sns.lmplot(x='temp_max', y='consumo', data =df)
ax.set_xlabels('Temperatura Máxima', fontsize = 14)
ax.set_ylabels('Tconsumo', fontsize = 14)

ax = sns.lmplot(x='temp_max', y ='consumo', data = df, hue='fds', legend=False)

ax.set_xlabels('Temperatura Máxima', fontsize = 14)
ax.set_ylabels('Tconsumo', fontsize = 14)
ax.set(title='Fim de Semana')

y = df['consumo']
X = df[['temp_max', 'chuva', 'fds']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2811) # x: caracteristica y: rotulo

X_train.shape

X_test.shape

modelo = LinearRegression()

modelo.fit(X_train, y_train) #dados de treino

print ('R2 = {}'.format(modelo.score(X_train, y_train).round(2)))

modelo.intercept_.round(2)

# Calculadora para prever consumo
temp_max = 60
chuva = 0
fds = 1
entrada = [[temp_max, chuva, fds]]

print('{0:.2f} litros'.format(modelo.predict(entrada)[0].round(2))) #predict() retorna uma matriz de previsões para cada instância de dados no conjunto de testes