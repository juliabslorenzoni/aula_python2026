import logging

logging.basicConfig(filename="aula_python2026/Arquivo_Desafio7.log,",
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
while True:
    print("PROCESSAMENTO DE PEDIDOS:\n1- Iniciar\n2- Sair")
    opcao = int(input("Digite a opção:"))
    if opcao == 1:
        input("Nome do cliente:")
        input("Nome do produto:")
        quantidade = int(input("Quantidade:"))
        valor_unitario = int(input("Valor unitário:"))
        try:
            valor_total = quantidade*valor_unitario
            logging.info(f"O valor total é {valor_total}")
            print(valor_total)
        except ZeroDivisionError:
            logging.error("Erro ao multiplicar por 0")
            print("Não foi possível calcular o valor final")

    else:
        break