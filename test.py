import unittest
import liquidacion

class TestLiquidacion(unittest.TestCase):

    def test_calcular_liquidacion_definitiva(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(2000000, 365, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 2102854.0, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 252342.48, 2)
        self.assertAlmostEqual(resultado["prima"], 2102854.0, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 833333.33, 2)
        self.assertAlmostEqual(resultado["total"], 5291383.81, 2)

    def test_sin_auxilio_transporte(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(2000000, 365, 0)
        self.assertAlmostEqual(resultado["cesantias"], 2000000.0, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 240000.0, 2)
        self.assertAlmostEqual(resultado["prima"], 2000000.0, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 833333.33, 2)
        self.assertAlmostEqual(resultado["total"], 5033333.33, 2)

    def test_trabajo_medio_tiempo(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(1000000, 180, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 551427.0, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 6617.12, 2)
        self.assertAlmostEqual(resultado["prima"], 551427.0, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 250000.0, 2)
        self.assertAlmostEqual(resultado["total"], 1355471.12, 2)

    def test_renuncia_voluntaria(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(1500000, 90, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 400713.50, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 12021.41, 2)
        self.assertAlmostEqual(resultado["prima"], 400713.50, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 375000.0, 2)
        self.assertAlmostEqual(resultado["total"], 1188448.41, 2)

    def test_salario_integral(self):
        resultado = liquidacion.calculo_salario_integral()
        self.assertEqual(resultado, "El salario integral no genera prestaciones sociales.")

    def test_contrato_menor_a_un_mes(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(1200000, 15, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 54285.58, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 271.43, 2)
        self.assertAlmostEqual(resultado["prima"], 54285.58, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 50000.0, 2)
        self.assertAlmostEqual(resultado["total"], 158842.59, 2)

if __name__ == '__main__':
    unittest.main()
