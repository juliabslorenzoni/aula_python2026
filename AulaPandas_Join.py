import pandas as pd

clientes = pd.DataFrame({"nome": ["Ana", "Bruno", "Carlos"]})

cidades = pd.DataFrame({"valor":["vix","vv","serra"]})

df = clientes.join(cidades, how="inner")
print(df)