import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Portal de Servicio Técnico", layout="centered")

# --- CONFIGURACIÓN DE ENLACES EXTERNOS ---
# ✅ AQUÍ AGREGAS TU NUEVO ENLACE TÉCNICO
URL_FORMULARIO_TECNICO = "AQUÍ_PEGA_LA_NUEVA_URL_QUE_TE_DIO_APPS_SCRIPT"

# --- INTERFAZ ---
st.markdown("<h2 style='text-align: center;'>Módulo Técnico</h2>", unsafe_allow_html=True)
st.divider()

st.info("Utiliza este botón para generar un reporte de instalación o mantenimiento independiente. Los datos se guardarán automáticamente en tu base de datos.")

# Este botón abrirá el formulario en blanco en una nueva pestaña
st.link_button("🛠️ ABRIR FORMULARIO TÉCNICO", URL_FORMULARIO_TECNICO, use_container_width=True)