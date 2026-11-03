class Personagem():
    def __init__(self, nome, energia, ataque):
        self.nome = nome
        self.energia = energia
        self.ataque = ataque

personagens = []

personagem = Personagem("P1", 100,35)
personagens.append(personagem)
print("Seu personagem tem Id:", len(personagens)-1)

personagem = Personagem("P2", 100,35)
personagens.append(personagem)
print("Seu personagem tem Id:", len(personagens)-1)

for i in range(len(personagens)):
    print(personagens[i].nome, personagens[i].energia, personagens[i].ataque)