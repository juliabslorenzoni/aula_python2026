import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets
from sklearn.model_selection import train_test_split

titanic = pd.read_excel(r"C:\Users\julia\Downloads\94557f36-bfa8-42dd-b367-c6620ca47b56.xlsx")

y = titanic["Survived"].values
x1 = titanic["Pclass"].values
x2 = titanic["Sex"].values
x3 = titanic["Age"].values
x4 = titanic["Relatives"].values
x5 = titanic["Fare"].values

X = np.column_stack((x1,x2,x3,x4,x5))

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
modelo = LinearRegression()
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
rs = r2_score(y_test, y_pred)
print(mse)
print(rs)

plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.xlabel('Valores reais')
plt.ylabel('Valores reais')
plt.show()

previsao = modelo.predict([[1, 0, 18, 5, 10000.0]])
print(previsao)