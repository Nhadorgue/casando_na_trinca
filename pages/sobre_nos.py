import streamlit as st
from utils.background import apply_virgem_maria_background, get_base64_image



def bloco_texto_imagem(texto, imagem, invertido=False):
    col1, col2 = st.columns([1.2, 1])

    if invertido:
        col_img, col_txt = col1, col2
    else:
        col_txt, col_img = col1, col2

    img_base64 = get_base64_image(imagem)

    with col_txt:
        st.markdown(
            f"""
            <div class="texto-historia">
                {texto}
            """,
            unsafe_allow_html=True
        )

    with col_img:
        st.markdown(
            f"""
            <div class="img-container">
                <img src="data:image/jpeg;base64,{img_base64}">
            </div>
            """,
            unsafe_allow_html=True
        )


def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    # CSS específico da página
    st.markdown(
        """
        <style>
        .texto-historia {
            text-align: justify;
            font-size: 18px;
            line-height: 1.8;
            color: #2f2f2f;
            padding: 150px 100px;
        }

        .img-container {
            width: 320px;
            height: 320px;
            margin: 0 auto; /* centraliza na coluna */
            overflow: hidden;
            border-radius: 12px; /* pode tirar se quiser quadrado perfeito */
        }

        .img-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    st.title("💞 Sobre Nós")
    st.markdown("### *Uma história escrita por Deus* ✨")

    st.write("")  # espaçamento

    # BLOCO 1 — Texto esquerda | Imagem direita
    bloco_texto_imagem(
        texto="""
        Aqui começa a nossa história. Entre encontros, conversas simples
        e a mão de Deus conduzindo cada passo, fomos descobrindo que o amor
        verdadeiro nasce da amizade, do cuidado e da entrega diária.
        """,
        imagem="assets/images/Foto.jpg",
        invertido=False
    )

    st.write("")
    st.write("")

    # BLOCO 2 — Imagem esquerda | Texto direita
    bloco_texto_imagem(
        texto="""
        Com o tempo, aprendemos que amar é escolher todos os dias.
        É rezar juntos, sonhar juntos e confiar que, mesmo nas dificuldades,
        Deus permanece no centro da nossa história.
        """,
        imagem="assets/images/Foto1.jpg",
        invertido=True
    )

    st.write("")
    st.write("")

    # BLOCO 3 — Texto esquerda | Imagem direita
    bloco_texto_imagem(
        texto="""
        Hoje caminhamos rumo ao sacramento do matrimônio com o coração cheio
        de gratidão. Sabemos que esta história não é apenas nossa,
        mas foi cuidadosamente escrita pelas mãos de Deus.
        """,
        imagem="assets/images/Foto2.jpg",
        invertido=False
    )
