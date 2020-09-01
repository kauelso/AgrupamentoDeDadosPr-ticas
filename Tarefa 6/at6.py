import pandas as pd
import random
import numpy as np
from funcoes import *

 
df = pd.read_csv("https://raw.githubusercontent.com/johnsigma/meuPortfolio/master/dados/iris.csv")

# Retira a ultima coluna da base de dados
df = df[df.columns[:-1]]

#df.head()

np.random.seed(200)

for i in range(df.shape[0]):
  distancias = []
  inter =[]
  for m in centroides(3, data):
    dist = distancia(df.iloc[i], df.iloc[m])
    inter.append(dist)
    valor_min = min(inter)
  distancias.append(valor_min)
  print(distancias)

centros = centroides(3,data)

print(centros)