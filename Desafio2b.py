class Entrega:
    def __init__(self, distancia, peso):
        self.distancia = distancia
        self.peso = peso

class EntregaComum(Entrega):
    def calcular_frete(self):
        return ((self.distancia*2) + (self.peso*1))

class EntregaExpressa(Entrega):
    def calcular_frete(self):
        return ((self.distancia*3,5) + (self.peso*2) + 10)

while True:
    print("VERIFICAÇÃO DO VALOR DE ENTREGA:\n1- Entrega Comum\n2- Entrega Expressa\n3- Cancelar")
    opcao = int(input("Digite a opção:"))
    if opcao == 1:
        distancia = float(input("Qual a distância (apenas números): "))
        peso = float(input("Qual o peso (apenas números): "))
        cliente1 = EntregaComum(distancia, peso)
        print(cliente1.calcular_frete())
    elif opcao == 2:
        distancia = float(input("Qual a distância (apenas números): "))
        peso = float(input("Qual o peso (apenas números): "))
        cliente2 = EntregaComum(distancia, peso)
        print(cliente2.calcular_frete())
    else:
        break