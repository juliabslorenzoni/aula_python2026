import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets
from sklearn.model_selection import train_test_split

arquivo = pd.read_excel(r"C:\Users\julia\Downloads\cc079fef-6c3f-4620-878d-c9a41e69a9f9.xlsx")

#1. Conhecendo os Dados
linhas, colunas = arquivo.shape
print(f"Total de linhas: {linhas}\nTotal de colunas: {colunas}")
print(f'Primeiras Observações:\n{arquivo.head(5)}')
print(f"Tipo das variáveis e valores ausentes:\n{arquivo.info()}")
print(f"Estatística descritiva:\n{arquivo[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales', 'Critic_Score']].describe()}")

#2. Explorando os jogos
print("Qual jogo apresentou a maior venda global?")
maior_venda_global = arquivo.loc[arquivo["Global_Sales"].idxmax()]
print(maior_venda_global)
print("Qual jogo apresentou a maior venda na América do Norte?")
maior_venda_AN = arquivo.loc[arquivo["NA_Sales"].idxmax()]
print(maior_venda_AN)
print("Qual jogo apresentou a maior venda na Europa?")
maior_venda_EU = arquivo.loc[arquivo["EU_Sales"].idxmax()]
print(maior_venda_EU)
print("Qual jogo apresentou a maior venda no Japão?")
maior_venda_JP = arquivo.loc[arquivo["JP_Sales"].idxmax()]
print(maior_venda_JP)

#3. Avaliação × vendas
print("Gráfico de dispersão: Nota dos críticos × Vendas globais")
plt.scatter(arquivo["Critic_Score"], arquivo["Global_Sales"])
plt.title("Relação entre a Nota dos Críticos e as Vendas Globais")
plt.xlabel('Nota dos Críticos')
plt.ylabel('Vendas Globais')
plt.show()

print("Gráfico de dispersão: Nota dos usuários × Vendas globais")
plt.scatter(arquivo["User_Score"], arquivo["Global_Sales"], color='purple')
plt.title("Relação entre a Nota dos usuários × Vendas globais")
plt.xlabel('Nota dos Usuários')
plt.ylabel('Vendas Globais')
plt.show()

print("As notas parecem estar relacionadas às vendas? A relação parece forte ou fraca?\nSim, de acordo com os gráficos, as notas estão relacionadas com as vendas. A corelação parece forte.")

#4. Modelo de vendas globais
arquivo = arquivo.dropna()
y = arquivo["Global_Sales"].values
x1 = arquivo["Critic_Score"].values
x2 = arquivo["User_Score"].values

X = np.column_stack((x1,x2))

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
modelo = LinearRegression()
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
rs = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE):{mse}')
print(f'R²:{rs}')

#5. O modelo consegue prever as vendas?
print("Gráfico de comparação: Vendas reais × Vendas previstas")
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.xlabel('Vendas Reais')
plt.ylabel('Vendas Previstas')
plt.show()

#6. O comportamento é igual em diferentes mercados?
print("Comportamento na América do Norte:")
y = arquivo["NA_Sales"].values
x1 = arquivo["Critic_Score"].values
x2 = arquivo["User_Score"].values

X = np.column_stack((x1,x2))

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
modelo = LinearRegression()
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
rs = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE):{mse}')
print(f'R²:{rs}')

print("Comportamento na Europa:")
y = arquivo["EU_Sales"].values
x1 = arquivo["Critic_Score"].values
x2 = arquivo["User_Score"].values

X = np.column_stack((x1,x2))

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
modelo = LinearRegression()
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
rs = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE):{mse}')
print(f'R²:{rs}')

print("Comportamento no Japão:")
y = arquivo["JP_Sales"].values
x1 = arquivo["Critic_Score"].values
x2 = arquivo["User_Score"].values

X = np.column_stack((x1,x2))

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
modelo = LinearRegression()
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
rs = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE):{mse}')
print(f'R²:{rs}')

print("Em qual mercado as avaliações apresentam maior capacidade de explicar as vendas?\nOs mercados são Japão e Europa.")

#7. Prevendo as vendas de novos jogos
previsao_A = modelo.predict([[90, 8.5]])
print(f"Previsão do Jogo A: {previsao_A}")

previsao_B = modelo.predict([[75, 7]])
print(f"Previsão do Jogo B: {previsao_B}")

previsao_C = modelo.predict([[55, 5.5]])
print(f"Previsão do Jogo C: {previsao_C}")