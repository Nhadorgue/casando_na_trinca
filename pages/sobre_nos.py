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
            font-size: 18px;
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
        No dia 21 de abril de 2022, Deus começou a escrever uma das páginas mais bonitas das nossas vidas.
        Dois temperamentos fortes...
        Duas personalidades intensas...
        Muito amor… e a intercessão de São José...
        """,
        imagem="assets/images/foto.jpg",
        invertido=False
    )

    st.write("")
    st.write("")

    # BLOCO 2 — Imagem esquerda | Texto direita
    bloco_texto_imagem(
        texto="""
        Ele, engraçadinho, carinhoso, apaixonado por um bom cafuné.
        Ela, determinada, às vezes um pouquinho estressada… mas com 
        um coração imenso e cheio de amor.
        """,
        imagem="assets/images/foto.jpg",
        invertido=True
    )

    st.write("")
    st.write("")

    # BLOCO 3 — Texto esquerda | Imagem direita
    bloco_texto_imagem(
        texto="""
        Desde o início sabíamos que não seria uma história comum. 
        Tivemos nossas diferenças, aprendemos a ceder, crescemos nas dificuldades 
        e descobrimos que amar é, acima de tudo, uma decisão diária.
        """,
        imagem="assets/images/foto.jpg",
        invertido=False
    )

    st.write("")
    st.write("")

    bloco_texto_imagem(
        texto="""
        Somos consagrados à Virgem Maria, e escolhemos viver nosso relacionamento 
        com um propósito maior: levar um ao outro à santidade. Nosso amor não é apenas 
        sobre felicidade aqui na terra — é sobre caminhar juntos rumo ao Céu.
        """,
        imagem="assets/images/foto.jpg",
        invertido=True
    )

    st.write("")
    st.write("")

    bloco_texto_imagem(
        texto="""
        No dia 18 de novembro de 2024, diante de Deus e com o coração 
        transbordando de alegria, dissemos “sim” ao noivado.
        E agora, com imensa gratidão, nos preparamos para dizer 
        nosso “sim” definitivo no altar, no dia 05 de dezembro de 2026.
        """,
        imagem="assets/images/foto.jpg",
        invertido=False
    )

    st.write("")
    st.write("")

    bloco_texto_imagem(
        texto="""
        Nossa história sempre foi construída com apoio, amizade, oração 
        e muito amor. Entre risadas, reconciliações, abraços demorados e 
        sonhos compartilhados, aprendemos que o amor verdadeiro não é a 
        ausência de desafios — é a escolha de permanecer.
        """,
        imagem="assets/images/foto.jpg",
        invertido=True
    )    

    st.write("")
    st.write("")

    bloco_texto_imagem(
        texto="""
        Hoje celebramos não apenas um casamento, mas uma missão:
        ser reflexo do amor de Deus um para o outro e para todos que caminham conosco.
        """,
        imagem="assets/images/foto.jpg",
        invertido=False
    )
    
    st.write("")
    st.write("")
    st.write("Que este seja apenas o começo de uma vida inteira juntos!!!")
    st.write("Com amor, Grazielle &  Gabriel  🤍")
    st.write("")