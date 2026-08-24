class Veiculo:
    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

class Carro(Veiculo):
    def ipva_carro(self):
        return self.valor*0.04

class Moto(Veiculo):
    def ipva_moto(self):
        return self.valor*0.02

while True:
    print("MENU DE CADASTRO:\n1- Carro\n2- Moto\n3- Cancelar")
    opcao = int(input("Digite a opção com que você deseja proseguir: "))
    if opcao == 1:
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo: ")
        ano = input("Digite o ano do carro: ")
        valor = int(input("Digite o valor do carro (apenas números): "))
        cliente1 = Carro(marca, modelo, ano, valor)
        print(cliente1.marca, cliente1.modelo, cliente1.ano, cliente1.valor, cliente1.ipva_carro())
    elif opcao == 2:
        marca = input("Digite a marca da moto: ")
        modelo = input("Digite o modelo: ")
        ano = input("Digite o ano da moto: ")
        valor = int(input("Digite o valor da moto (apenas números): "))
        cliente2 = Carro(marca, modelo, ano, valor)
        print(cliente2.marca, cliente2.modelo, cliente2.ano, cliente2.valor, cliente2.ipva_moto())
    else:
        break