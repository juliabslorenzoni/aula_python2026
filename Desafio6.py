from abc import ABC, abstractmethod

class Mensagem(ABC):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    @abstractmethod
    def enviar(self):
        pass

class Email(Mensagem):
    def __init__(self, conteudo, destinatario):
        super().__init__(conteudo)
        self.destinatario = destinatario
    def enviar(self):
        return f"Enviando e-mail para {self.destinatario}@dominio.com: [{self.conteudo}]"

class SMS(Mensagem):
    def __init__(self, conteudo, numero_telefone):
        super().__init__(conteudo)
        self.numero_telefone = numero_telefone
    def enviar(self):
        return f"Enviando SMS para {self.numero_telefone}: [{self.conteudo}]"

while True:
    print("ENVIO DE MENSAGENS:\n1: E-mail\n2: SMS\n3: Sair")
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        destinatario = input("Nome do destino: ")
        conteudo = input("Conteúdo:")
        cliente1 = Email(conteudo, destinatario)
        print(cliente1.enviar())
    elif opcao == 2:
        numero_telefone = int(input("Numero de telefone: "))
        conteudo = input("Conteúdo: ")
        cliente2 = SMS(conteudo, numero_telefone)
        print(cliente2.enviar())
    else:
        break