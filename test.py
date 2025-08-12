import unittest
import liquidacion
class TestLiquidacion(unittest.TestCase):
    def test_calcular_liquidacion_definitiva(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(2000000, 365, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 2040000.0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 245000.0)
        self.assertAlmostEqual(resultado["prima"], 2040000.0)
        self.assertAlmostEqual(resultado["vacaciones"], 2040000.0)
        self.assertAlmostEqual(resultado["total"], 6585000.0)
def test_sin_auxilio_transporte(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(2000000, 365, 0)
        self.assertAlmostEqual(resultado["cesantias"], 2000000.0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 240000.0)
        self.assertAlmostEqual(resultado["prima"], 2000000.0)
        self.assertAlmostEqual(resultado["vacaciones"], 2000000.0)
        self.assertAlmostEqual(resultado["total"], 6440000.0)
if __name__ == '__main__':
    unittest.main()