#PLOT: gráfico de linhas
#SCATTER: gráfico de dispersão (bolinha)
#MARKER: transforma a marcação em alguma coisa. Ex: marker='s' transforma a bolinha em quadrado
#HIST/HISTOGRAMA: gráfico de colunas coladas que mostra a frequência com que um grupo de dados numéricos contínuos aparece em determinados intervalos
import matplotlib.pyplot as plt

#GRÁFICO DE LINHA OU DISPERSÃO (plot ou scatter):
plt.scatter([1,2,3,4,5], [10,20,30,40,50], marker='s', color='red') #primeira estrutura: dados
plt.title("Título do Gráfico")
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.show()

#HISTOGRAMA:
dados = [12, 15, 13, 18, 22, 21, 23, 25, 25, 27, 30, 33, 35, 40]

plt.hist(dados, bins=10, color='red', edgecolor='black')
plt.title("Título do Gráfico")
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.show()

#GRÁFICO DE PIZZA:
x = ["A", "B", "C", "D"]
y = [40,25,60,30]
plt.pie( y, labels=x, autopct= '%1.1f%%' )
plt.show()
