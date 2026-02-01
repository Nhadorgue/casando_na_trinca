import streamlit as st
from utils.background import apply_virgem_maria_background
from utils.gallery import get_gallery_images

COLS = 4  # 4 colunas x 3 linhas = 12 fotos

def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("🖼️ Galeria")
    st.write("💕 Apreciem com moderação...")

    # ---------- IGREJA ----------
    st.subheader("📸 O lugar onde tudo acontecerá")

    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     st.image("assets/images/externa.jpg", caption="Paróquia - Visão externa")
    # with col2:
    #     st.image("assets/images/interior.jpg", caption="Interior da igreja")
    # with col3:
    #     st.image("assets/images/altar.jpg", caption="Altar")

    # col1 = st.columns([1])

    # with col1:
    st.image(
        "assets/images/igreja_vertical.jpg",
        width='stretch'
    )  

    st.divider()

    # ---------- GALERIA DO CASAL ----------

    st.subheader("👀 Algumas fotinhas nossas e participações especiais...🤍")

    # images = get_gallery_images()

    # if not images:
    #     st.info("📷 Em breve novas fotos...")
    #     return

    # # 🔒 Limite fixo: no máximo 12 imagens
    # gallery_images = images[:12]

    # # ---------- GRID FIXO 4x3 ----------
    # for row in range(0, len(gallery_images), COLS):
    #     cols = st.columns(COLS)
    #     for col, img_path in zip(cols, gallery_images[row:row + COLS]):
    #         with col:
    #             st.image(img_path)

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.image(
            "assets/images/galeria.jpg"#,
            # width='stretch'
        )  