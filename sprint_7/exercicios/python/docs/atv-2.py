import pandas as pd 
import numpy as np

actors = pd.read_csv("./actors.csv", encoding="UTF-8", sep=",")

media = np.average(actors['Number of Movies'])

print(f"A média do número de filmes é {media}")
