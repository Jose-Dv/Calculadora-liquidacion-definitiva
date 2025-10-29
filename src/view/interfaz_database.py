import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from controller.controlador_liquidacion import Controlador_liquidacion
from model.Empleados_liquidados import Empleados_liquidados

class InterfazDB(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=1, padding=10, spacing=10, **kwargs)

        form = GridLayout(cols=2, spacing=6, size_hint_y=None)
        form.bind(minimum_height=form.setter('height'))

        self.inputs = {}
        campos = [
            ("cedula", "Cédula"),
            ("nombre", "Nombre"),
            ("fecha_liquidacion", "Fecha (YYYY-MM-DD)"),
            ("salario", "Salario"),
            ("dias_trabajados", "Días trabajados"),
            ("auxilio_de_transporte", "Auxilio de transporte")
        ]
        for key, label in campos:
            form.add_widget(Label(text=label))
            ti = TextInput(multiline=False)
            self.inputs[key] = ti
            form.add_widget(ti)

        self.add_widget(form)

        botones = BoxLayout(size_hint_y=None, height=40, spacing=10)
        btn_insert = Button(text="Insertar")
        btn_insert.bind(on_press=self.on_insertar)
        btn_buscar = Button(text="Buscar")
        btn_buscar.bind(on_press=self.on_buscar)
        botones.add_widget(btn_insert)
        botones.add_widget(btn_buscar)
        self.add_widget(botones)

    def popup(self, title, message):
        p = Popup(title=title, content=Label(text=message), size_hint=(.7, .4))
        p.open()

    def on_insertar(self, instance):
        try:
            cedula = self.inputs["cedula"].text.strip()
            nombre = self.inputs["nombre"].text.strip()
            fecha = self.inputs["fecha_liquidacion"].text.strip()
            salario = float(self.inputs["salario"].text.strip())
            dias = int(self.inputs["dias_trabajados"].text.strip())
            aux = float(self.inputs["auxilio_de_transporte"].text.strip())

            empleado = Empleados_liquidados(
                cedula=cedula,
                nombre=nombre,
                fecha_liquidacion=fecha,
                salario=salario,
                dias_trabajados=dias,
                auxilio_de_transporte=aux
            )
            Controlador_liquidacion.Insertar(empleado)
            self.popup("Éxito", "Empleado insertado correctamente.")
        except Exception as e:
            self.popup("Error", f"No se pudo insertar: {e}")

    def on_buscar(self, instance):
        cedula = self.inputs["cedula"].text.strip()
        if not cedula:
            self.popup("Aviso", "Ingrese la cédula a buscar.")
            return
        try:
            encontrado = Controlador_liquidacion.Buscar(cedula)
            if encontrado is None:
                self.popup("Resultado", "No se encontró el empleado.")
                return
            # llenar campos con valores encontrados
            self.inputs["nombre"].text = encontrado.nombre or ""
            self.inputs["fecha_liquidacion"].text = str(encontrado.fecha_liquidacion) or ""
            self.inputs["salario"].text = str(encontrado.salario) or ""
            self.inputs["dias_trabajados"].text = str(encontrado.dias_trabajados) or ""
            self.inputs["auxilio_de_transporte"].text = str(encontrado.auxilio_de_transporte) or ""
            self.popup("Resultado", "Empleado encontrado y cargado en el formulario.")
        except Exception as e:
            self.popup("Error", f"No se pudo buscar: {e}")

class InterfazApp(App):
    def build(self):
        return InterfazDB()

if __name__ == "__main__":
    InterfazApp().run()