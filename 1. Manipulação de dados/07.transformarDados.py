import pandas as pd
import numpy as np

#DataFrame no pandas
df = pd.DataFrame(np.arange(36).reshape(6, 6))
dropLines = df.drop([0, 2]) #Remover linhas
dropColumns = df.drop([1, 3]) #Remover colunas

#Criando uma série
serie = pd.Series(np.arange(7))
serie.name = 'novaVariavel'

#Gerando objeto resultade DF com concatenação
novoDF = pd.DataFrame.join(df, serie)

#Ordenacao do novoDF, ascending significa se sera crescente ou nao
dfOrdenado = novoDF.sort_values(by= ['novaVariavel'], ascending=[False])
print (dfOrdenado)
