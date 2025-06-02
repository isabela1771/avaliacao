#CRIAR CLASSE CLIENTE QUE VAI ARMAZENAR OS DADOS DO CLIENTE,NOME, CPF, RENDA MENSAL, CREDITO, ESCORIA devera conter o
# metodo,verificar credito o cliente so tera credito aprovado se a escoria + ou = 600 e a renda igual a 2000

class Cliente:
    def __init__(self, nome, cpf, renda_mensal, sc_credito,):
        self.nome = nome
        self.cpf = cpf
        self.renda_mensal = renda_mensal
        self.sc_credito = sc_credito


    def verificar(self):
        if self.sc_credito >= 600 and self.renda_mensal >= 2000:
            print(f"Seu crédito está aprovado!! ")
        else:
            print(f"Seu crédito foi negado vacilão!! ")

cliente1 = Cliente("Rafael", "432.234.877-12", 3000.00,1000)
cliente2 = Cliente("Karla", "423.886.397-77", 1500.00, 600)
cliente3 = Cliente("Marina", "555.667.197-88", 5000.00, 700)

cliente1.verificar()
cliente2.verificar()
cliente3.verificar()