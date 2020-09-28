import pandas as pandas
import random
import sys
import numpy as np
from funcoes import *
from statistics import mean
from sklearn.cluster import KMeans

print("Insira abaixo o nome do arquivo que será utilizado, com extensão(exemplo.csv).\nEle deve estar na mesma pasta do programa.")

# input_name = input("Nome do arquivo:")
# try:
#     df = pd.read_csv(input_name)
# except:
#     print("Arquivo não é um csv ou não foi encontrado")
#     sys.exit()
df = pd.read_csv("iris_com_classe.csv")

k = int(input("Numero de centroides: "))


# Convert DataFrame to matrix
df_aux = df.copy()
df_aux.drop(["variety"],axis=1,inplace= True)
mat = df_aux.values
# Using sklearn
km = KMeans(n_clusters=k, max_iter=100)
km.fit(mat)
# Get cluster assignment labels
labels = km.labels_
# Format results as a DataFrame
df["cluster"] = labels
print(df)
