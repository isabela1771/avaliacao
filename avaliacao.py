#Samuel e Isabela 02/06/25
class Cliente:
    def __init__(self, nome, cpf, renda_mensal, score_credito):
        self.nome = nome
        self.cpf = cpf
        self.renda_mensal = renda_mensal
        self.score_credito = score_credito

    def verificar(self):
        if self.renda_mensal >= 2000 and self.score_credito >= 600:
            print(f"Cliente {self.nome}: Crédito aprovado para concessão de compras.")
        elif self.renda_mensal < 2000:
            print(f"Cliente {self.nome}: Crédito negado por renda.")
        else:
            print(f"Cliente {self.nome}: Crédito negado por score.")

cliente1 = Cliente("Renata", "466.867.347-87", 1900.00, 700)
cliente1.verificar()
cliente2 = Cliente("Theo", "343.437.568-99", 3000.00, 500)
cliente2.verificar()
cliente3 = Cliente("Kevin", "469.783.657-57", 10000, 9000)
cliente3.verificar()




#ddff