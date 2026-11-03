import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

vendas = pd.read_excel(r"C:\Users\julia\Downloads\661bc695-44b2-47f0-bc4d-2015abf56dfe.xlsx", sheet_name="Vendas")
dicionario = pd.read_excel(r"C:\Users\julia\Downloads\661bc695-44b2-47f0-bc4d-2015abf56dfe.xlsx",
                           sheet_name="Dicionario")

#ETAPA 1: CONHECENDO OS DADOS

print("Quantidade de registros:")
print(vendas.shape[0])

print("Variáveis:")
print(vendas.columns)

print("Tipos das variáveis e valores não nulos:")
print(vendas.info())

print("Valores ausentes por variável:")
print(vendas.isnull().sum())

print("Estatísticas descritivas:")
print(vendas[["Quantidade", "Preco_Unitario", "Desconto"]].describe())

print("Estatísticas da avaliação:")
print(vendas["Avaliacao"].describe())

print("ID_Venda é único?")
print(vendas["ID_Venda"].is_unique)

print("Período da base:")
print(vendas["Data"].min(), "a", vendas["Data"].max())

print("Quantas vendas têm o desconto máximo e em quais lojas:")
print((vendas["Desconto"] == vendas["Desconto"].max()).sum())
print(vendas[vendas["Desconto"] == vendas["Desconto"].max()]["Loja"].value_counts())

print("Distribuição das avaliações (1 a 5):")
print(vendas["Avaliacao"].value_counts().sort_index())

print("Distribuição da quantidade por venda:")
print(vendas["Quantidade"].value_counts().sort_index())

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

vendas["Quantidade"].value_counts().sort_index().plot(kind="bar", ax=axes[0], color="steelblue")
axes[0].set_title("Quantidade por venda")
axes[0].set_xlabel("Unidades")
axes[0].set_ylabel("Número de vendas")

axes[1].boxplot(vendas["Preco_Unitario"])
axes[1].set_title("Preço unitário (R$)")

axes[2].hist(vendas["Desconto"] * 100, bins=20, color="steelblue", edgecolor="white")
axes[2].set_title("Distribuição do desconto")
axes[2].set_xlabel("Desconto (%)")
axes[2].set_ylabel("Número de vendas")

plt.tight_layout()
plt.show()

#ETAPA 2: INDICADORES GERAIS DO NEGÓCIO

vendas["Valor_Venda"] = vendas["Quantidade"] * vendas["Preco_Unitario"] * (1 - vendas["Desconto"])

print("Faturamento total (R$):")
print(vendas["Valor_Venda"].sum())

print("Quantidade total de produtos vendidos:")
print(vendas["Quantidade"].sum())

print("Número de vendas realizadas:")
print(vendas["ID_Venda"].count())

print("Valor médio das vendas (R$):")
print(vendas["Valor_Venda"].mean())

print("Desconto médio concedido:")
print(vendas["Desconto"].mean())

print("Avaliação média dos clientes:")
print(vendas["Avaliacao"].mean())

print("Mediana do valor das vendas (R$):")
print(vendas["Valor_Venda"].median())

print("Faturamento médio por mês (R$):")
print(vendas["Valor_Venda"].sum() / 12)

print("Unidades vendidas por venda (média):")
print(vendas["Quantidade"].sum() / vendas["ID_Venda"].count())

valor_bruto = (vendas["Quantidade"] * vendas["Preco_Unitario"]).sum()
print("Valor bruto das vendas, antes do desconto (R$):")
print(valor_bruto)
print("Valor total concedido em descontos (R$):")
print(valor_bruto - vendas["Valor_Venda"].sum())

q1 = vendas["Valor_Venda"].quantile(0.25)
q3 = vendas["Valor_Venda"].quantile(0.75)
limite = q3 + 1.5 * (q3 - q1)
print("Limite superior de valores atípicos (R$):")
print(limite)
print("Vendas acima desse limite:")
print((vendas["Valor_Venda"] > limite).sum())

