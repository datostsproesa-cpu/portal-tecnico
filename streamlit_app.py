import streamlit as st
import os

# --- CONFIGURACIÓN DE PÁGINA CORPORATIVA ---
st.set_page_config(
    page_title="Portal Técnico - TS PROESA", 
    layout="centered", 
    page_icon="🛠️"
)

# --- DEFINICIÓN DE COLORES CORPORATIVOS ---
COLOR_FONDO = "#FFFFFF"     # Blanco puro
COLOR_TEXTO = "#00BFFF"      # Celeste DeepSkyBlue legible (Request)
COLOR_BRAND_BLUE = "#004481" # Azul oscuro para contrastes y botón (derivado del logo)

# --- INYECCIÓN DE ESTILOS CSS PERSONALIZADOS (TS PROESA) ---
st.markdown(f"""
    <style>
        /* 1. Fondo Blanco Total de la App */
        .stApp {{
            background-color: {COLOR_FONDO};
            color: black; /* Texto base en negro para legibilidad */
        }}

        /* 2. Cabecera y Sidebar Blancas */
        [data-testid="stHeader"], [data-testid="stSidebar"] {{
            background-color: {COLOR_FONDO};
        }}

        /* 3. Títulos h2 y Párrafos Generales en CELESTE */
        h2, p, label, li {{
            color: {COLOR_TEXTO} !important;
            font-family: sans-serif;
        }}

        /* 4. Estilizar el divisor (st.divider) en celeste */
        hr {{
            border-color: {COLOR_TEXTO} !important;
        }}

        /* 5. Estilizar st.info() - Mantenemos fondo por legibilidad, pero cambiamos borde y texto */
        .stAlert[data-baseweb="alert"] {{
            border: 2px solid {COLOR_TEXTO};
            background-color: #EBF7FF; /* Azul clarísimo de fondo de info */
            border-radius: 10px;
        }}
        .stAlert p {{
            color: #004481 !important; /* Azul oscuro legible para el texto dentro del info */
            font-weight: 500;
        }}

        /* 6. Estilizar st.link_button - Fondo Azul Brand, Texto Blanco (Mejor legibilidad y diseño) */
        div.stButton > button:first-child {{
            background-color: {COLOR_BRAND_BLUE};
            color: white !important;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            transition: all 0.3s;
            padding: 10px 20px;
        }}

        /* Estado Hover del Botón (Pasa a blanco con celeste al pasar el mouse) */
        div.stButton > button:first-child:hover {{
            background-color: {COLOR_FONDO};
            color: {COLOR_TEXTO} !important;
            border: 2px solid {COLOR_TEXTO};
        }}

        /* Centrar contenedor de imagen */
        [data-testid="stImage"] {{
            display: flex;
            justify-content: center;
        }}

    </style>
""", unsafe_allow_html=True)

# --- INTERFAZ GRAFICA ---

# 1. AGREGAR LOGO DE PROESA CENTRADO (LA SEGUNDA IMAGEN ADJUNTADA)
# Usamos columnas para forzar el centrado
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    logo_path = "logo_proesa.png" # Nombre exacto del archivo en tu carpeta
    # Verificación de seguridad por si no subiste la imagen
    if os.path.exists(logo_path):
        st.image(logo_path, use_column_width=True)
    else:
        st.warning("⚠️ Archivo 'logo_proesa.png' no encontrado. Asegúrate de subirlo al repositorio GitHub junto con este código.")

# 2. Título (Automáticamente celeste por CSS)
st.markdown("<h2 style='text-align: center; margin-top: 20px;'>Módulo Técnico</h2>", unsafe_allow_html=True)

st.divider() # Divisor celeste

st.info("Utiliza este botón para generar un reporte de instalación o mantenimiento independiente. Los datos se guardarán automáticamente en tu base de datos.")

# --- CONFIGURACIÓN DE ENLACES EXTERNOS ---
# URL de tu Apps Script
URL_FORMULARIO_TECNICO = "https://script.google.com/macros/s/AKfycbx7O0xl4rWhBtDrQudH90dJA4q8lCNM2ndKShe5MLA7Jtl9P-4JbxEkMrkQEygyOSwT6A/exec"

# Este botón abrirá el formulario en blanco en una nueva pestaña (Con estilo TS PROESA)
st.link_button(" ABRIR FORMULARIO TÉCNICO", URL_FORMULARIO_TECNICO, use_container_width=True)
