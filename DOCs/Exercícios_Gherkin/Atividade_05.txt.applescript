#Atividade 05 - Cria��o de Scenarios Outlines
# Assim como vimos na aula de hoje, solicito a cria��o de Scenarios~e Scenarios Outline para as quest�es a seguir.

# 	Instru��es:�
# 	�	Esta atividade � individual, cada aluno dever� enviar sua resposta
#	�	Dever� ser enviado um arquivo .txt �nico com todos os cen�rios
#	�	Quest�o 1 a 3 -> Scenario Outline
#	�	Quest�o 4 e 5 -> Scenario normal (gherkin)

#______________________________________________________________


# 1 -�[Valor Limite]��Um campo de formul�rio aceita sal�rios entre R$ 1.000 e R$ 10.000. 
# Crie casos de teste considerando os valores limite inferiores e superiores, utilizando Scenario Outline em Gherkin.

Scenario outline: Valida��o de sal�rios com an�lise de valor limite
	Given que o usu�rio informa o sal�rio <salario>
	When o sistema validar o campo
	Then o sistema deve retornar <resultado>

	Examples:
	|   idade    |  resultado    |
	|   999      |  �invalido�   |
	|   1000     |  �valido�     |
	|   1001     |  �valido�     |
	|   9999     |  �valido�     |
	|   10000    |  �valido�     |
	|   10001    |  �invalido�   |
	


# 2 -�[Particionamento de Equival�ncia]� Um sistema de inscri��o aceita candidatos com idades entre 18 e 60 anos. 
#Identifique pelo menos tr�s parti��es de equival�ncia (v�lida, abaixo do m�nimo, acima do m�ximo) e escreva casos de teste para cada uma. 
#Use o formato Scenario Outline.
# p1 --> entre 18 e 60
# p2 --> menor que 18
# p3 --> maior que 60

Scenario outline: Valida��o de idade com particionamento de equivalencia
	Given que o usu�rio informa a idade <idade>
	When o sistema validar o campo
	Then o sistema deve retornar <resultado>

	Examples:
	|  idade |  resultado   |
	|  25    |  �valido�    |
	|  -1    |  �invalido�  |
	|  61    |  �invalido�  |



# 3 -�[Transi��o de estados]� Um app de fidelidade classifica clientes com base em pontos acumulados: 
# 0�99: Bronze, 100�499: Prata, 500+: Ouro. 
# Crie um cen�rio de transi��o de estados, onde um cliente come�a com 90 pontos, 
# faz compras sucessivas e muda de categoria. 
# Modele os testes em Gherkin.
# p1 0 - 99 ->  Bronze
# p2 100 - 499 -> Prata
# p3 500+ -> Ouro

Scenario outline: Verifica��o de classifica��o por pontos (Transi��o de Estado)
	Given que o cliente possui 90 pontos <pontos_iniciais>
	And est� classificado como �<classificacao_inicial>�
	When o cliente realiza uma compra que concede 25 pontos <pontos_adquiridos>
	Then ele deve ter pontos <pontos_acumulados>
	And sua classifica��o deve mudar para �<classificacao_final>�

	Examples:
	| pontos_iniciais | classificacao_inicial  | pontos_adquiridos | pontos_acumulados | classificacao_final |
	| 90     		  | Bronze		           | 25			       | 115			   | Prata				 |
	| 115     	      | Prata			       | 200		       | 315			   | Prata				 |
	| 315     		  | Prata			       | 250		       | 565			   | Ouro				 |


4 -��[Heur�sticas de Nielsen]�Um sistema de upload de arquivos deve informar visualmente ao usu�rio quando um upload est� em andamento, conclu�do ou falhou. Crie um caso de teste validando a aplica��o da heur�stica de visibilidade do status do sistema durante o upload de arquivos grandes (>100MB).




5 -��[Testing Tours]�Situa��o:�

Um sistema de atendimento via chat online � utilizado por operadores que ficam logados das 08h �s 18h, atendendo m�ltiplos clientes durante o expediente. Crie um caso de teste baseado na heristica  "All-Nighter"
