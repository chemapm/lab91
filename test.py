import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(sumar(3, "2"), "Ambos argumentos deben ser números enteros")
        self.assertEqual(sumar(5.5, 3), "Ambos argumentos deben ser números enteros")
        
    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)
        self.assertEqual(restar(5.5, 3), "Ambos argumentos deben ser números enteros")
        self.assertEqual(restar(3, "2"), "Ambos argumentos deben ser números enteros")
        
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)
        self.assertEqual(multiplicar("3", 2), "Ambos argumentos deben ser números enteros")
        self.assertEqual(multiplicar(3, 2.5), "Ambos argumentos deben ser números enteros")
        
    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-10, 2), -5)
        self.assertEqual(dividir(5, 0), "No se puede dividir por cero")
        self.assertEqual(dividir(10, "2"), "Ambos argumentos deben ser números enteros")
        self.assertEqual(dividir(10.5, 2), "Ambos argumentos deben ser números enteros")

if __name__ == '__main__':
    unittest.main()