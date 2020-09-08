import pandas as pd
import numpy as np
from pandas import DataFrame, Series

emBranco = np.nan
np.random.seed(25)
df = DataFrame(np.random.rand(36).reshape(6, 6))
df.loc[3:5, 0] = emBranco
df.loc[1:4, 5] = emBranco

count = df.isnull().sum() #somando valores em branco do DataSet
#Caso passar parametro Axis= 1, o resultado será de um DF sem colunas
drop = df.dropna(axis = 1) #apresentando apenas valores que não estão em branco

print(drop)