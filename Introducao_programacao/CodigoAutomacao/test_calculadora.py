import pytest
from calculadora import Calculadora

class TestCalculadora:
    
    def setup_method(self):
        self.calc = Calculadora()

    def test_somar(self):
        assert self.calc.somar(3,7) == 10

    def test_divisao_por_zero(self):
        with pytest.raises(ValueError):
            self.calc.dividir(10,0)