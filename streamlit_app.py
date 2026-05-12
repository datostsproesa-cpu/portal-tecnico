import streamlit as st
import os

st.set_page_config(page_title="Portal Técnico - TS PROESA", layout="centered", page_icon="🛠️")

# --- ESTILOS CORPORATIVOS ---
st.markdown("""
    <style>
        .stApp { background-color: #FFFFFF; color: black; }
        [data-testid="stHeader"], [data-testid="stSidebar"] { background-color: #FFFFFF; }
        h2, p, label, li { color: #00BFFF !important; font-family: sans-serif; }
        hr { border-color: #00BFFF !important; }
        .stAlert[data-baseweb="alert"] { border: 2px solid #00BFFF; background-color: #EBF7FF; border-radius: 10px; }
        .stAlert p { color: #004481 !important; font-weight: 500; }
        div.stButton > button:first-child, a.st-link-button { 
            background-color: #004481; color: white !important; font-weight: bold; 
            border-radius: 8px; border: none; padding: 10px 20px; transition: all 0.3s; width: 100%; text-align: center; display: block;
        }
        div.stButton > button:first-child:hover, a.st-link-button:hover { 
            background-color: #FFFFFF; color: #00BFFF !important; border: 2px solid #00BFFF; text-decoration: none;
        }
        [data-testid="stImage"] { display: flex; justify-content: center; }
    </style>
""", unsafe_allow_html=True)

# --- INTERFAZ GRAFICA ---
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    logo_path = "logo_proesa.png" 
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.warning("⚠️ Archivo 'logo_proesa.png' no encontrado.")

st.markdown("<h2 style='text-align: center; margin-top: 20px;'>Módulo de Operaciones Técnicas</h2>", unsafe_allow_html=True)
st.divider()
st.info("Selecciona el módulo al que deseas acceder. Los datos se guardarán automáticamente en tu base de datos.")

# --- ENLACES AL APPS SCRIPT (Asegúrate de poner la URL de tu implementación final) ---
URL_BASE_SCRIPT = "https://script.google.com/macros/s/AKfycbzkI5LVU8JMWdrHwgsDgjCwVpNhp0YqSn1XnC5TPUcKUc_HKAOmR3BbgWNRWfkS7If_/exec"

URL_CONTACTOS = f"{URL_BASE_SCRIPT}?page=contactos"
URL_VISITAS = f"{URL_BASE_SCRIPT}?page=visitas"

# Botones de navegación
col1, col2 = st.columns(2)
with col1:
    st.link_button("BASE CONTACTOS", URL_CONTACTOS, use_container_width=True)
with col2:
    st.link_button("REPORTE DE VISITAS", URL_VISITAS, use_container_width=True)
