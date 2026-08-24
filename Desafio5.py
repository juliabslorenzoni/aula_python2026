class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso
    def informacao_aluno(self):
        return f"O(a) aluno(a) {self.nome} tem {self.idade} anos, sua matrícula é {self.matricula} e seu curso é {self.curso}"

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina
    def informacao_professor(self):
        return f"O(a) professor(a) {self.nome} tem {self.idade} anos, sua salário é {self.salario} e leciona {self.disciplina}"

aluno1 = Aluno("Julia", 18, "J123456789", "Ciência de Dados")
professor1 = Professor("Octavio", 34, 100000, "Linguagens da Programação")

print(aluno1.informacao_aluno())
print(professor1.informacao_professor())