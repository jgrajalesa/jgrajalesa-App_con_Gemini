from datetime import datetime
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

def validar_fecha(fecha):
    patron = r'^\d{2}/\d{2}/\d{2}$'
    if not re.match(patron, fecha):
        return False
    try:
        # Intentar convertir la fecha para asegurarse de que sea válida
        datetime.strptime(fecha, '%d/%m/%y')
        return True
    except ValueError:
        return False

# Interfaz de Streamlit
st.title("Validación de Datos en Formularios")
st.write("Por favor, completa los campos a continuación en el formato indicado:")

# Entradas del formulario
nombre = st.text_input("Nombre completo (Ejemplo: Juan Pérez)")
email = st.text_input("Correo electrónico (Ejemplo: juan.perez@example.com)")
telefono = st.text_input("Teléfono (+57 314 300 6989)")
fecha = st.text_input("Fecha de nacimiento (DD/MM/AA)")

# Botón de validación
if st.button("Validar datos"):
    errores = []
    if not validar_nombre(nombre):
        errores.append("Nombre no válido. Debe contener solo letras y comenzar con mayúsculas.")
    if not validar_email(email):
        errores.append("Correo electrónico no válido.")
    if not validar_telefono(telefono):
        errores.append("Teléfono no válido. Debe seguir el formato +57 314 300 6989.")
    if not validar_fecha(fecha):
        errores.append("Fecha no válida. Debe seguir el formato DD/MM/AA y ser una fecha existente.")
    
    if errores:
        st.error("Errores detectados:")
        for error in errores:
            st.write(f"- {error}")
    else:
        st.success("Todos los datos son válidos.")

# Footer
st.write("---")
st.write("**App desarrollada por: Juan Grajales**")
