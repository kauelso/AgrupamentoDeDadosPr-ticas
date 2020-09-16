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

df = pd.read_csv("iris.csv")

#Computar a primeira matriz (pronto)
matriz = distancia_todos(df)


# print(matriz)
#Encontrar menor valor (pronto)
print(matriz)
indice_menor_valor = np.unravel_index(np.nanargmin(matriz, axis=None), matriz.shape)
print(indice_menor_valor)
ind1 = indice_menor_valor[0]
ind2 = indice_menor_valor[1]
#Unir os grupos do menor valor
for i,l in enumerate(matriz[ind2]):
    matriz[i][ind2] = min(matriz[i][ind2],matriz[i][ind1])
print(matriz)
#Atualizar a matriz

#Encerrrar somente quando houver apenas um grupo

#Gerar output


# Imputando a média nos valores que estão faltando
# df.fillna(df.mean(), inplace=True)