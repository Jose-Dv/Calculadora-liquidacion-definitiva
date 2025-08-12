Salario:float=2000000
dias_trabajados:int=365
auxilio_transporte:float=102854
def calcular_liquidacion_definitiva(salario, dias, auxilio):
    base = salario + auxilio
    cesantias = base * dias / 360
    intereses_cesantias = cesantias * 0.12 * dias / 360
    prima = base * dias / 360
    vacaciones = salario * 15 * dias / (360 * 360)
    total = cesantias + intereses_cesantias + prima + vacaciones
    return {
        "cesantias": cesantias,
        "intereses_cesantias": intereses_cesantias,
        "prima": prima,
        "vacaciones": vacaciones,
        "total": total
    }