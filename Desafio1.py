class Personagem:
    def __init__(self, nome, energia, ataque, moedas):
        self.nome = nome
        self.energia = energia
        self.ataque = ataque
        self.moedas = moedas

    def mostrar_info(self):
        print(f"Status de {self.nome}")
        print(f"Energia: {self.energia} | Ataque: {self.ataque} | Moedas: {self.moedas}\n")

    def receber_dano(self,dano):
        self.energia -= dano
        if self.energia < 0:
            self.energia = 0
            print(f"{self.nome} recebeu {dano}! Energia restante: {self.energia}")

    def atacar(self, outro_personagem):
        print(f"\n> {self.nome} está atacando {outro_personagem.nome}!")
        outro_personagem.receber_dano(self.ataque)

    def coletar_moedas(self, quantidade):
        self.moedas += quantidade
        print(f"> {self.nome} coletou {quantidade} moedas! Total: {self.moedas}")

guerreiro = Personagem("Guerreiro", energia=100, ataque=20, moedas=5)
mago = Personagem("Mago", energia=80, ataque=30, moedas=10)

guerreiro.mostrar_info()
mago.mostrar_info()

mago.atacar(guerreiro)
guerreiro.atacar(mago)

guerreiro.coletar_moedas(15)

print("STATUS FINAL:")
guerreiro.mostrar_info()
mago.mostrar_info()