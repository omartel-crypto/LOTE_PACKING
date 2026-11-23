"""Reporte Lote Packing - El Pedregal. Muestra el reporte HTML dentro de Streamlit."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Lote Packing", page_icon="📦", layout="wide")
# sin el menu ni los margenes de Streamlit, para que se vea solo el reporte
st.markdown("""<style>
header[data-testid="stHeader"], footer, #MainMenu {display:none !important;}
.block-container {padding:0 !important; max-width:100% !important;}
</style>""", unsafe_allow_html=True)

html = Path(__file__).with_name("LOTE_PACKING.html").read_text(encoding="utf-8")
components.html(html, height=2700, scrolling=True)
