import pandas as pd
import numpy as np


def distancia(obj1, obj2):

    lista = []

    for (valor1, valor2) in zip(obj1, obj2):
        resultado = abs(valor1 - valor2) ** 2
        lista.append(resultado)

    resultado = sum(lista)
    resultado = resultado ** (1 / 2)

    return round(resultado, 2)


def distancia_todos(df):
    listas = []
    for i, (nome_col, dados_row) in enumerate(df.iterrows()):
        lista = dados_row.values.tolist()
        listas.append(lista)

    resultado = []
    for i, l1 in enumerate(listas):
        r = []
        for j, l2 in enumerate(listas):
            result = distancia(l1, l2)
            if result == 0.0:
              result = np.nan
            r.append(result)
        resultado.append(r)
    resultado = pd.DataFrame(resultado)
    
    return resultado

def cols_agrup(matriz, indice_menor_valor):
  cols = []
  ind1, ind2 = matriz.columns[indice_menor_valor[0]], matriz.columns[indice_menor_valor[1]]
  for col in matriz.columns:
    if col == ind1:
      cols.append(str(ind1)+','+str(ind2))
      continue
    if col == ind2:
      continue
    cols.append(col)
  return cols


def acha_pos_min(matriz):

    # Retira listas vazias, caso houver
    matriz_sem_vazio = [x for x in matriz if x != []]

    # Dicionário que conterá o menor valor de cada linha
    minimo = {}

    for i, l1 in enumerate(matriz_sem_vazio):
        linha = i
        coluna = l1.index(min(l1))
        menor_valor_cada_linha = min(l1)

        # Se algum valor se repetir, pegamos o primeiro que aparece
        if menor_valor_cada_linha not in minimo:
            minimo[menor_valor_cada_linha] = [linha, coluna]

    # Achando o mínimo dos minimos
    chave = min(minimo.keys())
    minn = minimo[chave]

    return minn

def single_link(matriz):
    indice_menor_valor = np.unravel_index(np.nanargmin(matriz, axis=None), matriz.shape)
    ind1 = indice_menor_valor[1]
    ind2 = indice_menor_valor[0]
    #Unir os grupos do menor valor
    for i,c in enumerate(matriz.columns):
        minimo = min(matriz.iloc[ind1][c],matriz.iloc[ind2][c])
        if ind1 < ind2:
            matriz.iloc[ind1][c] = minimo
            matriz.iloc[i][matriz.columns[ind1]] = minimo
        else:
            matriz.iloc[ind2][c] = minimo
            matriz.iloc[i][matriz.columns[ind2]] = minimo
    #Atualizar a matriz
    if ind1 < ind2:
        matriz.iloc[ind1][ind1] = float('nan')
        matriz.rename(columns = {matriz.columns[ind1]: str(matriz.columns[ind1])+","+str(matriz.columns[ind2])},inplace= True)
        matriz.rename(index = {matriz.index[ind1]: str(matriz.index[ind1])+","+str(matriz.index[ind2])},inplace = True)
        matriz.drop([matriz.index[ind2]],axis=0,inplace=True)
        matriz.drop([matriz.columns[ind2]],axis=1,inplace=True)
    else:
        matriz.iloc[ind2][ind2] = float('nan')
        matriz.rename(columns = {matriz.columns[ind2]: str(matriz.columns[ind2])+","+str(matriz.columns[ind1])},inplace= True)
        matriz.rename(index = {matriz.index[ind2]: str(matriz.index[ind2])+","+str(matriz.index[ind1])},inplace= True)
        matriz.drop([matriz.index[ind1]],axis=0,inplace=True)
        matriz.drop([matriz.columns[ind1]],axis=1,inplace=True)


def output_txt(listas):
    f = open("output.txt", "w")
    for lista in listas:
        f.write(str(lista[0]))
        for i in lista[1:]:
            f.write("," + str(i))
        f.write("\n")
    f.close()
