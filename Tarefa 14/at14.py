import pandas as pd
import random
from funcoes import *
import sys
import numpy as np
from statistics import mean
from sklearn.cluster import KMeans

print("Insira abaixo o nome do arquivo que será utilizado, com extensão(exemplo.csv).\nEle deve estar na mesma pasta do programa.")

input_name = input("Nome do arquivo:")
try:
    df = pd.read_csv(input_name)
except:
    print("Arquivo não é um csv ou não foi encontrado")
    sys.exit()

frases = []

for k in range(2,5):
  # Convert DataFrame to matrix
  df_aux = df.copy()
  df_aux.drop(["variety"],axis=1,inplace= True)
  mat = df_aux.values
  # Using sklearn
  km = KMeans(n_clusters=k, max_iter=100)
  km.fit(mat)
  # Get cluster assignment labels
  labels = km.labels_
  # Format results as a DataFrame
  df["cluster"] = labels

  count = df.groupby(["cluster","variety"]).count()
  count = count['sepal.length']
  count = pd.DataFrame(count)
  count.columns = ['quantidade']
  count.reset_index(inplace=True)
  
  resultado = pureza_total(count)

  frase = f'Para o k-means com k = {k} a pureza total foi de: {resultado}'

  frases.append(frase)

  grava_arquivo(frases)
