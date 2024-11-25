import streamlit as st
import re

def evaluar_contraseña(contraseña):
    """Evalúa la fortaleza de una contraseña y devuelve un mensaje.

    Args:
        contraseña (str): La contraseña a evaluar.

    Returns:
        str: Un mensaje indicando si la contraseña es segura y sugerencias.
    """

    # Expresiones regulares para verificar los criterios
    mayusculas = re.compile(r'[A-Z]')
    minusculas = re.compile(r'[a-z]')
    numeros = re.compile(r'\d')
    especiales = re.compile(r'[^a-zA-Z0-9]')

    # Verificar si la contraseña cumple con todos los criterios
    if (len(contraseña) >= 8 and
            mayusculas.search(contraseña) and
            minusculas.search(contraseña) and
            numeros.search(contraseña) and
            especiales.search(contraseña)):
        return "La contraseña es segura."
    else:
        sugerencias = []
        if len(contraseña) < 8:
            sugerencias.append("Debe tener al menos 8 caracteres.")
        if not mayusculas.search(contraseña):
            sugerencias.append("Debe incluir al menos una letra mayúscula.")
        if not minusculas.search(contraseña):
            sugerencias.append("Debe incluir al menos una letra minúscula.")
        if not numeros.search(contraseña):
            sugerencias.append("Debe incluir al menos un número.")
        if not especiales.search(contraseña):
            sugerencias.append("Debe incluir al menos un carácter especial.")
        return f"La contraseña no es segura. Sugerencias: {', '.join(sugerencias)}"

# Interfaz de usuario con Streamlit
st.title("Evaluador de Contraseñas")

contraseña = st.text_input("Ingrese su contraseña:")

if contraseña:
    resultado = evaluar_contraseña(contraseña)
    st.write(resultado)