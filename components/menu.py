import streamlit as st
from utils.background import get_base64_image

def render_menu():

    if "pagina" not in st.session_state:
        st.session_state.pagina = "Casamento"
       

    # CONTAINER DO MENU
    st.markdown("<div class='menu-wrapper'>", unsafe_allow_html=True)

    # LOGO CENTRALIZADO
    st.markdown(
        f"""
        <div class="logo-container">
            <img src="data:image/png;base64,{
                get_base64_image("assets/images/logo.png")
                }" width="280"/>
        </div>
        """,
        unsafe_allow_html=True
    )

    # MENU
    paginas = ["Casamento", "Galeria", "Sobre Nós", "Recados", "Presentes"]
    cols = st.columns(len(paginas))

    for col, nome in zip(cols, paginas):
        with col:
            if st.button(
                nome,
                key=f"menu-{nome}",
                use_container_width=True
            ):
                st.session_state.pagina = nome

            # if st.session_state.pagina == nome:
            #     st.markdown("<div class='menu-underline'></div>", unsafe_allow_html=True)

    return st.session_state.pagina

