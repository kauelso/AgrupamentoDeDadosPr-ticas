import pandas as pd
import random
import sys
import numpy as np
from funcoes import *
from statistics import mean
from sklearn.cluster import KMeans

print("Insira abaixo o nome do arquivo que será utilizado, com extensão(exemplo.csv).\nEle deve estar na mesma pasta do programa.")

input_name = input("Nome do arquivo:")
try:
    df = pd.read_csv(input_name)
except:
    print("Arquivo não é um csv ou não foi encontrado")
    sys.exit()

k = int(input("Numero de centroides: "))


# Convert DataFrame to matrix
mat = dataset.values
# Using sklearn
km = KMeans(n_clusters=3, max_iter=100, metric="euclidian")
km.fit(mat)
# Get cluster assignment labels
labels = km.labels_
# Format results as a DataFrame
results = pandas.DataFrame([dataset.index, labels]).T


kmeans = KMeans(n_clusters=3, max_iter=100, metrics="euclidian").fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
