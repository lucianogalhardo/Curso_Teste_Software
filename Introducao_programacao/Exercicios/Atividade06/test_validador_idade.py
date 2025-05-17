import pytest
from validador_idade import ValidadorIdade

class TestValidadorIdade:
    def setup_method(self):
        self.validador = ValidadorIdade()

    ## Testes utilizando particionamento de equivalência
    def test_idade_abaixo_13(self):
        assert self.validador.validar_idade(10) == "Cadastro não permitido"

    def test_idade_entre_13_e_18(self):
        assert self.validador.validar_idade(15) == "Necessário consentimento dos pais"

    def test_idade_acima_18(self):
        assert self.validador.validar_idade(21) == "Cadastro liberado"

    ## Testes utilizando análise de valor limite
    def test_idade_negativa(self):
        with pytest.raises(ValueError):
            self.validador.validar_idade(-1)

    def test_idade_fora_limite(self):
        with pytest.raises(ValueError):
            self.validador.validar_idade(210)
    
    ## Testes valores não numéricos (inválidos)
    def test_idade_nao_numerica(self):
        with pytest.raises(ValueError):
            self.validador.validar_idade("vinte")


