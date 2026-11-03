import matplotlib.pyplot as plt
import pandas as pd
pedidos = pd.read_excel(r"C:\Users\julia\OneDrive\Desktop\JULIA\LINGUAGENS DE PROGRAMAÇÃO\aula_pandas_joins.xlsx", sheet_name='pedidos')
vendas_janeiro = pd.read_excel(r"C:\Users\julia\OneDrive\Desktop\JULIA\LINGUAGENS DE PROGRAMAÇÃO\aula_pandas_joins.xlsx", sheet_name='vendas_jan')
populacao = pd.read_excel(r"C:\Users\julia\OneDrive\Desktop\JULIA\LINGUAGENS DE PROGRAMAÇÃO\aula_pandas_joins.xlsx", sheet_name='populacao')


#LINHA
plt.plot(pedidos['data'], pedidos['valor'], color='orange')
plt.title("Evolução de Valor por Data", fontsize=20, fontweight='bold')
plt.xlabel("Data", fontsize=20)
plt.ylabel("Valor", fontsize=20)
plt.show()


#DISPERÇÂO
plt.scatter(pedidos['id_pedido'], pedidos['valor'],color='purple')
plt.title("Valor por ID", fontsize=20, fontweight='bold')
plt.xlabel("ID")
plt.ylabel("Valor")
plt.show()


#BARRAS
plt.bar(populacao['cidade'], populacao['pop_mil'], color='pink')
plt.title("População por Cidade", fontsize=20, fontweight='bold')
plt.xlabel("Cidade")
plt.ylabel("População (mil)")
plt.show()

#PIZZA
x = vendas_janeiro['produto']
y = vendas_janeiro['vendas']
minhas_cores = ['#FF9999', '#66B3FF', '#99FF99']
plt.pie(y, labels=x, autopct= '%1.1f%%',colors=minhas_cores)
plt.title("Vendas por Produto", fontsize=20, fontweight='bold')
plt.xlabel("Produto")
plt.ylabel("Vendas")
plt.show()

#SUBPLOTS
fig,axs = plt.subplots(nrows=2, ncols=2)
axs[0,0].plot(pedidos['data'], pedidos['valor'], color='orange')
axs[0,0].set_title("Evolução de Valor por Data",fontsize=14, fontweight='bold')

axs[0,1].scatter(pedidos['id_pedido'], pedidos['valor'], color='purple')
axs[0,1].set_title("Vendas por ID", fontsize=14, fontweight='bold')

axs[1,0].bar(populacao['cidade'], populacao['pop_mil'], color='pink')
axs[1,0].set_title("População por Cidade", fontsize=14, fontweight='bold')

axs[1,1].pie(y, labels=x, autopct= '%1.1f%%', colors=minhas_cores)
axs[1,1].set_title("Vendas por Produto", fontsize=14, fontweight='bold')
plt.show()

# BOXPLOT
plt.boxplot(pedidos['valor'], patch_artist=True)
plt.title("Distribuição do Valor dos Pedidos")
plt.ylabel("Valor")
plt.show()
