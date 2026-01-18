import streamlit as st
from utils.style import load_css


st.set_page_config(
    page_title="Casando na Trinca",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from components.menu import render_menu
from components.recados_barra import render_recados_barra
from components.footer import render_footer
from pages import Casamento, Galeria, Presentes, Recados, Sobre_nos

load_css()


# MENU
pagina = render_menu()

# BARRA DE RECADOS
render_recados_barra()

# CONTEÚDO PRINCIPAL
if pagina == "Casamento":
    Casamento.render()

elif pagina == "Galeria":
    Galeria.render()

elif pagina == "Sobre Nós":
    Sobre_nos.render()

elif pagina == "Recados":
    Recados.render()

elif pagina == "Presentes":
     Presentes.render()

# FOOTER
render_footer()
