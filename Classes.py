class Pessoa():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    def saudacao(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

class Professor(Pessoa):
    def __init__(self, nome, idade, sexo, titulo):
        super().__init__(nome, idade, sexo)
        self.titulo = titulo
    def info(self):
        print(f"O titulo é {self.titulo}")

prof_1 = Professor ("Manoel", "65", "Masculino", "Doutor")
print(prof_1.nome)
print(prof_1.info())

pessoa1 = Pessoa("Isaac", "35", "Masculino")
pessoa2 = Pessoa("Esteniffer", "34", "Feminino")
pessoa3 = Pessoa("Gabriel", "0", "Masculino")

pessoa1.saudacao()
pessoa2.saudacao()
pessoa3.saudacao()

print(pessoa1.nome)
print(pessoa2.nome)