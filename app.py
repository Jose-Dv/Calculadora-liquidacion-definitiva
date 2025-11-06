from flask import Flask, render_template, request
from model.liquidacion import LiquidacionDefinitiva  # Asegúrate de que la ruta sea correcta

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@app.route('/resultado', methods=['GET'])
def resultado():
    # Obtener los parámetros de la URL
    salario = float(request.args.get('salario'))
    dias_trabajados = int(request.args.get('dias_trabajados'))
    auxilio_de_transporte = float(request.args.get('auxilio_de_transporte'))

    # Crear una instancia de LiquidacionDefinitiva y calcular
    liquidacion = LiquidacionDefinitiva(salario, dias_trabajados, auxilio_de_transporte)
    resultado = liquidacion.calcular()

    # Pasar los resultados a la plantilla
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

