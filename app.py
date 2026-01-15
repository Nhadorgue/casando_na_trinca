import streamlit as st
from utils.style import load_css
st.set_page_config(
    page_title="Casando na Trinca",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()

from components.menu import render_menu
from components.recados_barra import render_recados_barra
from components.footer import render_footer
from pages import casamento, galeria, sobre_nos, recados, presentes


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
