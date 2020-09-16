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
print(matriz)
indice_menor_valor = np.unravel_index(np.nanargmin(df, axis=None), df.shape)
print(indice_menor_valor)
#Unir os grupos do menor valor
        
#Atualizar a matriz

#Encerrrar somente quando houver apenas um grupo

#Gerar output


# Imputando a média nos valores que estão faltando
# df.fillna(df.mean(), inplace=True)