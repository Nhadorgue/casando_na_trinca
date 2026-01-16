import streamlit as st
import base64
from pathlib import Path

def render_menu():

    if "pagina" not in st.session_state:
        st.session_state.pagina = "Casamento"

    # CONTAINER DO MENU
    st.markdown("<div class='menu-wrapper'>", unsafe_allow_html=True)

    # LOGO CENTRALIZADO
    st.markdown(
        f"""
        <div class="logo-container">
            <img src="data:image/png;base64,{get_logo_base64()}" width="280"/>
        </div>
        """,
        unsafe_allow_html=True
    )

    # MENU
    paginas = ["Casamento", "Galeria", "Sobre Nós", "Recados", "Presentes"]
    cols = st.columns(len(paginas))

    for col, nome in zip(cols, paginas):
        with col:
            is_active = st.session_state.pagina == nome
            
            st.button(
                nome,
                key=f"menu-{nome}",
                use_container_width=True,
            )

            if is_active:
                st.markdown(
                    f"""
                    <script>
                    const btn = window.parent.document.querySelector(
                        'button[kind="secondary"]:has-text("{nome}")'
                    );
                    if (btn) btn.setAttribute("data-active", "true");
                    </script>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state.pagina


def get_logo_base64():
    path = Path("assets/images/logo.png")
    return base64.b64encode(path.read_bytes()).decode()
