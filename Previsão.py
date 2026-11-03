from sklearn.linear_model import LinearRegression
import numpy as np

gastos = np.array([2.0,2.4,1.5,3.5,3.5,3.5,3.7,3.7])
vendas = np.array([196,221,136,255,244,230,232,267])

modelo = LinearRegression()
modelo.fit(gastos.reshape(-1,1),vendas)

previsao = modelo.predict([[4.0]])
print(previsao)