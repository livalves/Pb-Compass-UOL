import pandas as pd 

actors = pd.read_csv("./actors.csv", encoding="UTF-8", sep=",")

indice = actors['Average per Movie'].idxmax()
nome = actors.loc[indice, 'Actor']

print(f"O ator/atriz com maior média por filme é {nome}")