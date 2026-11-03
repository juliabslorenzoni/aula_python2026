#print(df.shape) - Mostra quantas linhas e quantas colunas
#print(df.columns) - Mostra os títulos das colunas
#print(df.dtypes) - Mostra o tipo de dado
#print(df.info()) - Mostra o mesmo que o dtypes mas com mais informações
#print(df.head()) - Traz as primeiras linhas (no parêntesis podemos escolher quantas linhas)
#print(df.tail()) - O mesmo que o head, só que as linhas finais
#print(df[["Valor","Quantidade"]]) - Quando há 2+ valores, deve haver 2 []
#print(df.loc[1:2]) - Traz uma linha específica, um valor específico (traz informação do index)
import pandas as pd

data = {"Produto":["Café", "Arroz", "Feijão"],
        "Quantidade":[10, 20, 30],
        "Valor":[45, 15, 10]}
df = pd.DataFrame(data)

print(df.loc[0, "Valor"]) #Traz uma linha específica

