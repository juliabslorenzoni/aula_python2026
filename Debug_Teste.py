#LOGGING: registrar mensagens durante a execução de um programa, usado quando alguém ja usa o código. Possui níveis de severidade, controle de saída, registro em arquivo e formatos customizáveis.
##NÍVEIS LOG: Debug - detalhes técnicos, Info - informações gerais sobre o fluxo, Warning - algo inesperado que não quebra o código, Error - erros que impedem a execução do código, Critical - erros graves que podem encerrar o programa.

import logging

logging.basicConfig(filename="Arquivo_Log.log,",
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def dividir(a, b):
    logging.info(f"A função foi chamada pelo usuário com os valores {a} e {b}")
    try:
        resultado = a/b
        logging.info(f"O resultado é {resultado}")
        return resultado
    except ZeroDivisionError:
        logging.error("Erro ao dividir por 0")
        return 0

dividir (10, 0)