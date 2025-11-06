import sys 
sys.path.append("src")
import unittest
from model.Empleados_liquidados import Empleados_liquidados
from controller.controlador_liquidacion import Controlador_liquidacion

class TestDbEmpleados(unittest.TestCase):
    def CreacionEmpleado(self):
        # Datos de prueba que usaremos en varios tests
        self.empleado_prueba = Empleados_liquidados(
            cedula="1010101010",
            nombre="empleado prueba",
            fecha_liquidacion="2023-10-10",
            salario=1000000,
            dias_trabajados=30,
            auxilio_de_transporte=102854
        )
    def test_crear_tabla(self):
            resultado = Controlador_liquidacion.Crear_tabla()
            self.assertTrue(resultado)
    def test_insertar_y_buscar_exitoso(self):
        Controlador_liquidacion.Eliminar(self.empleado_prueba.cedula)
        Controlador_liquidacion.Insertar(self.empleado_prueba)
        empleado_encontrado = Controlador_liquidacion.Buscar(self.empleado_prueba.cedula)
        self.assertTrue(self.empleado_prueba.EsIgual(empleado_encontrado))
    def test_buscar_no_existente(self):
        Controlador_liquidacion.Eliminar("999999999")
        resultado = Controlador_liquidacion.Buscar("999999999")
        self.assertIsNone(resultado)
    def test_insertar_duplicado(self):
        Controlador_liquidacion.Insertar(self.empleado_prueba)
        with self.assertRaises(Exception):
            Controlador_liquidacion.Insertar(self.empleado_prueba)
    def test_eliminar_exitoso(self):
        Controlador_liquidacion.Insertar(self.empleado_prueba)
        resultado = Controlador_liquidacion.Eliminar(self.empleado_prueba.cedula)
        self.assertTrue(resultado)
        empleado = Controlador_liquidacion.Buscar(self.empleado_prueba.cedula)
        self.assertIsNone(empleado)
    def test_eliminar_no_existente(self):
        # Intentamos eliminar una cédula que no existe
        resultado = Controlador_liquidacion.Eliminar("999999999")
        self.assertFalse(resultado)
    def Textfixture(self):
        """Limpieza después de cada prueba"""
        Controlador_liquidacion.Eliminar(self.empleado_prueba.cedula)
if __name__ == '__main__':
    unittest.main()



