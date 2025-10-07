# Calculadora-liquidacion-definitiva
Video explicacion experto: https://drive.google.com/file/d/1c9Oo18Vego88zhcTV-6tEkw6AILwgGP_/view?usp=drive_link, https://drive.google.com/file/d/1Sn2my1YLyh8yll2mgTRcAMYdJwrQz8Hm/view?usp=drive_link
## 👨‍💻 Autores
Jose manuel Diaz Villa


Isaac Daniel Mosquera

Samuel Duran

## Autores Gui

Juan José Ocampo Gómez



David Garcia Villanueva

## 📋 Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar un **Liquidador de Nómina**, una herramienta capaz de calcular automáticamente los pagos que un empleador debe realizar a sus trabajadores, teniendo en cuenta factores como:
- Salario base  
- Auxilio de transporte  
- Dias trabajados  
La aplicación permite **automatizar el cálculo**,de tu liquidacion en caso de renuncia o salida de una empresa, para mas informacion consultar el video explicativo.
---
## 🎯 Objetivos
- Automatizar el proceso de cálculo de liquidacion para exempleados.  
- Implementar fórmulas y reglas legales relacionadas con salarios, prestaciones y deducciones.    
- Diseñar una interfaz amigable para ingresar y visualizar información.  
---
## ⚙️ Funcionalidades Principales
- ✅ Cálculo del total a pagar por liquidacion segun el contrato
- ✅ Calculo de las prestaciones a pagar que componen la liquidacion.  
- ✅ Cálculo de deducciones legales: salud, pensión, fondo de solidaridad.  
- ✅ Cálculo de prestaciones sociales: prima, cesantías, intereses de cesantías, vacaciones.  
---
## 📥 Variables de Entrada
- `salario_base` (numérico): Salario mensual base del empleado.  
- `auxilio_transporte` (numérico): Auxilio de transporte según ley vigente.  
- `dias trabajados` (numerico): Dias establecidos en el contrato
---
## 📤 Variables de Salida
- `Lquidacion total`(numérico):Total de la deuda a pagar por parte de la empresa.
  `Cesantias`(numérico):prestación social a la que tiene derecho todo trabajador que tenga un contrato laboral.
  `Intereses a las cesantias`
  `Prima`(numérico): retribución que hace el empleador por los beneficios económicos y sociales que obtiene del trabajador
  `Vacaciones no pagas`(numérico):dias no pagos de las vacaciones
---
## 🖥️ Ejecución del Programa
### 1. Clonar el Repositorio
```bash
git clone git@github.com:Jose-Dv/Calculadora-liquidacion-definitiva.git
```
### 2. Navegar al Repositorio
```bash
cd d:\Documentos\Programación\Proyectos\Calculadora-liquidacion-definitiva
```
Recuerda donde clonaste el repossitorio
### 3. Ejecutar la interfaz
```bash
python src/view/interfaz.py
```
## 📦 Requisitos

Python 3.7 o superior

Sistema operativo: Windows
# Liquidador de Nómina Definitivo (Kivy)

Aplicación gráfica desarrollada en **Python + Kivy** para calcular la nómina de un empleado según diferentes parámetros como salario base, horas extras, tipo de hora, préstamos, cuotas e intereses.

---

## Requisitos

- Python 3.7 o superior
- Kivy (`pip install kivy`)
---

## Instrucciones para ejecutar

1. **Clona o descarga el proyecto**

2. **Instala las dependencias**

```bash
pip install kivy
```

3. **Ejecuta la aplicación**

- Desde la raíz del proyecto, corre:

```bash
python src/view/ViewGui/interfaz_gui.py
```
.

 

