def calcular_liquidacion_definitiva(salario, dias, auxilio):
    base = salario + auxilio  # salario + auxilio para prima y cesantías
    cesantias = base * dias / 360
    intereses_cesantias = cesantias * 0.12 * dias / 360
    prima = base * dias / 360
    vacaciones = salario * 15 * dias / 360  # corregido
    total = cesantias + intereses_cesantias + prima + vacaciones
    return {
        "cesantias": round(cesantias, 2),
        "intereses_cesantias": round(intereses_cesantias, 2),
        "prima": round(prima, 2),
        "vacaciones": round(vacaciones, 2),
        "total": round(total, 2)
    }