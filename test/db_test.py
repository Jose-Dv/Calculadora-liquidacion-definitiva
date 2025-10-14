import sys 
sys.path.append("src")
import unittest
from src.model.Empleados_liquidados import Empleados_liquidados
from src.controller.controlador_liquidacion import Controlador_liquidacion
class TestDbEmpleados(unittest.TestCase):
    def insertar_y_buscar_en_DB(self):
        empleadoprueba=Empleados_liquidados(
            cedula="1010101010",
            nombre="empleado prueba",
            fecha_liquidacion="2023-10-10",
            salario=1000000,
            dias_trabajados=30,
            auxilio_de_transporte=102854
        )
        Controlador_liquidacion.Insertar(empleadoprueba)
        empleadoencontrado=Controlador_liquidacion.Buscar("1010101010")
        self.assertTrue(empleadoprueba.EsIgual(empleadoencontrado))
      


