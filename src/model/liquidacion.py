
class LiquidacionDefinitiva:
    def __init__(self, salario, dias_trabajados, auxilio_de_transporte):
        if salario is None or dias_trabajados is None or auxilio_de_transporte is None:
            raise ValueError("Todos los parámetros son obligatorios.")
        if not isinstance(salario, (int, float)) or not isinstance(dias_trabajados, (int, float)) or not isinstance(
                auxilio_de_transporte, (int, float)):
            raise TypeError("Los parámetros deben ser números.")
        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        if dias_trabajados < 0:
            raise ValueError("Los días no pueden ser negativos.")
        if auxilio_de_transporte < 0:
            raise ValueError("El auxilio de transporte no puede ser negativo.")

        self.salario = salario
        self.dias_trabajados = dias_trabajados
        self.auxilio_de_transporte = auxilio_de_transporte
        
    @staticmethod
    def calcular_liquidacion_salario_integral(salario, dias_trabajados):

        salario_integral = (salario/30) * dias_trabajados
        vacaciones = (salario * 0.7 * dias_trabajados) / 720
        
        return {
        "salario_pendiente": round(salario_integral, 2),
        "vacaciones": round(vacaciones, 2),
        "nota": "No se liquidan cesantías, intereses ni prima. Solo salario y vacaciones proporcionales."
        }

    def calcular(self):
        base = self.salario + self.auxilio_de_transporte  # salario + auxilio para prima y cesantías
        cesantias = base * self.dias_trabajados / 360
        intereses_cesantias = cesantias * 0.12 * (self.dias_trabajados / 360)
        prima = base * self.dias_trabajados / 360
        vacaciones = self.salario * self.dias_trabajados / 720
        total = cesantias + intereses_cesantias + prima + vacaciones

        return {
            "cesantias": round(cesantias),
            "intereses_cesantias": round(intereses_cesantias),
            "prima": round(prima),
            "vacaciones": round(vacaciones),
            "total": round(total)
        }


