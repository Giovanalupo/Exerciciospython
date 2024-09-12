import unittest

class TestFuncionario(unittest.TestCase):
    def test_calculo_inss(self):
        funcionario = Funcionario("Lais", 6000)
        self.assertEqual(funcionario.calcular_inss(), 600)

    def test_inss_abaixo_limite(self):
        funcionario = Funcionario("Luis", 4000)
        self.assertEqual(funcionario.calcular_inss(), 0)

if __name__ == "__main__":
    unittest.main()


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_inss(self):
        if self.salario > 5000:
            return self.salario * 0.10
        return 0
