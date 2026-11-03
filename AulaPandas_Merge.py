#inner: só mostra o que está em comum nas duas
#left: pega o q esta na tabela da esquerda e tenta encontrar na tabela direita
#right: pega o que esta na tabela direita e tenta encontrar na tabela esquerda
#outer: junta todos
import pandas as pd

clientes = pd.DataFrame({"id": [1,2,3], "nome": ["Ana", "Bruno", "Carlos"]})

pedidos = pd.DataFrame({"id":[1,2,2,4], "valor":[100,200,300,400]})

df = pd.merge(clientes, pedidos, on="id", how="outer")
print(df)
