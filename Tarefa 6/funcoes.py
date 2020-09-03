import pandas as pd
import numpy as np
import random


def KMeans(k, df, max_interacao):
  centroids = centroides(k, df)
  agrup_ini = agrup_inicial(centroids, df)
  print(agrup_ini)


def centroides(k, data):
  centroides = {}

  for i in range(k):
    valores = []
    for c in df.columns:
      valores.append(round(random.uniform(min(df[c]), max(df[c])),2))

    centroides[i+1] = valores

  return centroides

def distancia(obj1, obj2, dist=2):
  
  lista = []

  for (valor1, valor2) in zip(obj1, obj2):
    resultado = abs(valor1 - valor2) ** int(dist)
    lista.append(resultado)

  resultado = sum(lista)
  resultado = resultado ** (1/int(dist))

  return round(resultado, 2)


def agrup_inicial(centroides, df):
  clusters = {n: 0 for n in range(0,df.shape[0])}
  for i in range(0, df.shape[0]):
    distancias = []
    for e, m in enumerate(centroides):
      dist = distancia(df.iloc[i], df.iloc[m])
      distancias.append(dist)
      if (e+1) == len(centroides):
        menor = min(distancias)
        for b, c in zip(distancias, centroides):
          if menor == b:
            clusters[i] = c
            break
  return clusters


def output_txt(listas):
  f = open("output.txt", "w")
  for lista in listas:
    f.write(str(lista[0]))
    for i in lista[1:]:
      f.write(','+ str(i))
    f.write("\n")
  f.close()

#def percorre(data, centros):
#  lista_dist = []
#  for i, (nome_col, dados_row) in enumerate(data.iteritems()):
#    for centro in enumerate(centros):
#      print(distancia(dados_row, centro, 1))
#      break
  

