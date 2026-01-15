import streamlit as st

def render_menu():

    if "pagina" not in st.session_state:
        st.session_state.pagina = "Casamento"

    # LOGO
    st.markdown(
        """
        <div class="logo-container">
            <img src="data:image/png;base64,{}" width="280"/>
        </div>
        """.format(get_logo_base64()),
        unsafe_allow_html=True
    )

    # MENU
    cols = st.columns(5)
    paginas = ["Casamento", "Galeria", "Sobre Nós", "Recados", "Presentes"]

    for col, nome in zip(cols, paginas):
        with col:
            classe = "menu-active" if st.session_state.pagina == nome else ""
            if st.button(nome, key=nome):
                st.session_state.pagina = nome
            st.markdown(
                f"<div class='{classe}'></div>",
                unsafe_allow_html=True
            )

    return st.session_state.pagina


def get_logo_base64():
    import base64
    with open("assets/images/logo.png", "rb") as img:
        return base64.b64encode(img.read()).decode()
