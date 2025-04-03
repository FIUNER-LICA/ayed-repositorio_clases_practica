import unittest
import math
from modules.piramide import Piramide

class TestPiramide(unittest.TestCase):
    def test_creacion_piramide(self):
        piramide = Piramide(base_longitud=4, altura=6)
        self.assertEqual(piramide.base_longitud, 4)
        self.assertEqual(piramide.altura, 6)
    
    def test_base_longitud_negativo_error(self):
        with self.assertRaises(ValueError):
            Piramide(base_longitud=-2, altura=5)
    
    def test_altura_negativa_error(self):
        with self.assertRaises(ValueError):
            Piramide(base_longitud=3, altura=-4)

    def test_setear_base_longitud_invalido(self):
        piramide = Piramide(base_longitud=3, altura=5)
        with self.assertRaises(ValueError):
            piramide.base_longitud = -2

    def test_setear_altura_invalida(self):
        piramide = Piramide(base_longitud=3, altura=5)
        with self.assertRaises(ValueError):
            piramide.altura = -5
    
    def test_volumen(self):
        piramide = Piramide(base_longitud=5, altura=10)
        L = piramide.base_longitud
        h = piramide.altura
        # Volumen = (L² * h) / 3
        esperado = (L ** 2 * h) / 3
        self.assertAlmostEqual(piramide.volumen(), esperado, places=3)
    
    def test_area_superficial(self):
        piramide = Piramide(base_longitud=4, altura=6)
        L = piramide.base_longitud
        h = piramide.altura

        # A = L * (L + math.sqrt(4*h² + (L/2)²))
        esperado = L * (L + math.sqrt(4*h**2 + (L/2)**2))
        self.assertAlmostEqual(piramide.area_superficial(), esperado, places=3)


if __name__ == '__main__':
    unittest.main()