import pandas as pd
import numpy as np
from pandas import DataFrame

dados = {
    'coluna1': [1, 1, 2, 2, 3, 3, 3],
    'coluna2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'coluna3': ['D', 'A', 'B', 'B', 'C', 'C', 'C'],
}
#verificarDuplicados e Remover Duplicados(LINHAS)
df = DataFrame(dados)
#verificar = df.duplicated()
removerDuplos = df.drop_duplicates(['coluna3']) #verificar se os valores estão realmente duplicados


print(removerDuplos)