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
print(matriz)
while len(matriz) != 1:
    single_link(matriz)
    print(matriz)


#Encerrrar somente quando houver apenas um grupo

#Gerar output
