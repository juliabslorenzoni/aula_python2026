class Produto:
    def __init__(self, nome, preco, quantidade=10):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, numero):
        self.quantidade += numero
        print(f"Foi adicionado ao estoque: {numero}")
    def remover_estoque(self, numero):
        self.quantidade -= numero
        print(f"Foi removido ao estoque: {numero}")

    def valor_total(self):
        print(f"O valor total de produtos: {self.quantidade*self.preco}")

produto1 = Produto("Maçã", 2)
produto2 = Produto("Banana", 5)

produto1.adicionar_estoque(20)
produto2.adicionar_estoque(10)
produto1.remover_estoque(10)
produto2.remover_estoque(15)
produto1.valor_total()
produto2.valor_total()