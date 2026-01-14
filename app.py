import streamlit as st

from components.menu import render_menu
from components.recados_barra import render_recados_barra
from components.footer import render_footer

st.set_page_config(
    page_title="Casando na Trinca",
    layout="wide"
)

# MENU
pagina = render_menu()

# BARRA DE RECADOS (abaixo do menu)
render_recados_barra()

# CONTEÚDO PRINCIPAL
if pagina == "Casamento":
    st.switch_page("pages/casamento.py")
elif pagina == "Galeria":
    st.switch_page("pages/galeria.py")
elif pagina == "Sobre Nós":
    st.switch_page("pages/sobre_nos.py")
elif pagina == "Recados":
    st.switch_page("pages/recados.py")
elif pagina == "Presentes":
    st.switch_page("pages/presentes.py")

# FOOTER
render_footer()
