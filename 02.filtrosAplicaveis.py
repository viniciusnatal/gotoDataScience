import pandas as pd
import numpy as np
from pandas import DataFrame, Series

np.random.seed(25)
indice = ['linha1', 'linha2', 'linha3',
          'linha4', 'linha5', 'linha6']
colunas = ['coluna1', 'coluna2', 'coluna3',
           'coluna4', 'coluna5', 'coluna6' ]

df = DataFrame(np.random.rand(36).reshape((6, 6)),
               index=indice, columns=colunas)

#listando os valores com condição no DF
comparacao = df < .2

#Criando e organizando série
indice = ['linha1', 'linha2', 'linha3', 'linha4',
          'linha5', 'linha6', 'linha7', 'linha8', ]
serie = Series(np.arange(8), index= indice)
filtro = serie > 4 #Aplicando filtro
apl = serie[filtro]

#Alterando valores na serie
serie['linha1', 'linha2'] = 8

#print(serie)


