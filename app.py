from dotenv import load_dotenv

load_dotenv()

import streamlit as st

st.set_page_config(
    page_title="Casando na Trinca 💍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from components.footer import render_footer
from components.menu import render_menu
from components.recados_barra import render_recados_barra
from utils.style import load_css
from views import casamento, galeria, presentes, recados, sobre_nos

PAGINAS = {
    "Casamento": casamento.render,
    "Galeria": galeria.render,
    "Sobre Nós": sobre_nos.render,
    "Recados": recados.render,
    "Presentes": presentes.render,
}

load_css()

# MENU
pagina = render_menu()

# BARRA DE RECADOS
render_recados_barra()

# CONTEÚDO PRINCIPAL
PAGINAS.get(pagina, casamento.render)()

# FOOTER
render_footer()
