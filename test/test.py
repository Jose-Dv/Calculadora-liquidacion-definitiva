
import unittest
import sys
sys.path.append("src")
from model.liquidacion import LiquidacionDefinitiva

class TestLiquidacion(unittest.TestCase):

    def test_solo_un_dia_trabajado(self):
        # Crear una instancia de la clase LiquidacionDefinitiva
        liquidacion = LiquidacionDefinitiva(1000000, 1, 0)
        resultado = liquidacion.calcular()

        self.assertAlmostEqual(resultado["cesantias"], 2778, 0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 1, 0)
        self.assertAlmostEqual(resultado["prima"], 2778, 0)
        self.assertAlmostEqual(resultado["vacaciones"], 1389, 2)
        self.assertAlmostEqual(resultado["total"], 6945, 0)

    def test_calcular_liquidacion_definitiva(self):
        liquidacion = LiquidacionDefinitiva(2000000, 365, 102854)
        resultado = liquidacion.calcular()

        self.assertAlmostEqual(resultado["cesantias"], 2132060, 0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 259401, 2)
        self.assertAlmostEqual(resultado["prima"], 2132060, 0)
        self.assertAlmostEqual(resultado["vacaciones"], 1013889, 2)
        self.assertAlmostEqual(resultado["total"], 5537410, 0)

    def test_sin_auxilio_transporte(self):
        liquidacion = LiquidacionDefinitiva(1500000, 180, 0)
        resultado = liquidacion.calcular()

        self.assertAlmostEqual(resultado["cesantias"], 750000, 0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 45000, 0)
        self.assertAlmostEqual(resultado["prima"], 750000, 0)
        self.assertAlmostEqual(resultado["vacaciones"], 375000, 0)
        self.assertAlmostEqual(resultado["total"], 1920000, 0)

    def test_trabajo_medio_tiempo(self):
        liquidacion = LiquidacionDefinitiva(1000000, 120, 102854)
        resultado = liquidacion.calcular()

        self.assertAlmostEqual(resultado["cesantias"], 367618, 0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 14705, 2)
        self.assertAlmostEqual(resultado["prima"], 367618, 0)
        self.assertAlmostEqual(resultado["vacaciones"], 166667, 2)
        self.assertAlmostEqual(resultado["total"], 916607, 0)

    def test_renuncia_voluntaria(self):
        liquidacion = LiquidacionDefinitiva(3000000, 200, 102854)
        resultado = liquidacion.calcular()

        self.assertAlmostEqual(resultado["cesantias"], 1723808, 0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 114921, 0)
        self.assertAlmostEqual(resultado["prima"], 1723808, 0)
        self.assertAlmostEqual(resultado["vacaciones"], 833333, 0)
        self.assertAlmostEqual(resultado["total"], 4395869, 0)

    def test_contrato_menor_a_un_mes(self):
        liquidacion = LiquidacionDefinitiva(1200000, 15, 102854)
        resultado = liquidacion.calcular()

        self.assertAlmostEqual(resultado["cesantias"], 54285.63, 0)
        self.assertAlmostEqual(resultado["intereses_cesantias"], 271.43, 0)
        self.assertAlmostEqual(resultado["prima"], 54285.63, 0)
        self.assertAlmostEqual(resultado["vacaciones"], 25000, 0)
        self.assertAlmostEqual(resultado["total"], 133843, 0)

    def test_salario_negativo(self):
        with self.assertRaises(ValueError) as context:
            liquidacion = LiquidacionDefinitiva(-1000000, 30, 102854)
            liquidacion.calcular()  # Llamamos al método calcular
        self.assertEqual(str(context.exception), "El salario no puede ser negativo.")

    def test_dias_negativos(self):
        with self.assertRaises(ValueError) as context:
            liquidacion = LiquidacionDefinitiva(1000000, -30, 102854)
            liquidacion.calcular()  # Llamamos al método calcular
        self.assertEqual(str(context.exception), "Los días no pueden ser negativos.")

    def test_parametros_faltantes(self):
        with self.assertRaises(ValueError) as context:
            liquidacion = LiquidacionDefinitiva(None, 30, 102854)
            liquidacion.calcular()  # Llamamos al método calcular
        self.assertEqual(str(context.exception), "Todos los parámetros son obligatorios.")

    def test_auxilio_negativo(self):
        with self.assertRaises(ValueError) as context:
            liquidacion = LiquidacionDefinitiva(1000000, 30, -102854)
            liquidacion.calcular()  # Llamamos al método calcular
        self.assertEqual(str(context.exception), "El auxilio de transporte no puede ser negativo.")

if __name__ == '__main__':
    unittest.main()
