class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Foi realizado um depósito de {valor} reais")

    def sacar(self, valor):
        self.saldo -= valor
        print(f"Foi realizado um saque de {valor} reais")

    def exibir_saldo(self):
        print(f"O saldo da conta é de {self.saldo}")

conta1 = Conta("Dante")
conta2 = Conta("Julia")

conta1.depositar(100)
conta2.depositar(200)
conta1.sacar(20)
conta2.sacar(300)
conta1.exibir_saldo()
conta2.exibir_saldo()