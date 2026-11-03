import pandas as pd
import numpy as np

arquivo = pd.read_excel(r"C:\Users\julia\OneDrive\Desktop\JULIA\LINGUAGENS DE PROGRAMAÇÃO\BASE_FINAL.xlsx")

print(arquivo.shape)#1
print(arquivo.columns)#2
print(arquivo.head(5))#3
print(arquivo["Mrg Ebitda"].mean())#4
print(arquivo["RECEITA"].sum())#5
print(arquivo[arquivo["LUCRO LIQUIDO"]>0])#6
print(arquivo.info())
print(arquivo[arquivo["ISE"]>0])#7
arquivo["Margem Operacional"] = arquivo["EBIT"] / arquivo["RECEITA"]#8
print(arquivo.columns)
arquivo["Lucro"] = np.where(arquivo["LUCRO LIQUIDO"]>0,"Lucro", "Prejuizo")#9
print(arquivo["Lucro"])
