import sys
sys.path.append( "." )
sys.path.append( "src" )
import psycopg2
import datetime
from src.model.Empleados_liquidados import Empleados_liquidados
import secret_config
class Controlador_liquidacion:
    def Crear_cursor():
        conexion = psycopg2.connect(database=secret_config.DATABASE,
                                    user=secret_config.USER,
                                    password=secret_config.PASSWORD,
                                    host=secret_config.HOST,
                                    port=secret_config.PORT)
        cursor = conexion.cursor()
        return cursor
    def Insertar(empelado:Empleados_liquidados):
        cursor=Controlador_liquidacion.Crear_cursor()
        consulta=f"""""INSERT INTO empleadosliquidados (cedula,nombre,fecha_liquidacion,salario,dias_trabajados,auxilio_de_transporte,cesantias,intereses_cesantias,prima,vacaciones,total)
         VALUES ('{empelado.cedula}','{empelado.nombre}','{empelado.fecha_liquidacion}',{empelado.salario},{empelado.dias_trabajados},{empelado.auxilio_de_transporte},{empelado.cesantias},{empelado.intereses_cesantias},{empelado.prima},{empelado.vacaciones},{empelado.total});"""""
        cursor.execute(consulta)
    def Buscar(cedula:str)->Empleados_liquidados:
        cursor=Controlador_liquidacion.Crear_cursor()
        consulta=f"""select * from empleadosliquidados where cedula='{cedula}';"""
        cursor.execute(consulta)
        datos=cursor.fetchone()


  