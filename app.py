import streamlit as st

from components.menu import render_menu
from components.recados_barra import render_recados_barra
from components.footer import render_footer

from pages import casamento, galeria, sobre_nos, recados, presentes

st.set_page_config(
    page_title="Casando na Trinca",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    with open("assets/styles/theme.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# MENU
pagina = render_menu()

# BARRA DE RECADOS
render_recados_barra()

# CONTEÚDO PRINCIPAL
if pagina == "Casamento":
    casamento.render()

elif pagina == "Galeria":
    galeria.render()

elif pagina == "Sobre Nós":
    sobre_nos.render()

elif pagina == "Recados":
    recados.render()

elif pagina == "Presentes":
    presentes.render()

# FOOTER
render_footer()