plt.figure(figsize=(8, 4))
plt.hist(vendas["Valor_Venda"], bins=30, color="steelblue", edgecolor="white")
plt.axvline(vendas["Valor_Venda"].mean(), color="red", linestyle="--", label="Média")
plt.axvline(vendas["Valor_Venda"].median(), color="green", linestyle="--", label="Mediana")
plt.title("Distribuição do valor das vendas")
plt.xlabel("Valor da venda (R$)")
plt.ylabel("Número de vendas")
plt.legend()
plt.tight_layout()
plt.show()

#ETAPA 3: DESEMPENHO DAS LOJAS

lojas = vendas.groupby("Loja").agg(
    Faturamento=("Valor_Venda", "sum"),
    Num_Vendas=("ID_Venda", "count"),
    Qtd_Produtos=("Quantidade", "sum"),
    Ticket_Medio=("Valor_Venda", "mean"),
    Avaliacao_Media=("Avaliacao", "mean")
).round(2).sort_values("Faturamento", ascending=False)

print("Desempenho das lojas:")
print(lojas)

print("Preço unitário médio por loja (R$):")
print(vendas.groupby("Loja")["Preco_Unitario"].mean().round(2))

print("Desconto médio por loja:")
print(vendas.groupby("Loja")["Desconto"].mean().round(4))

print("Percentual de avaliações com nota 3 ou menos, por loja:")
print((vendas["Avaliacao"].le(3).groupby(vendas["Loja"]).mean() * 100).round(1))

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

lojas["Faturamento"].plot(kind="bar", ax=axes[0], color="steelblue")
axes[0].set_title("Faturamento (R$)")
axes[0].bar_label(axes[0].containers[0], fmt="%.0f")

lojas["Num_Vendas"].plot(kind="bar", ax=axes[1], color="seagreen")
axes[1].set_title("Número de vendas")
axes[1].bar_label(axes[1].containers[0])

lojas["Qtd_Produtos"].plot(kind="bar", ax=axes[2], color="darkorange")
axes[2].set_title("Quantidade de produtos vendidos")
axes[2].bar_label(axes[2].containers[0])

for ax in axes:
    ax.set_xlabel("")
    ax.tick_params(axis="x", rotation=30)

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

lojas["Ticket_Medio"].plot(kind="bar", ax=axes[0], color="mediumpurple")
axes[0].set_title("Ticket médio (R$)")
axes[0].bar_label(axes[0].containers[0], fmt="%.2f")

lojas["Avaliacao_Media"].plot(kind="bar", ax=axes[1], color="goldenrod")
axes[1].set_title("Avaliação média")
axes[1].set_ylim(1, 5)
axes[1].bar_label(axes[1].containers[0], fmt="%.2f")

for ax in axes:
    ax.set_xlabel("")
    ax.tick_params(axis="x", rotation=30)

plt.tight_layout()
plt.show()

#ETAPA 4: PRODUTOS E CATEGORIAS

categorias = vendas.groupby("Categoria").agg(
    Faturamento=("Valor_Venda", "sum"),
    Qtd_Produtos=("Quantidade", "sum"),
    Num_Vendas=("ID_Venda", "count"),
    Ticket_Medio=("Valor_Venda", "mean")
).round(2)

produtos = vendas.groupby("Produto").agg(
    Faturamento=("Valor_Venda", "sum"),
    Qtd_Produtos=("Quantidade", "sum"),
    Num_Vendas=("ID_Venda", "count"),
    Ticket_Medio=("Valor_Venda", "mean")
).round(2)

print("Categorias com maior faturamento:")
print(categorias["Faturamento"].sort_values(ascending=False))

print("Categorias com maior quantidade de produtos vendidos:")
print(categorias["Qtd_Produtos"].sort_values(ascending=False))

