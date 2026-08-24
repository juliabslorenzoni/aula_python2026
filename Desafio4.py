class Ingresso:
    def __init__(self, evento, preco):
        self._evento = evento
        self._preco = preco

class IngressoInteiro(Ingresso):
    def calcular_preco_inteiro(self):
        return self._preco
    def __str__(self):
        return f"O ingresso de {self._evento} custa {self._preco}"
    def __repr__(self):
        return f"A classe é Ingresso os atributos são evento: {self._evento} e preco: {self._preco}"

class IngressoMeia(Ingresso):
    def calcular_preco_meia(self):
        return (self._preco * 0.5)
    def __str__(self):
        return f"O ingresso de {self._evento} custa {self._preco*0.5}"
    def __repr__(self):
        return f"A classe é Ingresso os atributos são evento: {self._evento} e preco: {self._preco*0.5}"

while True:
    print("COMPRA DE INGRESSOS:\n 1- Inteiro\n 2- Meia\n 3- Sair")
    opcao = int(input("Escolha a opção:"))
    if opcao == 1:
        nome = input("Informe o seu nome: ")
        cliente1 = IngressoInteiro(nome, 10)
        print(cliente1)
    elif opcao == 2:
        nome = input("Informe o seu nome: ")
        cliente2 = IngressoMeia(nome, 10)
        print(cliente2)
    else:
        break
