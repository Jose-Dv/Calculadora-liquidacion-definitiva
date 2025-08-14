def calcular_liquidacion_definitiva(salario, dias, auxilio):
    # Validaciones
    if salario is None or dias is None or auxilio is None:
        raise ValueError("Todos los parámetros son obligatorios.")
    if not isinstance(salario, (int, float)) or not isinstance(dias, (int, float)) or not isinstance(auxilio, (int, float)):
        raise TypeError("Los parámetros deben ser números.")
    if salario < 0:
        raise ValueError("El salario no puede ser negativo.")
    if dias < 0:
        raise ValueError("Los días no pueden ser negativos.")

    base = salario + auxilio  # salario + auxilio para prima y cesantías
    cesantias = base * dias / 360
    intereses_cesantias = cesantias * 0.12 * (dias / 360)
    prima = base * dias / 360
    vacaciones = salario *  dias / 720
    total = cesantias + intereses_cesantias + prima + vacaciones
    return {
        "cesantias": round(cesantias),
        "intereses_cesantias": round(intereses_cesantias),
        "prima": round(prima, 2),
        "vacaciones": round(vacaciones),
        "total":(total)
    }
def calculo_salario_integral():
    return "El salario integral no genera prestaciones sociales."