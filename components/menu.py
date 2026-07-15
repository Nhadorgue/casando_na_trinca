import streamlit as st

from utils.background import get_base64_image

PAGINAS = ["Casamento", "Galeria", "Sobre Nós", "Recados", "Presentes"]


def render_menu():
    if "pagina" not in st.session_state:
        st.session_state.pagina = "Casamento"

    # O key gera a classe CSS ".st-key-menu_navegacao", usada no theme.css
    # para estilizar apenas os botões do menu
    with st.container(key="menu_navegacao"):

        # LOGO CENTRALIZADO
        st.markdown(
            f"""
            <div class="logo-container">
                <img src="data:image/png;base64,{get_base64_image('assets/images/logo.png')}"
                     width="280" alt="Casando na Trinca"/>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # BOTÕES DE NAVEGAÇÃO
        cols = st.columns(len(PAGINAS))

        for col, nome in zip(cols, PAGINAS):
            with col:
                if st.button(nome, key=f"menu-{nome}", width="stretch"):
                    st.session_state.pagina = nome

    return st.session_state.pagina
