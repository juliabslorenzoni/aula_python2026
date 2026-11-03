#concat: empilha tabelas uma em cima da outra
import pandas as pd

clientes = pd.DataFrame({"nome": ["Ana", "Bruno", "Carlos"]})

cidades = pd.DataFrame({"valor":["vix","vv","serra"]})

df = pd.concat([cidades,clientes],axis=1)
print(df)