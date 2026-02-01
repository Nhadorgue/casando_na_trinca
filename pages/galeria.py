import streamlit as st
from utils.background import apply_virgem_maria_background
from utils.gallery import get_gallery_images

def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("🖼️ Galeria")
    st.write("💕 Apreciem com moderação...")

    # ---------- IGREJA ----------
    st.subheader("📸 O lugar onde tudo acontecerá")

    col1, col2, col3 = st.columns([0.5, 4, 0.5])


    with col2:
        st.image(
            "assets/images/igreja_vertical.jpg",
            width='stretch'
        )  

    st.divider()

    # ---------- GALERIA DO CASAL ----------

    st.subheader("👀 Algumas fotinhas nossas e participações especiais...🤍")

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.image(
            "assets/images/galeria.jpg"#,
            # width='stretch'
        )  