class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Olá, me chamo {self.nome} e a minha idade é {self.idade}'
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def estudar(self):
        return f'Olá, me chamo {self.nome}, idade {self.idade}, curso {self.curso}'


pessoa = Pessoa("Angelo", 26)
print(pessoa.apresentar())

aluno = Aluno("Angelo", 26, "Engenharia de Software")
print(aluno.apresentar())
print(aluno.estudar())
