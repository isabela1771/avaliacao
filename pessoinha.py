class Pessoa:
    def __init__(self, nome, idade, altura, peso, profissao):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.profissao = profissao

    def apresentar(self):
        print(f"Me chamo {self.nome} , tenho {self.idade} anos , atuo como "
              f"{self.profissao} , tenho {self.altura} metros de altura e peso {self.peso} quilos")

        if self.altura >= 1.79 and self.peso >= 89:
            print(f"Precisa perder gordura !")
        else:
            print(f"Não Precisa perder gordura !")

pessoa1 = Pessoa("Samuel", 18, 1.73, 78, 'estudante')
pessoa2 = Pessoa('Ana Julia', 16, 1.70, 73, "estudante")
pessoa3 = Pessoa("Roseane", 47, 1.72, 80, "Mini Empreendedora")
pessoa4 = Pessoa("Gabriel Pedro", 17, 1.73, 60, "estudante")
pessoa5 = Pessoa("Isa-bela Soa ares", 17, 1.69, 71, "estudante")

pessoa1.apresentar()


