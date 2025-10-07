
import sys

sys.path.append("src")
from model import LiquidacionDefinitiva

input("Bienvenido a la calculadora de liquidación definitiva, ¿usted cuenta con salario integral?")
respuesta = input("Si o No: ").lower()

if respuesta == "si":
    print(LiquidacionDefinitiva.mensaje_salario_integral())
else:
    try:
        salario = float(input("Ingrese su salario mensual: "))
        dias = int(input("Ingrese los días trabajados: "))
        auxilio = float(input("Ingrese el auxilio de transporte (0 si no aplica): "))

        # Crear una instancia de la clase LiquidacionDefinitiva
        liquidacion = LiquidacionDefinitiva(salario, dias, auxilio)

        # Calcular la liquidación
        resultado = liquidacion.calcular()

        # Mostrar los resultados
        print("Liquidación definitiva calculada:")
        print(f"Cesantías: {resultado['cesantias']}")
        print(f"Intereses de cesantías: {resultado['intereses_cesantias']}")
        print(f"Prima: {resultado['prima']}")
        print(f"Vacaciones: {resultado['vacaciones']}")
        print(f"Total: {resultado['total']}")

    except ValueError as e:
        print(f"Error en los datos ingresados: por favor no ingrese números negativos.")
    except Exception as e:
        print(f"Error inesperado: {e}")
