import datetime
from liquidacion import LiquidacionDefinitiva

class Empleados_liquidados:
    def __init__(
        self,
        cedula,
        nombre,
        fecha_liquidacion,
        salario,
        dias_trabajados,
        auxilio_de_transporte
    ):
        self.cedula = cedula
        self.nombre = nombre
        self.fecha_liquidacion = fecha_liquidacion
        self.salario = salario
        self.dias_trabajados = dias_trabajados
        self.auxilio_de_transporte = auxilio_de_transporte
        # Calcular liquidación
        liquidacion = LiquidacionDefinitiva(salario, dias_trabajados, auxilio_de_transporte)
        resultado = liquidacion.calcular()
        self.cesantias = resultado["cesantias"]
        self.intereses_cesantias = resultado["intereses_cesantias"]
        self.prima = resultado["prima"]
        self.vacaciones = resultado["vacaciones"]
        self.total = resultado["total"]
    def EsIgual(self, otro):
        return (
            self.cedula == otro.cedula and
            self.nombre == otro.nombre and
            self.fecha_liquidacion == otro.fecha_liquidacion and
            self.salario == otro.salario and
            self.dias_trabajados == otro.dias_trabajados and
            self.auxilio_de_transporte == otro.auxilio_de_transporte and
            self.cesantias == otro.cesantias and
            self.intereses_cesantias == otro.intereses_cesantias and
            self.prima == otro.prima and
            self.vacaciones == otro.vacaciones and
            self.total == otro.total
        )