import pandas as pd
import numpy as np

def valor_mais_frequente(df, nome_col):
  dic = {n: 0 for n in df[nome_col].unique()}
  
  for index, valor in df[nome_col].items():
    for n in dic:
      if n == valor:
        dic[n] +=1

  valor = sorted(dic.items(), reverse=True, key=itemgetter(1))[0][0]
  return valor

def distancia(obj1, obj2, dist=1):
#  if dist != 1 and dist != 2:
#    return 'Somente as distâncias 1 (euclediana) e 2 (manhattan) estão disponíveis!'
  
  lista = []

  for (valor1, valor2) in zip(obj1, obj2):
    resultado = abs(valor1 - valor2) ** int(dist)
    lista.append(resultado)

  resultado = sum(lista)
  resultado = resultado ** (1/int(dist))

  return round(resultado, 2)

def distancia_todos(df, dist=1):
  f = open("output.txt", "w")
  if dist != 1 and dist != 2:
    return 'Somente as distâncias 1 (euclediana) e 2 (manhattan) estão disponíveis!'
    
  listas = []
  for i, (nome_col, dados_row) in enumerate(df.iterrows()):
    lista = (dados_row.values.tolist())
    listas.append(lista)

  resultado = []
  for i, l1 in enumerate(listas):
    r = []
    for j, l2 in enumerate(listas):
      result = distancia(l1, l2, dist)
      r.append(result)
      f.write(str(result))
      if listas.index(l2) < len(listas)-1:
        f.write(",")
    f.write("\n")
    resultado.append(r)
  f.close()
  return resultado