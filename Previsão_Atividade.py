import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

dados = pd.read_excel(r"C:\Users\julia\Downloads\data.xlsx")

x1 = dados['Feature1'].values
x2 = dados['Feature2'].values
y = dados['Target'].values

X = np.column_stack([x1,x2])

modelo = LinearRegression()
modelo.fit(X, y)

previsao = modelo.predict([[2.4,0.6]])
print(previsao)