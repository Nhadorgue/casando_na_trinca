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
            <div class="texto-wrapper">
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

        /* ===============================
        VARIÁVEIS DE COR
        =============================== */
        
        :root {
            --serenity-blue: #A7C7E7;
        }

        .texto-historia {
            display: flex;
            align-items: center;      /* centraliza verticalmente */
            justify-content: center;  /* centraliza horizontalmente */
            
            text-align: justify;
            font-size: 50px;
            line-height: 1.9;
            color: #2f2f2f;

            max-width: 600px;         /* estreita o texto */
            margin: 0 auto;           /* centraliza horizontalmente */
            padding: 20px 10px 28px 10px;

            border-bottom: 1.5px solid #91a8d0;
        }

        .texto-wrapper {
            min-height: 360px;
            display: flex;
            align-items: center;
        }


        .img-container {
            width: 360px;
            height: 360px;
            margin: 0 auto; /* centraliza na coluna */
            overflow: hidden;
        }

        .img-container img {
            width: 100%;
            height: 100%;        
            border-radius: 18px;
            border: 2px solid var(--serenity-blue);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.10);
            filter: blur(0.6px) saturate(1.05);
            transition: all 0.35s ease;
        }

        .galeria-img img:hover {
            filter: blur(0px) saturate(1.1);
            transform: scale(1.03);
        }

        @media (max-width: 768px) {

            .img-container {
                width: 260px;
                height: 260px;
                margin: 20px auto;
            }

            .texto-wrapper {
                min-height: auto;
                padding: 0 10px;
            }

            .texto-historia {
                font-size: 17px;
                line-height: 1.7;

                max-width: 100%;
                padding: 16px 8px 22px 8px;
            }
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
        imagem="assets/images/Foto.jpg",
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
        imagem="assets/images/Foto.jpg",
        invertido=False
    )
