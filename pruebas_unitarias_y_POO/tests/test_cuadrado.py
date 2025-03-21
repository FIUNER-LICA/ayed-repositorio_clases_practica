# Archivo de test para realizar pruebas unitarias del modulo cuadrado.py

import unittest
# Importa el módulo unittest, que permite crear y ejecutar pruebas unitarias en Python.

from modules.cuadrado import Cuadrado
# Importa la clase Cuadrado desde el módulo 'modules.cuadrado', que será el objeto a probar.

class TestCuadrado(unittest.TestCase):
    # Define una clase de prueba que hereda de unittest.TestCase, lo que permite definir métodos de prueba.

    def test_creacion(self):
        # Prueba la creación de un objeto Cuadrado con un lado válido.
        c = Cuadrado(5)
        self.assertEqual(c.lado, 5)
        # Verifica que el atributo 'lado' del objeto creado sea igual al valor proporcionado (5).

    def test_lado_negativo_error(self):
        # Prueba que intentar crear un Cuadrado con un lado negativo lanza un ValueError.
        with self.assertRaises(ValueError):
            Cuadrado(-3)

    def test_area(self):
        # Prueba el cálculo del área del cuadrado.
        c = Cuadrado(4)
        self.assertAlmostEqual(c.area(), 16, places=3)
        # Verifica que el área calculada sea aproximadamente igual a 16 (lado^2).

    def test_perimetro(self):
        # Prueba el cálculo del perímetro del cuadrado.
        c = Cuadrado(3)
        self.assertAlmostEqual(c.perimetro(), 12, places=3)
        # Verifica que el perímetro calculado sea aproximadamente igual a 12 (4 * lado).

    def test_setter_lado_valido(self):
        # Prueba el setter del atributo 'lado' con un valor válido.
        c = Cuadrado(2)
        c.lado = 10
        self.assertEqual(c.lado, 10)
        # Verifica que el valor del lado se actualice correctamente.

    def test_setter_lado_invalido(self):
        # Prueba el setter del atributo 'lado' con un valor inválido (negativo).
        c = Cuadrado(2)
        with self.assertRaises(ValueError):
            c.lado = -5
        # Verifica que se lance un ValueError al intentar asignar un valor negativo.


unittest.main()
# Ejecuta todas las pruebas definidas en la clase TestCuadrado si el archivo se ejecuta directamente.