print("Produtos com maior faturamento (top 5):")
print(produtos["Faturamento"].sort_values(ascending=False).head(5))

print("Produtos com maior quantidade vendida (top 5):")
print(produtos["Qtd_Produtos"].sort_values(ascending=False).head(5))

print("Produtos com maior número de vendas (top 5):")
print(produtos["Num_Vendas"].sort_values(ascending=False).head(5))

print("Posição de cada produto em cada critério (1 = melhor):")
ranking_produtos = produtos[["Faturamento", "Qtd_Produtos", "Num_Vendas"]].rank(ascending=False, method="min").astype(
    int)
print(ranking_produtos.sort_values("Faturamento"))

print("Participação das categorias no faturamento (%):")
print((categorias["Faturamento"] / categorias["Faturamento"].sum() * 100).round(1))

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

categorias["Faturamento"].sort_values(ascending=False).plot(kind="bar", ax=axes[0], color="steelblue")
axes[0].set_title("Faturamento por categoria (R$)")
axes[0].bar_label(axes[0].containers[0], fmt="%.0f")

categorias["Qtd_Produtos"].sort_values(ascending=False).plot(kind="bar", ax=axes[1], color="darkorange")
axes[1].set_title("Quantidade vendida por categoria")
axes[1].bar_label(axes[1].containers[0])

for ax in axes:
    ax.set_xlabel("")
    ax.tick_params(axis="x", rotation=30)

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

produtos["Faturamento"].sort_values().plot(kind="barh", ax=axes[0], color="steelblue")
axes[0].set_title("Faturamento por produto (R$)")

produtos["Qtd_Produtos"].sort_values().plot(kind="barh", ax=axes[1], color="darkorange")
axes[1].set_title("Quantidade vendida por produto")

for ax in axes:
    ax.set_ylabel("")

plt.tight_layout()
plt.show()

#ETAPA 5: DESEMPENHO DOS VENDEDORES

vendedores = vendas.groupby("Vendedor").agg(
    Faturamento=("Valor_Venda", "sum"),
    Num_Vendas=("ID_Venda", "count"),
    Qtd_Produtos=("Quantidade", "sum"),
    Ticket_Medio=("Valor_Venda", "mean"),
    Desconto_Medio=("Desconto", "mean")
).round(4).sort_values("Faturamento", ascending=False)

print("Desempenho dos vendedores:")
print(vendedores.round(3))

print("Posição de cada vendedor em cada indicador (1 = maior valor):")
ranking_vendedores = vendedores.rank(ascending=False, method="min").astype(int)
print(ranking_vendedores)

print("Loja em que cada vendedor atua:")
print(vendas.groupby("Vendedor")["Loja"].unique())

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

vendedores["Faturamento"].sort_values().plot(kind="barh", ax=axes[0, 0], color="steelblue")
axes[0, 0].set_title("Faturamento (R$)")

vendedores["Num_Vendas"].sort_values().plot(kind="barh", ax=axes[0, 1], color="seagreen")
axes[0, 1].set_title("Número de vendas")

vendedores["Ticket_Medio"].sort_values().plot(kind="barh", ax=axes[1, 0], color="mediumpurple")
axes[1, 0].set_title("Ticket médio (R$)")

(vendedores["Desconto_Medio"] * 100).sort_values().plot(kind="barh", ax=axes[1, 1], color="indianred")
axes[1, 1].set_title("Desconto médio (%)")

for ax in axes.flat:
    ax.set_ylabel("")

plt.tight_layout()
plt.show()

# ETAPA 6: ANÁLISE DOS DESCONTOS

print("Desconto médio por loja:")
print(vendas.groupby("Loja")["Desconto"].mean().sort_values(ascending=False).round(4))

print("Desconto médio por categoria:")
print(vendas.groupby("Categoria")["Desconto"].mean().sort_values(ascending=False).round(4))

