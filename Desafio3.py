class Aluno:
    def __init__(self, nome, nota, status=False):
        self._nome = nome
        self._nota = nota
        self._status = status

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            print("Nota invalida")
            raise ValueError("A nota não pode ser menor que 0 e maior que 10")
        elif nota >=6:
            self._status = True
        else:
            self._status = False
        self._nota = nota

a = Aluno("Julia", 8)
print(a.nota, a._status)