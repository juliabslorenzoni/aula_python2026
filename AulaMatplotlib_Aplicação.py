import pandas as pd
import matplotlib.pyplot as plt

vendas = pd.read_excel(r"C:\Users\julia\OneDrive\Desktop\JULIA\LINGUAGENS DE PROGRAMAÇÃO\Dados_vendas.xlsx", sheet_name='Planilha1')
produtos = pd.read_excel(r"C:\Users\julia\OneDrive\Desktop\JULIA\LINGUAGENS DE PROGRAMAÇÃO\Dados_vendas.xlsx", sheet_name='Planilha2')

plt.plot(vendas['Mes'],vendas['Vendas'])
plt.title("Evolução de Vendas", fontsize=20, fontweight='bold')
plt.xlabel("Meses", fontsize=20)
plt.ylabel("Vendas", fontsize=20)
plt.grid(True,linestyle='--',alpha=0.6)
plt.show()

plt.plot(produtos['Produto'],produtos['Quantidade_Vendida'])
plt.title("Quantidade de Vendas Por Produto", fontsize=20, fontweight='bold')
plt.xlabel("Produtos", fontsize=20)
plt.ylabel("Vendas", fontsize=20)
plt.grid(True,linestyle='--',alpha=0.6)
plt.show()

#COLOCAR MAIS DE UM GRÁFICO NA MESMA IMAGEM
fig,axs = plt.subplots(nrows=1, ncols=2)
axs[0].plot([1,2,3,4],[10,15,18,20])
axs[0].set_title("Gráfico 1")

axs[1].bar(["A","B","C","D"],[10,15,18,20])
axs[1].set_title("Gráfico 2")
plt.show()
