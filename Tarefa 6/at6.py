import pandas as pd
import random
import numpy as np
from funcoes import *

 
df = pd.read_csv("iris.csv")

# Retira a ultima coluna da base de dados
df = df[df.columns[:-1]]

#df.head()

k = input("Numero de centroides: ")

np.random.seed(200)

for i in range(df.shape[0]):
  distancias = []
  inter =[]
  for m in centroides(k, data):
    dist = distancia(df.iloc[i], df.iloc[m])
    inter.append(dist)
    valor_min = min(inter)
  distancias.append(valor_min)
  print(distancias)

centros = centroides(k,data)

print(centros)