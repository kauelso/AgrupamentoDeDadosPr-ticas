import pandas as pd
import numpy as np
from completar_dados import *

input_name = "iris.csv"
df = pd.read_csv(input_name)

#df.info()

#df.head()

#Removendo colunas que não são numéricas
df.drop(df.select_dtypes(include=[object]), axis=1, inplace=True)
df.dropna(inplace=True)

#df.info()

#Criando uma lista que contém as somas totais de cada coluna do conjunto de dados
#e substituindo os valores marcados com "?" por NaN
somas = []

for (nome_col, dados_col) in df.iteritems():
  soma = 0
  for (index, valor) in zip(df[nome_col].index, df[nome_col]):
    if dados_col[index] == "?":
      df[nome_col][index] = np.nan
    else:
      if not isinstance(valor, str):
        valor = float(valor)
        soma += valor
  somas.append(soma)

for i, (nome_col, dados_col) in enumerate(df.iteritems()):
  for (index, valor) in zip(df[nome_col].index, df[nome_col]):
    if dados_col[index] is np.nan:
      if somas[i] == 0:
        df[nome_col][index] = valor_mais_frequente(df, nome_col)

distancia_todos(df, 1)