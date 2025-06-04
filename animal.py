class Animal:
    def falar(self):
        print("Este animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late.")

class Gato(Animal):
    def falar(self):
        print("O gato mia.")

#Criando objects

c = Cachorro()
g = Gato()

c.falar() #Saída: O cachorro late.
g.falar() #Saída: O gato mia.