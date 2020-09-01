import pandas as pd
import random
import numpy as np
from funcoes import *

 
df = pd.read_csv("iris.csv")

# Retira a ultima coluna da base de dados
df = df[df.columns[:-1]]

#df.head()

k = 3 #int(input("Numero de centroides: "))


print(df.iloc[1])
