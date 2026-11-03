import random
from memory_profiler import profile

@profile
def gerar_vendas(n=300000):
    vendas = []

    for i in range(n):
        venda = {
            "cliente": random.randint(1, 3000),
            "produto": random.randint(1, 100),
            "valor": random.uniform(10, 1000)
        }

        vendas.append(venda)

    return vendas

@profile
def analisar_vendas(vendas):

    faturamento = 0
    clientes = {}
    quantidade_vendas_altas = 0

    for venda in vendas:

        cliente = venda["cliente"]
        valor = venda["valor"]

        # Faturamento total
        faturamento += valor

        # Faturamento por cliente
        if cliente not in clientes:
            clientes[cliente] = 0

        clientes[cliente] += valor

        # Vendas de alto valor
        if valor >= 900:
            quantidade_vendas_altas += 1

    return faturamento, clientes, quantidade_vendas_altas

@profile
def main():

    vendas = gerar_vendas()

    faturamento, clientes, vendas_altas = analisar_vendas(vendas)

    print(f"Faturamento: R$ {faturamento:,.2f}")
    print(f"Clientes analisados: {len(clientes)}")
    print(f"Vendas acima de R$ 900: {vendas_altas}")


if __name__ == "__main__":
    main()
