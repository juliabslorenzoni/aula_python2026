#Identificar o problema, corrigi-lo e testar
#1ª Forma: Colocar o print no meio do código e ver se funfiona
#2ª Forma: Usar o logging (requisitos mais sofisticados)
#3ª Forma: Usar depuradores (quando editamos o código)
#O inseto do lado da seta de run: vai correr o código ate a bolinha vermelha
#LOGGING: registrar mensagens durante a execução de um programa, usado quando alguém ja usa o código. Possui níveis de severidade, controle de saída, registro em arquivo e formatos customizáveis.
##NÍVEIS LOG: Debug - detalhes técnicos, Info - informações gerais sobre o fluxo, Warning - algo inesperado que não quebra o código, Error - erros que impedem a execução do código, Critical - erros graves que podem encerrar o programa.
def soma_ate (n):
    soma = 0

    for i in range(n):
        soma += i

    return soma

print(soma_ate(3))
