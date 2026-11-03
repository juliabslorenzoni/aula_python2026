import pandas as pd

arquivo = pd.read_excel(r"C:\Users\julia\OneDrive\Desktop\JULIA\LINGUAGENS DE PROGRAMAÇÃO\dados_unificados.xlsx")
print(arquivo.columns)
print(arquivo[arquivo["População 2022"]<10000][["Municipio", "População 2022"]])

arquivo["Superavit"] = arquivo ["Total de receitas brutas 2024"] - arquivo["Total de despesas brutas 2024"]
print(arquivo.columns)

arquivo["Mortalidade infantil 2023"] = arquivo["Mortalidade infantil 2023"].apply(pd.to_numeric, errors="coerce")
print(arquivo[["População 2022", "Mortalidade infantil 2023"]].describe().round(2).T)