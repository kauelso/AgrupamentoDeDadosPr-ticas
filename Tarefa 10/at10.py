import pandas as pd
import numpy as np
import sys
import math
from completar_dados import *

# print(
#     "Insira abaixo o nome do arquivo que será utilizado, com extensão(exemplo.csv).\nEle deve estar na mesma pasta do programa."
# )

# input_name = input("Nome do arquivo: ")
# try:
#     df = pd.read_csv(input_name)
# except:
#     print("Arquivo não é um csv ou não foi encontrado")
#     sys.exit()

df = pd.read_csv("teste.csv")

#Computar a primeira matriz (pronto)
matriz = distancia_todos(df)


# print(matriz)
#Encontrar menor valor (pronto)
indice_menor_valor = np.unravel_index(np.nanargmin(matriz, axis=None), matriz.shape)
ind2 = indice_menor_valor[0]
ind1 = indice_menor_valor[1]
#Unir os grupos do menor valor
for i in matriz.columns:
    minimo = min(matriz.iloc[ind1][i],matriz.iloc[ind2][i])
    if ind1 < ind2:
        matriz.iloc[ind1][i] = minimo
        matriz.iloc[i][ind1] = minimo
    else:
        matriz.iloc[ind2][i] = minimo
        matriz.iloc[i][ind2] = minimo
#Atualizar a matriz
if ind1 < ind2:
    matriz.drop([ind2],axis=1,inplace=True)
    matriz.drop([ind2],axis=0,inplace=True)
else:
    matriz.drop([ind1],axis=1,inplace=True)
    matriz.drop([ind1],axis=0,inplace=True)
#     matriz.drop(matriz.columns[ind2], inplace=True)
# else:
#     matriz.drop(matriz.index[ind1], inplace=True)
#     matriz.drop(matriz.columns[ind1], inplace=True)
print(matriz)
#Encerrrar somente quando houver apenas um grupo

#Gerar output
