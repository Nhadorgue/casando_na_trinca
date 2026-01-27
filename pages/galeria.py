import random
import streamlit as st
from utils.background import apply_virgem_maria_background
from utils.gallery import get_gallery_images

IMAGES_PER_PAGE = 25
COLS = 5


def prev_page():
    if st.session_state.gallery_page > 1:
        st.session_state.gallery_page -= 1


def next_page(total_pages):
    if st.session_state.gallery_page < total_pages:
        st.session_state.gallery_page += 1


def gallery_navigation(total_pages, position: str):
    col_prev, col_info, col_next = st.columns([1, 3, 1])

    with col_prev:
        st.button(
            "⬅️",
            key=f"prev_{position}",
            disabled=st.session_state.gallery_page == 1,
            on_click=prev_page
        )

    with col_info:
        st.markdown(
            f"<div style='text-align:center;'>"
            f"Página <b>{st.session_state.gallery_page}</b> de <b>{total_pages}</b>"
            f"</div>",
            unsafe_allow_html=True
        )

    with col_next:
        st.button(
            "➡️",
            key=f"next_{position}",
            disabled=st.session_state.gallery_page == total_pages,
            on_click=next_page,
            args=(total_pages,)
        )


def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("🖼️ Galeria")
    st.write("💕 Apreciem com moderação...")

    # ---------- IGREJA ----------
    st.subheader("📸 O lugar onde tudo acontecerá")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/images/externa.jpg", caption="Paróquia - Visão externa", width='stretch')
    with col2:
        st.image("assets/images/interior.jpg", caption="Interior da igreja", width='stretch')
    with col3:
        st.image("assets/images/altar.jpg", caption="Altar", width='stretch')

    st.divider()

    # ---------- GALERIA DO CASAL ----------
    st.subheader("👀 Algumas fotinhas nossas e participações especiais...")

    # 🔄 Busca automática
    images = get_gallery_images()

    if not images:
        st.info("📷 Em breve novas fotos...")
        return

    # 🎲 SHUFFLE UMA VEZ POR SESSÃO
    if "shuffled_images" not in st.session_state:
        shuffled = images.copy()
        random.shuffle(shuffled)
        st.session_state.shuffled_images = shuffled

    images = st.session_state.shuffled_images

    total_pages = (len(images) - 1) // IMAGES_PER_PAGE + 1

    if "gallery_page" not in st.session_state:
        st.session_state.gallery_page = 1

    # ---------- NAVEGAÇÃO EM CIMA ----------

    gallery_navigation(total_pages, position="top")

    # ---------- SLICE ----------
    start = (st.session_state.gallery_page - 1) * IMAGES_PER_PAGE
    end = start + IMAGES_PER_PAGE
    page_images = images[start:end]

    # ---------- GRID ----------
    for row in range(0, len(page_images), COLS):
        cols = st.columns(COLS)
        for col, img_url in zip(cols, page_images[row:row + COLS]):
            with col:
                st.image(img_url, width='stretch')

    # ---------- NAVEGAÇÃO EM BAIXO ----------

    gallery_navigation(total_pages, position="bottom")

