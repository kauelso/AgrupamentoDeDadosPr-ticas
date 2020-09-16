import pandas as pd
import numpy as np
import sys
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
menor = acha_pos_min(df)
print(matriz)
# ind1 = menor[0]
# ind2 = menor[1]
#Unir os grupos do menor valor
# for i in range(ind1,ind2):
#     print(i)
#     print(matriz[ind1][i])
#     print(matriz[ind2][i])
# matriz.remove(matriz[ind1])
# print(matriz)
        
#Atualizar a matriz

#Encerrrar somente quando houver apenas um grupo

#Gerar output


# Imputando a média nos valores que estão faltando
# df.fillna(df.mean(), inplace=True)

# print(acha_pos_min(distancia_todos(df)))
# print(distancia_todos(df))
# print(cols_agrup(df,menor))