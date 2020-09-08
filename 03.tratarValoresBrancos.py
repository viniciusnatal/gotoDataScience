import numpy as np
import pandas as pd
from pandas import DataFrame, Series

#criando objeto em branco
emBranco = np.nan
serie = Series(['lista1', 'lista2', 'lista3', emBranco, 'lista5', 'lista6', emBranco, emBranco ])
verifBranco= serie.isnull()
#print(verifBranco)

#Criando DF e alterando valores para emBranco
np.random.seed(25)
df = DataFrame(np.random.rand(36).reshape((6, 6)))
df.loc[3:5, 0] = emBranco
df.loc[1:3, 5] = emBranco
df.loc[1:3, 5] = emBranco

#Alterando valores em Branco para zero
dfPreencher = df.fillna(0)

#Preencher em mais de uma linha
dicio = {0: 0.1, 5: 1.25}
dfPreencher = df.fillna(dicio)

print(dfPreencher)