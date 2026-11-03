import pandas as pd

df = pd.DataFrame({
    'Nome': ['Joice', 'Julia', 'Dante'],
    'Nota_1': [10, 10, 10]
})

for linha in df.itertuples():
    print(linha.Nome, linha.Nota_1)







