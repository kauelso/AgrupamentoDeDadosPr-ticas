import pandas as pd
import random
import numpy as np
from funcoes import *
from statistics import mean

 
df = pd.read_csv("iris.csv")

k = int(input("Numero de centroides: "))

grupos = KMeans(k, df, max_interacao=100)

output_txt(grupos)