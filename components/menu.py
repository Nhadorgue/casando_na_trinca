import streamlit as st

def render_menu():
    menu = st.columns(5)

    paginas = ["Casamento", "Galeria", "Sobre Nós", "Recados", "Presentes"]

    for col, nome in zip(menu, paginas):
        with col:
            if st.button(nome, use_container_width=True):
                st.session_state["pagina"] = nome

    return st.session_state.get("pagina", "Casamento")
