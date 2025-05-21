import math
class ValidadorIdade:

    def validar_idade(self, idade):

        if not isinstance(idade, (int, float)):
            raise ValueError("Idade informada não é um número.")
        
        if math.isnan(idade):
            raise ValueError("Idade informada não é um número.")

        if idade < 0:
            return "Idade infomada fora do limite permitido."
        elif 0 <= idade < 13:
            return "Cadastro não permitido"
        elif 13 <= idade < 18:
            return "Necessário consentimento dos pais"
        elif 18 <= idade <= 200:
            return "Cadastro liberado"
        else:
            return "Idade acima do limite permitido."
        

