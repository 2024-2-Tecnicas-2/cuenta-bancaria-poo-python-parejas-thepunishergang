import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from cuenta_bancaria import CuentaBancaria

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestCalcular(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    def test_ingresar(self):
        mi_cuenta_test = CuentaBancaria("Nathalia", "123547896", 1000000)
        valor_esperado = 1200000
        valor_actual = mi_cuenta_test.ingresar(200000)
        self.assertEqual(valor_esperado, valor_actual)

    def test_segundo_ingresar(self):
        mi_cuenta_test = CuentaBancaria("Nathalia", "123547896", 1500000)
        valor_esperado = 1500000
        valor_actual = mi_cuenta_test.ingresar(-300000)
        self.assertEqual(valor_esperado, valor_actual)

    def test_retirar(self):
        mi_cuenta_test = CuentaBancaria("Nathalia", "123547896", 1000000)
        valor_esperado = 500000
        valor_actual = mi_cuenta_test.retirar(500000)
        self.assertEqual(valor_esperado, valor_actual)

    def test_segundo_retirar(self):
        mi_cuenta_test = CuentaBancaria("Nathalia", "123547896", 1500000)
        valor_esperado = 1500000
        valor_actual = mi_cuenta_test.retirar(-300000)
        self.assertEqual(valor_esperado, valor_actual)

    def test_calcular_interes(self):
        mi_cuenta_test = CuentaBancaria("Nathalia", "123547896", 1000000)
        valor_esperado = 1015000
        valor_actual = mi_cuenta_test.calcular_interes()
        self.assertEqual(valor_esperado, valor_actual)

    def test_segundo_calcular_interes(self):
        mi_cuenta_test = CuentaBancaria("Nathalia", "123547896", 1500000)
        valor_esperado = 1522500
        valor_actual = mi_cuenta_test.calcular_interes()
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()