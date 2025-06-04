class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar (self):
        print(f"Olá, meu nome é {self.nome}")

class Professor(Pessoa):
    def __init__(self, nome, departamento):
        super().__init__(nome)
        self.departamento = departamento #Aqui estamos passando um objeto

    def apresentar(self):
        print(f"Sou o Professor {self.nome}, do departamento de {self.departamento.nome}")

class Departamento:
    def __init__(self, nome):
        self.nome = nome

dep = Departamento("Computação")
prof = Professor("Carlos", dep) #


prof.apresentar()

