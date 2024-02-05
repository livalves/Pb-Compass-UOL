import pandas as pd 

actors = pd.read_csv("./actors.csv", encoding="UTF-8", sep=",")
indice = actors['Number of Movies'].idxmax()

nome = actors.loc[indice, 'Actor']
maior = actors.loc[indice, 'Number of Movies']

print(f"O ator/atriz com maior número de filmes é {nome} com {maior} filmes")
