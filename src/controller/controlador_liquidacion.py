import sys
sys.path.append( "." )
sys.path.append( "src" )
import psycopg2
import datetime
from src.model.Empleados_liquidados import Empleados_liquidados
class Controlador_liquidacion:
    def CrearCursor():
        conexion = psycopg2.connect(database="clx2",user="clx2_user",password="BDwKNA512qLzvuKr6I0U7itOvVitLhbt",host="dpg-d3dvqmmuk2gs739p1kf0-a",port="5432"
        )
        cursor = conexion.cursor()
        return cursor
    def Insertar(empelado:Empleados_liquidados):
        cursor=Controlador_liquidacion.CrearCursor()
        consulta=f"""""INSERT INTO empleadosliquidados (cedula,nombre,fecha_liquidacion,salario,dias_trabajados,auxilio_de_transporte,cesantias,intereses_cesantias,prima,vacaciones,total)
         VALUES ('{empelado.cedula}','{empelado.nombre}','{empelado.fecha_liquidacion}',{empelado.salario},{empelado.dias_trabajados},{empelado.auxilio_de_transporte},{empelado.cesantias},{empelado.intereses_cesantias},{empelado.prima},{empelado.vacaciones},{empelado.total});"""""
        cursor.execute(consulta)
    def Buscar(cedula:str)->Empleados_liquidados:
        pass


  