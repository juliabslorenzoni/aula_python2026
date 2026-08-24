class Conta():
    def __init__(self, descricao, valor, vencimento, status):
        self.descricao = descricao
        self.valor = valor
        self.vencimento = vencimento
        self.status = status

    def pagar(self):
        self.status = ('Pago')
        
contas = []

while True:
    resp = int(input("Digite 1 para cadastrar, 2 para pagar, 3 para listar ou 4 para sair:"))
    if resp == 1:
        desc = str(input("Nome:"))
        vlr = float(input("Valor:"))
        venc = str(input("Vencimento:"))
        nova_conta = Conta(desc, vlr, venc)
        contas.append(nova_conta)
        print("Essa conta tem Id: ", len(contas)-1)
    elif resp == 2:
        id_pgt = int(input("Id da conta a ser paga: "))
        contas[id_pgt].pagar()
    elif resp == 3:
        for i in range(len(contas)):
            print(i, contas[i].descricao, contas[i].valor, contas[i].vencimento, contas[i].status)
    else:
        print("Encerramento")
        break