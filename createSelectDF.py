import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#criando array com np
dados = np.arange(8)
#Reorganizando o array
dados.reshape((4, 2))

indice = ['linha1', 'linha2', 'linha3', 'linha4',
          'linha5', 'linha6', 'linha7', 'linha8', ]

#Organizando as series
serie = Series(dados, index= indice)
#print(serie['linha6'])

#Criando dataFrame
np.random.seed(25)
indice = ['linha1', 'linha2', 'linha3',
          'linha4', 'linha5', 'linha6']
colunas = ['coluna1', 'coluna2', 'coluna3',
           'coluna4', 'coluna5', 'coluna6' ]

df = DataFrame(np.random.rand(36).reshape((6, 6)),
               index=indice, columns=colunas)

#Selecionar Linhas e colunas no DF
selectLinesColumns = df.loc[['linha1', 'linha4'], ['coluna2', 'coluna3']]
selectFor= serie['linha2': 'linha7']
print("Linhas e colunas: \n", selectLinesColumns)
print('\n')
print("De linha à linha: \n", selectFor)




