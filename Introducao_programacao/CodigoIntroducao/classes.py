class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} \ne eu tenho {self.idade} anos.")
    
    def idade_atual(self):
        print(f" {self.idade} anos.")
    
    def andar(self):
        print(f"{self.nome} está andando.")

    def cumprimentar_amigo(self, nome_amigo):
        print(f"Olá, {nome_amigo}! \nEu sou {self.nome}")
    
david = Pessoa("Luciano", 46)
david.apresentar()
david.andar()
david.cumprimentar_amigo("David Brandão")