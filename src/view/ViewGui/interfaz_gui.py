import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from model.liquidacion import LiquidacionDefinitiva


class LiquidacionApp(App):
    def build(self):
        self.title = "Calculadora de Liquidación Definitiva"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input: ¿Salario integral?
        layout.add_widget(Label(text="¿Cuenta con salario integral? (si/no):"))
        self.input_integral = TextInput(multiline=False)
        layout.add_widget(self.input_integral)

        # Input: salario
        layout.add_widget(Label(text="Salario mensual:"))
        self.input_salario = TextInput(multiline=False, input_filter='float')
        layout.add_widget(self.input_salario)

        # Input: días trabajados
        layout.add_widget(Label(text="Días trabajados:"))
        self.input_dias = TextInput(multiline=False, input_filter='int')
        layout.add_widget(self.input_dias)

        # Input: auxilio de transporte
        layout.add_widget(Label(text="Auxilio de transporte (0 si no aplica):"))
        self.input_auxilio = TextInput(multiline=False, input_filter='float')
        layout.add_widget(self.input_auxilio)

        # Botón para calcular
        calcular_btn = Button(text="Calcular Liquidación", size_hint=(1, 0.2))
        calcular_btn.bind(on_press=self.calcular_liquidacion)
        layout.add_widget(calcular_btn)

        return layout

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(0.8, 0.4))
        popup.open()

    def calcular_liquidacion(self, instance):
        try:
            respuesta = self.input_integral.text.strip().lower()
            if respuesta == "si":
                mensaje = LiquidacionDefinitiva.mensaje_salario_integral()
                self.mostrar_popup("Resultado", mensaje)
                return

            salario = float(self.input_salario.text)
            dias = int(self.input_dias.text)
            auxilio = float(self.input_auxilio.text)

            liquidacion = LiquidacionDefinitiva(salario, dias, auxilio)
            resultado = liquidacion.calcular()

            mensaje = (
                f"Cesantías: {resultado['cesantias']}\n"
                f"Intereses de Cesantías: {resultado['intereses_cesantias']}\n"
                f"Prima: {resultado['prima']}\n"
                f"Vacaciones: {resultado['vacaciones']}\n"
                f"Total: {resultado['total']}"
            )
            self.mostrar_popup("Liquidación Calculada", mensaje)

        except ValueError as ve:
            self.mostrar_popup("Error de Validación", str(ve))
        except Exception:
            self.mostrar_popup("Error", "Datos ingresados inválidos.")


if __name__ == '__main__':
    LiquidacionApp().run()
