import streamlit as st

from utils.background import apply_virgem_maria_background


def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("🖼️ Galeria")
    st.write("💕 Apreciem com moderação...")

    # ---------- IGREJA ----------
    st.subheader("📸 O lugar onde tudo acontecerá")

    _, col_igreja, _ = st.columns([0.5, 4, 0.5])

    with col_igreja:
        st.image("assets/images/igreja_horizontal.jpg")

    st.divider()

    # ---------- GALERIA DO CASAL ----------
    st.subheader("👀 Algumas fotinhas nossas e participações especiais...🤍")

    _, col_galeria, _ = st.columns([1, 4, 1])

    with col_galeria:
        st.image("assets/images/galeria.jpg")
