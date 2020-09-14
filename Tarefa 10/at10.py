import pandas as pd
import numpy as np
import sys
from completar_dados import *

print(
    "Insira abaixo o nome do arquivo que será utilizado, com extensão(exemplo.csv).\nEle deve estar na mesma pasta do programa."
)

input_name = input("Nome do arquivo: ")
try:
    df = pd.read_csv(input_name)
except:
    print("Arquivo não é um csv ou não foi encontrado")
    sys.exit()

#Computar a primeira matriz (pronto)

#Encontrar menor valor (pronto)

#Unir os grupos do menor valor

#Atualizar a matriz

#Encerrrar somente quando houver apenas um grupo

#Gerar output


# Imputando a média nos valores que estão faltando
df.fillna(df.mean(), inplace=True)

# print(acha_pos_min(distancia_todos(df)))
print(acha_pos_min(distancia_todos(df)))