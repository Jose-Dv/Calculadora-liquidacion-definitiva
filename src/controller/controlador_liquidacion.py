import sys
sys.path.append(".")
sys.path.append("src")
import psycopg2
import datetime
from src.model.Empleados_liquidados import Empleados_liquidados
import secret_config

class Controlador_liquidacion:
    @staticmethod
    def Crear_conexion():
        conexion = psycopg2.connect(database=secret_config.DATABASE,
                                    user=secret_config.USER,
                                    password=secret_config.PASSWORD,
                                    host=secret_config.HOST,
                                    port=secret_config.PORT)
        cursor = conexion.cursor()
        return conexion, cursor

    @staticmethod
    def Insertar(empelado: Empleados_liquidados):
        conexion, cursor = Controlador_liquidacion.Crear_conexion()
        consulta = """
        INSERT INTO empleadosliquidados
        (cedula,nombre,fecha_liquidacion,salario,dias_trabajados,auxilio_de_transporte,cesantias,intereses_cesantias,prima,vacaciones,total)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        params = (
            empelado.cedula,
            empelado.nombre,
            empelado.fecha_liquidacion,
            empelado.salario,
            empelado.dias_trabajados,
            empelado.auxilio_de_transporte,
            empelado.cesantias,
            empelado.intereses_cesantias,
            empelado.prima,
            empelado.vacaciones,
            empelado.total
        )
        cursor.execute(consulta, params)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def Buscar(cedula: str) -> Empleados_liquidados:
        conexion, cursor = Controlador_liquidacion.Crear_conexion()
        consulta = """
        SELECT cedula,nombre,fecha_liquidacion,salario,dias_trabajados,auxilio_de_transporte,cesantias,intereses_cesantias,prima,vacaciones,total
        FROM empleadosliquidados WHERE cedula=%s;
        """
        cursor.execute(consulta, (cedula,))
        datos = cursor.fetchone()
        cursor.close()
        conexion.close()
        if datos is not None:
            empleado = Empleados_liquidados(
                cedula=datos[0],
                nombre=datos[1],
                fecha_liquidacion=str(datos[2]),
                salario=datos[3],
                dias_trabajados=datos[4],
                auxilio_de_transporte=datos[5],
                cesantias=datos[6],
                intereses_cesantias=datos[7],
                prima=datos[8],
                vacaciones=datos[9],
                total=datos[10]
            )
            return empleado
        else:
            return None

Pruebainsertar=Empleados_liquidados(
    cedula="1515151515",
    nombre="empleado prueba",
    fecha_liquidacion="2024-03-03",
    salario=1000000,
    dias_trabajados=30,
    auxilio_de_transporte=102854
)
Controlador_liquidacion.Insertar(Pruebainsertar)


