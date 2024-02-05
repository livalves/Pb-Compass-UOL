import pandas as pd 

actors = pd.read_csv("./actors.csv", encoding="UTF-8", sep=",")

contador = actors.groupby(['#1 Movie'])['#1 Movie'].count().reset_index(name='Quantidade').sort_values(['Quantidade', '#1 Movie'], ascending=[False, True]) 

for i, (index, row) in enumerate(contador.iterrows()):
    print(f"{i+1} - O filme {row['#1 Movie']} aparece {row['Quantidade']} vez(es) no dataset")
    