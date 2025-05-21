# import math
# class ValidadorIdade:

#     def validar_idade(self, idade):

#         if not isinstance(idade, (int, float)):
#             raise ValueError("Idade informada não é um número.")
        
#         if math.isnan(idade):
#             raise ValueError("Idade informada não é um número.")

#         if idade < 0 or idade > 200:
#             raise ValueError("Idade infomada fora do limite permitido.")
        
#         if idade < 13:
#             return "Cadastro não permitido"
#         elif 13 <= idade < 18:
#             return "Necessário consentimento dos pais"
#         else:
#             return "Cadastro liberado"
        

