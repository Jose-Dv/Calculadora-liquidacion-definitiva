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
        consulta=f"""select cedula,nombre,fecha_liquidacion,salario,dias_trabajados,auxilio_de_transporte,cesantias,intereses_cesantias,prima,vacaciones,total
        from empleadosliquidados where cedula='{cedula}';"""
        cursor.execute(consulta)
        datos=cursor.fetchone()
        if datos!=None:
            empleado=Empleados_liquidados(cedula=datos[0],nombre=datos[1],fecha_liquidacion=datos[2],salario=datos[3],dias_trabajados=datos[4],auxilio_de_transporte=datos[5],cesantias=datos[6],intereses_cesantias=datos[7],prima=datos[8],vacaciones=datos[9],total=datos[10])
            return empleado
        else:
            return None



  