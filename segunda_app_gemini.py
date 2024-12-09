from datetime import datetime, date
import streamlit as st
import re

# Funciones para validación
def validar_nombre(nombre):
    patron = r'^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)*$'
    return bool(re.match(patron, nombre))

def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))

def validar_telefono(telefono):
    patron = r'^\+57\s3\d{2}\s\d{3}\s\d{4}$'
    return bool(re.match(patron, telefono))

def validar_fecha_nacimiento(fecha_nacimiento):
    hoy = date.today()
    edad_minima = 0  # No puede ser una fecha futura
    edad_maxima = 120  # Supongamos un límite razonable para la edad
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad_minima <= edad <= edad_maxima

# Interfaz de Streamlit
st.title("Validación de Datos en Formularios")
st.write("Por favor, completa los campos a continuación en el formato indicado:")

# Entradas del formulario
nombre = st.text_input("Nombre completo (Ejemplo: Juan Pérez)")
email = st.text_input("Correo electrónico (Ejemplo: juan.perez@example.com)")
telefono = st.text_input("Teléfono (+57 314 300 6989)")

# Selector de fecha
fecha_nacimiento = st.date_input("Fecha de nacimiento")

# Botón de validación
if st.button("Validar datos"):
    errores = []
    if not validar_nombre(nombre):
        errores.append("Nombre no válido. Debe contener solo letras y comenzar con mayúsculas.")
    if not validar_email(email):
        errores.append("Correo electrónico no válido.")
    if not validar_telefono(telefono):
        errores.append("Teléfono no válido. Debe seguir el formato +57 314 300 6989.")
    if not validar_fecha_nacimiento(fecha_nacimiento):
        errores.append("Fecha de nacimiento no válida. Debe ser una fecha en el pasado y corresponder a una edad razonable (0-120 años).")
    
    if errores:
        st.error("Errores detectados:")
        for error in errores:
            st.write(f"- {error}")
    else:
        st.success("Todos los datos son válidos.")

# Footer
st.write("---")
st.write("**App desarrollada por: Juan Grajales**")
