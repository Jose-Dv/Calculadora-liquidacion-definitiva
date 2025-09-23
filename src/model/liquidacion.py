
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

    @staticmethod
    def mensaje_salario_integral():
        return "El salario integral no genera prestaciones sociales."
