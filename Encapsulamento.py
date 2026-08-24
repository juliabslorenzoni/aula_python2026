class Conta:
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = saldo

    def __str__(self):
        return f"Nome: {self._nome}, Saldo: {self._saldo}"
    #str usado apenas para imprimir. Se tentar imprimir uma variável que não é string, ela não vai fazer

    def __repr__(self):
        return f"Conta({self._nome}, Saldo: {self._saldo})"
    @property #camada de leitura do atributo: somente leitura
    def saldo(self):
        return self._saldo

    @saldo.setter #permite que o atributo seja alterado com uma regra específica
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = valor

conta1 = Conta("Julia", 10000)
print(repr(conta1))
print(conta1)

c = Conta("Julia", 100)
print(c.saldo)
c.saldo = 1000
print(c.saldo)
