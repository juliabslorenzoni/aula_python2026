from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    @abstractmethod  #Cria obrigatoriedade de haver "calcular_ipva" em todas as subclasses
    def calcular_ipva(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, valor, portas):
        super().__init__(marca, modelo, ano, valor) #Aproveita os atributos já colocados anteriormente
        self.portas = portas #Coloca um atributo específico. Define um  novo, pra n precisar definir tudo de novo

    def calcular_ipva(self):
        return self.valor*0.04

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, valor, cilindrada):
        super().__init__(marca, modelo, ano, valor)
        self.cilindrada = cilindrada

    def calcular_ipva(self):
        return self.valor*0.02

carro1 = Carro("Jeep", "Renegade", 2026, 100000, 4)
moto1 = Moto("Honda", "C6", 2015, 100000, 150)
veic1 = Veiculo("Marco", "Polo", 2005, 100, 1507)
print(carro1.calcular_ipva())
print(moto1.calcular_ipva())