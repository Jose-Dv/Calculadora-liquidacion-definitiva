import unittest
import liquidacion

class TestLiquidacion(unittest.TestCase):

    def test_calcular_liquidacion_definitiva(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(2000000, 365, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 2134393.81, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 259964.46, 2)
        self.assertAlmostEqual(resultado["prima"], 2134393.81, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 304861.11, 2)
        self.assertAlmostEqual(resultado["total"], 4833613.19, 2)
    def test_sin_auxilio_transporte(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(2000000, 365, 0)
        self.assertAlmostEqual(resultado["cesantias"], 2027777.78, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 243333.33, 2)
        self.assertAlmostEqual(resultado["prima"], 2027777.78, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 304861.11, 2)
        self.assertAlmostEqual(resultado["total"], 4603750.00, 2)
    def test_trabajo_medio_tiempo(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(1000000, 180, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 551427.00, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 33086.03, 2)
        self.assertAlmostEqual(resultado["prima"], 551427.00, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 75000.00, 2)
        self.assertAlmostEqual(resultado["total"], 1210940.03, 2)
    def test_renuncia_voluntaria(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(1500000, 90, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 400713.50, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 12021.41, 2)
        self.assertAlmostEqual(resultado["prima"], 400713.50, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 56250.00, 2)
        self.assertAlmostEqual(resultado["total"], 869698.41, 2)
    def test_contrato_menor_a_un_mes(self):
        resultado = liquidacion.calcular_liquidacion_definitiva(1200000, 15, 102854)
        self.assertAlmostEqual(resultado["cesantias"], 54285.63, 2)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 271.43, 2)
        self.assertAlmostEqual(resultado["prima"], 54285.63, 2)
        self.assertAlmostEqual(resultado["vacaciones"], 7500.00, 2)
        self.assertAlmostEqual(resultado["total"], 116342.69, 2)
    # Test excepciones
    def test_salario_negativo(self):
        with self.assertRaises(ValueError) as context:
            liquidacion.calcular_liquidacion_definitiva(-1000000, 30, 102854)
        self.assertEqual(str(context.exception), "El salario no puede ser negativo.")
    def test_dias_negativos(self):
        with self.assertRaises(ValueError) as context:
            liquidacion.calcular_liquidacion_definitiva(1000000, -30, 102854)
        self.assertEqual(str(context.exception), "Los días no pueden ser negativos.")

    def test_parametros_faltantes(self):
        with self.assertRaises(ValueError) as context:
            liquidacion.calcular_liquidacion_definitiva(None, 30, 102854)
        self.assertEqual(str(context.exception), "Todos los parámetros son obligatorios.")

if __name__ == '__main__':
    unittest.main()
