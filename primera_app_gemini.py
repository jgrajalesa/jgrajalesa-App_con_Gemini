import streamlit as st
import re

def evaluar_contrasena(password):
    """Evalúa la fortaleza de una contraseña utilizando expresiones regulares.

    Args:
        password (str): La contraseña a evaluar.

    Returns:
        str: Un mensaje indicando si la contraseña es segura o no, y sugerencias para mejorarla.
    """

    # Expresiones regulares
    mayuscula = re.compile('[A-Z]')
    minuscula = re.compile('[a-z]')
    numero = re.compile('\d')
    especial = re.compile('[^\w\s]')

    mensaje = ""  # Inicializamos el mensaje vacío

    if len(password) < 8:
        mensaje += "\nLa contraseña debe tener al menos 8 caracteres."
    if not mayuscula.search(password):
        mensaje += "\nLa contraseña debe incluir al menos una mayúscula."
    if not minuscula.search(password):
        mensaje += "\nLa contraseña debe incluir al menos una minúscula."
    if not numero.search(password):
        mensaje += "\nLa contraseña debe incluir al menos un número."
    if not especial.search(password):
        mensaje += "\nLa contraseña debe incluir al menos un carácter especial."

    if mensaje == "":
        mensaje = "¡La contraseña es segura!"
    else:
        mensaje = "La contraseña NO es segura. " + mensaje

    return mensaje

# Interfaz de usuario con Streamlit
st.title("Evaluador de Contraseñas")
st.caption("App elaborada por: Juan Grajales")
password = st.text_input("Ingrese su contraseña")

if st.button("Evaluar"):
    resultado = evaluar_contrasena(password)
    st.text(resultado)