print("Desconto médio por vendedor:")
print(vendas.groupby("Vendedor")["Desconto"].mean().sort_values(ascending=False).round(4))

print("Correlação entre desconto e valor da venda:")
print(vendas["Desconto"].corr(vendas["Valor_Venda"]))

print("Correlação entre desconto e valor da venda, dentro de cada loja:")
print(
    vendas.groupby("Loja")[["Desconto", "Valor_Venda"]].apply(lambda x: x["Desconto"].corr(x["Valor_Venda"])).round(3))

print("Correlação entre faturamento e desconto médio dos vendedores:")
print(vendedores["Faturamento"].corr(vendedores["Desconto_Medio"]))

vendas["Faixa_Desconto"] = pd.cut(vendas["Desconto"], bins=[0, 0.10, 0.15, 0.20, 1],
                                  labels=["Até 10%", "10% a 15%", "15% a 20%", "Acima de 20%"])

faixas = vendas.groupby("Faixa_Desconto", observed=True).agg(
    Num_Vendas=("ID_Venda", "count"),
    Valor_Medio=("Valor_Venda", "mean"),
    Preco_Medio=("Preco_Unitario", "mean"),
    Qtd_Media=("Quantidade", "mean")
).round(2)

print("Valor médio das vendas por faixa de desconto:")
print(faixas)

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

axes[0].scatter(vendas["Desconto"] * 100, vendas["Valor_Venda"], alpha=0.3, color="steelblue")
axes[0].set_title("Desconto x valor da venda")
axes[0].set_xlabel("Desconto (%)")
axes[0].set_ylabel("Valor da venda (R$)")

faixas["Valor_Medio"].plot(kind="bar", ax=axes[1], color="steelblue")
axes[1].set_title("Valor médio por faixa de desconto (R$)")
axes[1].set_xlabel("")
axes[1].tick_params(axis="x", rotation=30)
axes[1].bar_label(axes[1].containers[0], fmt="%.0f")

axes[2].scatter(vendedores["Desconto_Medio"] * 100, vendedores["Faturamento"], color="indianred")
for nome in vendedores.index:
    axes[2].annotate(nome, (vendedores.loc[nome, "Desconto_Medio"] * 100, vendedores.loc[nome, "Faturamento"]))
axes[2].set_title("Vendedores: desconto médio x faturamento")
axes[2].set_xlabel("Desconto médio (%)")
axes[2].set_ylabel("Faturamento (R$)")

plt.tight_layout()
plt.show()

pagamento = vendas.groupby("Forma_Pagamento").agg(
    Num_Vendas=("ID_Venda", "count"),
    Faturamento=("Valor_Venda", "sum"),
    Ticket_Medio=("Valor_Venda", "mean"),
    Desconto_Medio=("Desconto", "mean"),
    Avaliacao_Media=("Avaliacao", "mean")
).round(4).sort_values("Faturamento", ascending=False)

pagamento["Pct_Faturamento"] = (pagamento["Faturamento"] / pagamento["Faturamento"].sum() * 100).round(1)

print("Desempenho por forma de pagamento:")
print(pagamento)

# ETAPA 7: COMPORTAMENTO E AVALIAÇÃO DOS CLIENTES

print("Avaliação média por loja:")
print(vendas.groupby("Loja")["Avaliacao"].mean().sort_values(ascending=False).round(2))

print("Avaliação média por categoria:")
print(vendas.groupby("Categoria")["Avaliacao"].mean().sort_values(ascending=False).round(2))

print("Avaliação média por vendedor:")
print(vendas.groupby("Vendedor")["Avaliacao"].mean().sort_values(ascending=False).round(2))

vendas["Faixa_Valor"] = pd.qcut(vendas["Valor_Venda"], 4,
                                labels=["1º quartil (menores)", "2º quartil", "3º quartil", "4º quartil (maiores)"])

print("Avaliação média por faixa de valor da compra:")
print(vendas.groupby("Faixa_Valor", observed=True)["Avaliacao"].mean().round(2))

