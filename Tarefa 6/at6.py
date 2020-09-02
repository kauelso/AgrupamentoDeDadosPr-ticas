import pandas as pd
import random
import numpy as np
from funcoes import *

 
df = pd.read_csv("iris.csv")

# Retira a ultima coluna da base de dados
df = df[df.columns[:-1]]

#df.head()

<<<<<<< HEAD
k = int(input("Numero de centroides: "))
=======
k = 3 #int(input("Numero de centroides: "))
centroides = centroides(k,df)
for i in range(0,100):
    grupos = []
    centroides_aux = []
    for m in df.values:
        distancias = []
        for n in centroides:
            distancias.append(distancia(m,n))
        menor = min(distancias)
        grupos[distancias.index(menor)] = m
    for grp in range(centroides):
        centroides_aux[grp] = np.mean(grupos[grp])
    if centroides == centroides_aux:
        break
>>>>>>> f0d196ca1362955d79ea2f3239c2b2cd60c500a6

KMeans(k, df, max_interacao=100)




#print(df.iloc[1])
