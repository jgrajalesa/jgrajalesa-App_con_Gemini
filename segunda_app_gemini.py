import streamlit as st
import re

def validar_nombre(nombre):
    """Valida si un nombre solo contiene caracteres alfabéticos y comienza con mayúscula.

    Args:
        nombre (str): El nombre a validar.

    Returns:
        bool: True si el nombre es válido, False si no.
    """
    return re.match(r"^[A-Z][a-zA-Z]*$", nombre) is not None

def validar_email(email):
    """Valida si una cadena es una dirección de correo electrónico válida.

    Args:
        email (str): El correo electrónico a validar.

    Returns:
        bool: True si el correo electrónico es válido, False si no.
    """
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) is not None

def validar_telefono(telefono):
    """Valida si una cadena es un número de teléfono válido.

    Args:
        telefono (str): El número de teléfono a validar.

    Returns:
        bool: True si el número de teléfono es válido, False si no.
    """
    # Ejemplo de expresión regular para números de teléfono con código de país opcional
    return re.match(r"^\+?\d{1,3}\s?\d{10}$", telefono) is not None

def validar_fecha(fecha):
    """Valida si una cadena es una fecha válida en formato "AAAA-MM-DD".

    Args:
        fecha (str): La fecha a validar.

    Returns:
        bool: True si la fecha es válida, False si no.
    """
    return re.match(r"^\d{4}-\d{2}-\d{2}$", fecha) is not None

# Interfaz de usuario con Streamlit
st.title("Formulario de Validación")

nombre = st.text_input("Ingrese su nombre (solo letras, comenzando con mayúscula):")
email = st.text_input("Ingrese su correo electrónico (ejemplo: nombre@ejemplo.com):")
telefono = st.text_input("Ingrese su número de teléfono (ejemplo: +54 11 23456789):")
fecha = st.text_input("Ingrese su fecha de nacimiento (AAAA-MM-DD):")

if st.button("Validar"):
    if validar_nombre(nombre):
        st.success("Nombre válido.")
    else:
        st.error("Nombre inválido. Solo se permiten letras y debe comenzar con mayúscula.")

    if validar_email(email):
        st.success("Correo electrónico válido.")
    else:
        st.error("Correo electrónico inválido. Por favor, ingrese un formato válido como nombre@ejemplo.com")

    if validar_telefono(telefono):
        st.success("Número de teléfono válido.")
    else:
        st.error("Número de teléfono inválido. Por favor, ingrese un número con el formato +código_de_país número_de_teléfono.")

    if validar_fecha(fecha):
        st.success("Fecha válida.")
    else:
        st.error("Fecha inválida. Use el formato AAAA-MM-DD (por ejemplo, 2023-11-22).")
