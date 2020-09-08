import pandas as pd
import numpy as np
from pandas import DataFrame, Series

#Criando dois DataFrames
df = pd.DataFrame(np.arange(36).reshape(6, 6))
df2 = pd.DataFrame(np.arange(15).reshape(5, 3))

#Coloca as linhas do primeiro objeto, no segundo objeto
#Caso adicionado o axis = 1 considera o indice das linhas
concat = pd.concat([df, df2])

print(concat)