class Calculadora:
    
    def somar(self, a,b):
        return a + b

    def subtrair(self, a,b):
        return a - b
    def multiplicar(self, a,b): 
        return a * b
    def dividir(self, a,b): 
        if b == 0:
            raise ValueError("Não pode dividir por zero")
        else:
            return a / b
    