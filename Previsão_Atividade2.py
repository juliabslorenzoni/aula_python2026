import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets
from sklearn.model_selection import train_test_split

dados = datasets.load_diabetes()

#dividir em treino e teste
x_train, x_test, y_train, y_test = train_test_split(dados.data, dados.target, test_size = 0.2, random_state = 42)

modelo = LinearRegression()
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(mse)
print(r2)

plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.xlabel('Valores reais')
plt.ylabel('Valores reais')
plt.show()