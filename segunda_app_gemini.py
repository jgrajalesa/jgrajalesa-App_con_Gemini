import streamlit as st
import re

def validar_datos(nombre, email, telefono, fecha):
    """Valida los datos ingresados por el usuario utilizando expresiones regulares.

    Args:
        nombre (str): El nombre ingresado.
        email (str): La dirección de correo electrónico ingresada.
        telefono (str): El número de teléfono ingresado.
        fecha (str): La fecha ingresada.

    Returns:
        bool: True si todos los datos son válidos, False en caso contrario.
    """

    # Expresiones regulares
    patron_nombre = r'^[A-Z][a-zA-Z]+$'
    patron_email = r'^[\w\.-]+@[A-Za-z]+\.[A-Za-z]{2,}$'
    patron_telefono = r'^\d{10}$'  # Ajustar según el formato de teléfono deseado
    patron_fecha = r'^\d{4}-\d{2}-\d{2}$'  # Formato YYYY-MM-DD

    if not re.match(patron_nombre, nombre):
        st.error("El nombre debe comenzar con mayúscula y solo contener letras.")
        return False
    if not re.match(patron_email, email):
        st.error("Ingrese una dirección de correo electrónico válida (ejemplo: nombre@ejemplo.com).")
        return False
    if not re.match(patron_telefono, telefono):
        st.error("El número de teléfono debe tener 10 dígitos.")
        return False
    if not re.match(patron_fecha, fecha):
        st.error("Ingrese una fecha en formato YYYY-MM-DD.")
        return False
    return True

# Interfaz de usuario con Streamlit
st.title("Formulario de Registro")
st.caption("App elaborada por: Juan Grajales")
nombre = st.text_input("Nombre:", placeholder="Ingrese su nombre")
email = st.text_input("Correo electrónico:", placeholder="Ingrese su correo electrónico")
telefono = st.text_input("Teléfono:", placeholder="Ingrese su número de teléfono")
fecha = st.date_input("Fecha de nacimiento:", format="YYYY-MM-DD")

if st.button("Enviar"):
    if validar_datos(nombre, email, telefono, fecha):
        st.success("¡Datos válidos! Gracias por registrarte.")
    else:
        st.warning("Por favor, corrija los errores en el formulario.")
