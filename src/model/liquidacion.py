def calcular_liquidacion_definitiva(salario, dias_trabajados, auxilio_de_transsporte):
    if salario is None or dias_trabajados is None or auxilio_de_transsporte is None:
        raise ValueError("Todos los parámetros son obligatorios.")
    if not isinstance(salario, (int, float)) or not isinstance(dias_trabajados, (int, float)) or not isinstance(auxilio_de_transsporte, (int, float)):
        raise TypeError("Los parámetros deben ser números.")
    if salario < 0:
        raise ValueError("El salario no puede ser negativo.")
    if dias_trabajados < 0:
        raise ValueError("Los días no pueden ser negativos.")
    if auxilio_de_transsporte < 0:
        raise ValueError("El auxilio de transporte no puede ser negativo.")
    base = salario + auxilio_de_transsporte  # salario + auxilio para prima y cesantías
    cesantias = base * dias_trabajados / 360
    intereses_cesantias = cesantias * 0.12 * (dias_trabajados / 360)
    prima = base * dias_trabajados / 360
    vacaciones = salario *  dias_trabajados / 720
    total = cesantias + intereses_cesantias + prima + vacaciones
    return {
        "cesantias": round(cesantias),
        "intereses_cesantias": round(intereses_cesantias),
        "prima": round(prima),
        "vacaciones": round(vacaciones),
        "total":(total)
    }
def retornar_mensaje_salario_integral():
    return "El salario integral no genera prestaciones sociales."