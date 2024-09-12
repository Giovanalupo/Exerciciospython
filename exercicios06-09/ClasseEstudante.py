import unittest

class TestEstudante(unittest.TestCase):
    def test_calculo_media(self):
        estudante = Estudante("Giovana", [8, 7, 9, 6])
        self.assertEqual(estudante.calcular_media(), 7.5)

if __name__ == "__main__":
    unittest.main()

class Estudante:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
