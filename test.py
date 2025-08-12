import unittest
import liquidacion
class TestLiquidacion(unittest.TestCase):
    def test_calcular_liquidacion_definitiva(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(2000000, 365, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 2120854.0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 252343)
        self.assertAlmostEqual(resultado["prima"], 2102854)
        self.assertAlmostEqual(resultado["vacaciones"], 1000000)
        self.assertAlmostEqual(resultado["total"], 5458050)
def test_sin_auxilio_transporte(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(2000000, 365, 0)
        self.assertAlmostEqual(resultado["cesantias"], 2000000.0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 240000.0)
        self.assertAlmostEqual(resultado["prima"], 2000000.0)
        self.assertAlmostEqual(resultado["vacaciones"], 2000000.0)
        self.assertAlmostEqual(resultado["total"], 6440000.0)
def trabajo_medio_tiempo(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(1000000,180,102854)
        self.assertAlmostEqual(resultado["cesantias"], 1051427.0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 126171.0)
        self.assertAlmostEqual(resultado["prima"], 1051427.0)
        self.assertAlmostEqual(resultado["vacaciones"], 500000.0)
        self.assertAlmostEqual(resultado["total"], 2720025.0)
#En caso de renuncia voluntaria, se debe calcular la liquidación definitiva igualmente, aplica todas las prestaciones sociales.
#Caso de prueba normal
def renuncia_voluntaria(self):
      resultado = liquidacion.calcular_liquidacion_definitiva(1500000, 90, 102854)
      self.assertAlmostEqual(resultado["cesantias"], 400713.50, 3)
      self.assertAlmostEqual(resultado["intereses_cesantias"], 12021.41,3)
      self.assertAlmostEqual(resultado["prima"], 400713.50, 3)
      self.assertAlmostEqual(resultado["vacaciones"], 675000,3)
      self.assertAlmostEqual(resultado["total"], 875958.41,3)
def salario_integral(self):
        resultado = liquidacion.calculo_salario_integral()
        self.assertEqual(resultado, "El salario integral no genera prestaciones sociales.")
if __name__ == '__main__':
    unittest.main()