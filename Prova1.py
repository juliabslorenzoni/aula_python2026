class Chamado:
    def __init__(self, titulo, descricao, status, data_abertura):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_abertura = data_abertura

class Hardware(Chamado):
    def __init__(self, titulo, descricao, status, data_abertura, codigo_do_equipamento):
        super().__init__(titulo, descricao, status, data_abertura)
        self.codigo_do_equipamento = codigo_do_equipamento
    def exibir_resumo(self):
        return f"Chamado [{self.titulo}], descrÃ­Ã§Ã£o[{self.descricao}], status [{self.status}], data [{self.data_abertura}] e cÃ³digo do equipamento [{self.codigo_do_equipamento}]."
    def __str__(self):
        return f"Chamado [{self.titulo}], descrÃ­Ã§Ã£o[{self.descricao}], status [{self.status}], data [{self.data_abertura}] e cÃ³digo do equipamento [{self.codigo_do_equipamento}]."

class Software(Chamado):
    def __init__(self, titulo, descricao, status, data_abertura, sistema):
        super().__init__(titulo, descricao, status, data_abertura)
        self.sistema = sistema
    def exibir_resumo(self):
            return f"Chamado [{self.titulo}], descrÃ­Ã§Ã£o[{self.descricao}], status [{self.status}], data [{self.data_abertura}] e sistema [{self.sistema}]."
    def __str__(self):
        return f"Chamado [{self.titulo}], descrÃ­Ã§Ã£o[{self.descricao}], status [{self.status}], data [{self.data_abertura}] e sistema [{self.sistema}]."

chamados_hardware = []
chamados_software = []

while True:
    print("ABERTURA DE CHAMADO:\n1- Hardware\n2- Software\n3- Listar os chamados Hardware\n4- Listar os chamados Software\n5- Listar todos os chamados\n6- Sair")
    opcao = int(input("Escolha uma opÃ§Ã£o para prosseguir:"))
    if opcao == 1:
        titulo = input("Informe o titulo do chamado: ")
        descricao = input("Informe a descriÃ§Ã£o do chamado: ")
        status = input("Informe o status do chamado: ")
        data_abertura = input("Informe a data de abertura do chamado: ")
        codigo_do_equipamento = input("Informe o codigo do equipamento do chamado: ")
        chamado1 = Hardware(titulo, descricao, status, data_abertura, codigo_do_equipamento)
        chamados_hardware.append(chamado1)
        print(chamado1.exibir_resumo())
    elif opcao == 2:
        titulo = input("Informe o titulo do chamado: ")
        descricao = input("Informe a descriÃ§Ã£o do chamado: ")
        status = input("Informe o status do chamado: ")
        data_abertura = input("Informe a data de abertura do chamado: ")
        sistema = input("Informe o sistema do chamado: ")
        chamado2 = Software(titulo, descricao, status, data_abertura, sistema)
        chamados_software.append(chamado2)
        print(chamado2.exibir_resumo())
    elif opcao == 3:
        for i in range(len(chamados_hardware)):
            print(chamados_hardware[i])
    elif opcao == 4:
        for i in range(len(chamados_software)):
            print(chamados_software[i])
    elif opcao == 5:
        for i in range(len(chamados_hardware)):
            print(chamados_hardware[i])
        for i in range(len(chamados_software)):
            print(chamados_software[i])
    else:
        break