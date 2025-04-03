import unittest
# Importa el módulo unittest, que permite crear y ejecutar pruebas unitarias en Python.

from modules.cilindro import Cilindro
# Importa la clase Cilindro desde el módulo 'modules.cilindro', que será el objeto a probar.

class TestCilindro(unittest.TestCase):
    # Define una clase de prueba que hereda de unittest.TestCase, lo que permite definir métodos de prueba.

    def test_creacion(self):
        # Prueba la creación de un objeto Cilindro con valores válidos para el radio y la altura.
        cilindro = Cilindro(radio=2, altura=5)
        self.assertEqual(cilindro.radio, 2)
        # Verifica que el atributo 'radio' del cilindro sea igual al valor proporcionado (2).
        self.assertEqual(cilindro.altura, 5)
        # Verifica que el atributo 'altura' del cilindro sea igual al valor proporcionado (5).

    def test_radio_negativo_error(self):
        # Prueba que intentar crear un Cilindro con un radio negativo lanza un ValueError.
        with self.assertRaises(ValueError):
            Cilindro(radio=-1, altura=5)

    def test_altura_negativa_error(self):
        # Prueba que intentar crear un Cilindro con una altura negativa lanza un ValueError.
        with self.assertRaises(ValueError):
            Cilindro(radio=3, altura=-2)

    def test_setear_radio_invalido(self):
        # Prueba el setter del atributo 'radio' con un valor inválido (negativo).
        cilindro = Cilindro(radio=3, altura=5)
        with self.assertRaises(ValueError):
            cilindro.radio = -2
        # Verifica que se lance un ValueError al intentar asignar un valor negativo al radio.

    def test_setear_altura_invalida(self):
        # Prueba el setter del atributo 'altura' con un valor inválido (negativo).
        cilindro = Cilindro(radio=3, altura=5)
        with self.assertRaises(ValueError):
            cilindro.altura = -3
        # Verifica que se lance un ValueError al intentar asignar un valor negativo a la altura.

    def test_volumen(self):
        # Prueba el cálculo del volumen del cilindro.
        cilindro = Cilindro(radio=3, altura=5)
        # El volumen se calcula como π * r² * h.
        esperado = 3.14159 * 3**2 * 5
        self.assertAlmostEqual(cilindro.volumen(), esperado, places=3)
        # Verifica que el volumen calculado sea aproximadamente igual al valor esperado.

    def test_area_superficial(self):
        # Prueba el cálculo del área superficial del cilindro.
        cilindro = Cilindro(radio=2, altura=4)
        # El área superficial se calcula como 2πr(r + h).
        esperado = 2 * 3.14159 * 2 * (2 + 4)
        self.assertAlmostEqual(cilindro.area_superficial(), esperado, places=3)
        # Verifica que el área superficial calculada sea aproximadamente igual al valor esperado.

if __name__ == "__main__":
    unittest.main()
    # Ejecuta todas las pruebas definidas en la clase TestCilindro si el archivo se ejecuta directamente.