print("Avaliação média por faixa de desconto:")
print(vendas.groupby("Faixa_Desconto", observed=True)["Avaliacao"].mean().round(2))

print("Correlação da avaliação com valor da venda e com desconto:")
print(vendas[["Avaliacao", "Valor_Venda", "Desconto"]].corr().round(3)["Avaliacao"])

print("Correlação entre desconto e avaliação, dentro de cada loja:")
print(vendas.groupby("Loja")[["Desconto", "Avaliacao"]].apply(lambda x: x["Desconto"].corr(x["Avaliacao"])).round(3))

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

vendas.groupby("Loja")["Avaliacao"].mean().sort_values().plot(kind="barh", ax=axes[0], color="goldenrod")
axes[0].set_title("Avaliação média por loja")
axes[0].set_xlim(1, 5)

vendas.groupby("Vendedor")["Avaliacao"].mean().sort_values().plot(kind="barh", ax=axes[1], color="goldenrod")
axes[1].set_title("Avaliação média por vendedor")
axes[1].set_xlim(1, 5)

vendas.groupby("Faixa_Desconto", observed=True)["Avaliacao"].mean().plot(kind="bar", ax=axes[2], color="indianred")
axes[2].set_title("Avaliação média por faixa de desconto")
axes[2].set_ylim(1, 5)
axes[2].tick_params(axis="x", rotation=30)
axes[2].bar_label(axes[2].containers[0], fmt="%.2f")

for ax in axes:
    ax.set_xlabel("")
    ax.set_ylabel("")

plt.tight_layout()
plt.show()

# ETAPA 8: EVOLUÇÃO DAS VENDAS

vendas["Mes"] = vendas["Data"].dt.month

mensal = vendas.groupby("Mes").agg(
    Faturamento=("Valor_Venda", "sum"),
    Num_Vendas=("ID_Venda", "count"),
    Ticket_Medio=("Valor_Venda", "mean"),
    Desconto_Medio=("Desconto", "mean")
).round(4)

nomes_meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
mensal.index = nomes_meses

print("Evolução mensal:")
print(mensal.round(3))

print("Meses de maior faturamento:")
print(mensal["Faturamento"].nlargest(3).round(2))

print("Meses de menor faturamento:")
print(mensal["Faturamento"].nsmallest(3).round(2))

cat_mes = vendas.pivot_table(index="Mes", columns="Categoria", values="Valor_Venda", aggfunc="sum")
cat_mes.index = nomes_meses

print("Faturamento por categoria em cada mês (R$):")
print(cat_mes.round(0))

print("Faturamento médio mensal de cada categoria (R$):")
print(cat_mes.mean().round(0))

print("Faturamento do 1º semestre (R$):")
print(vendas[vendas["Mes"] <= 6]["Valor_Venda"].sum())

print("Faturamento do 2º semestre (R$):")
print(vendas[vendas["Mes"] > 6]["Valor_Venda"].sum())

print("Correlação entre faturamento mensal e número de vendas:")
print(mensal["Faturamento"].corr(mensal["Num_Vendas"]))

fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))

mensal["Faturamento"].plot(ax=axes[0], marker="o", color="steelblue")
axes[0].set_title("Faturamento mensal (R$)")
axes[0].set_xlabel("")

mensal["Num_Vendas"].plot(ax=axes[1], marker="o", color="seagreen")
axes[1].set_title("Número de vendas por mês")
axes[1].set_xlabel("")

for ax in axes:
    ax.set_xticks(range(12))
    ax.set_xticklabels(nomes_meses)
    ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()

cat_mes.plot(kind="bar", stacked=True, figsize=(11, 5))
plt.title("Faturamento mensal por categoria (R$)")
plt.xlabel("")
plt.xticks(rotation=0)
plt.legend(title="Categoria")
plt.tight_layout()
plt.show()