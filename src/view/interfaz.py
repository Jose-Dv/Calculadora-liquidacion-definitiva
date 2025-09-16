import sys
sys.path.append("src")
from model.liquidacion import calcular_liquidacion_definitiva
from model.liquidacion import retornar_mensaje_salario_integral
input("Bienvenido a la calculadora de liquidación definitiva , uste cuenta con salario integral?")
respuesta=input("Si o No: ").lower()
if respuesta == "si":
    print(retornar_mensaje_salario_integral())
else:
    try:
        salario = float(input("Ingrese su salario mensual: "))
        dias = int(input("Ingrese los días trabajados: "))
        auxilio = float(input("Ingrese el auxilio de transporte (0 si no aplica): "))
        resultado = calcular_liquidacion_definitiva(salario, dias, auxilio)
        print("Liquidación definitiva calculada:")
        print(f"Cesantías: {resultado['cesantias']}")
        print(f"Intereses de cesantías: {resultado['intereses_cesantias']}")
        print(f"Prima: {resultado['prima']}")
        print(f"Vacaciones: {resultado['vacaciones']}")
        print(f"Total: {resultado['total']}")
    except ValueError as e:
        print(f"Error en los datos ingresados,porfavor no ingresar numeros negativos")
    except Exception as e:
        print(f"Error inesperado:datos ingresados invalidos")