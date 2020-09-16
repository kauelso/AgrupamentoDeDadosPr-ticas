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
matriz = matriz.drop(0,1)
print(matriz)
indice_menor_valor = np.unravel_index(np.nanargmin(matriz, axis=None), matriz.shape)
print(indice_menor_valor)
ind2 = indice_menor_valor[0]
ind1 = indice_menor_valor[1]
#Unir os grupos do menor valor
matriz = list(matriz)
#Atualizar a matriz
print(matriz)
#Encerrrar somente quando houver apenas um grupo

#Gerar output
