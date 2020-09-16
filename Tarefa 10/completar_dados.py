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
            if result == 0:
              result = np.nan
            r.append(result)
        resultado.append(r)

    resultado = pd.DataFrame(resultado)
    resultado = resultado[:-1]
    
    return resultado


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


def output_txt(listas):
    f = open("output.txt", "w")
    for lista in listas:
        f.write(str(lista[0]))
        for i in lista[1:]:
            f.write("," + str(i))
        f.write("\n")
    f.close()
