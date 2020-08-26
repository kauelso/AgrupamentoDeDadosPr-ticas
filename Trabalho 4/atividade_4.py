import pandas as pd
import numpy as np
from completar_dados import *

print("Insira abaixo o nome do arquivo que será utilizado, com extensão(exemplo.csv).\nEle deve estar na mesma pasta do programa.")

input_name = input("Nome do arquivo:")
df = pd.read_csv(input_name)

#Removendo colunas que não são numéricas
df.drop(df.select_dtypes(include=[object]), axis=1, inplace=True)
df.dropna(inplace=True)

#Imputando a média nos valores que estão faltando
df.fillna(df.mean(), inplace=True)

output_txt(distancia_todos(df, 1))