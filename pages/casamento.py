import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timezone, timedelta
from streamlit_autorefresh import st_autorefresh
from utils.background import apply_virgem_maria_background, get_base64_image

FUSO_BRASIL = timezone(timedelta(hours=-3))

# =========================
# CONFIGURAÇÕES DO CASAMENTO
# =========================
DATA_CASAMENTO = datetime(2026, 12, 5, 14, 0) 

LOCAL = "Paróquia Nossa Senhora das Graças"
ENDERECO = (
    "R. Nova Independência, 9 - Jardim Ana Estela\n"
    "Carapicuíba - SP, 06364-570"
)

# =========================
# FUNÇÕES AUXILIARES
# =========================
def calcular_tempo_restante(data_evento):
    agora = datetime.now(FUSO_BRASIL)

    if data_evento.tzinfo is None:
        data_evento = data_evento.replace(tzinfo=FUSO_BRASIL)

    diferenca = data_evento - agora

    if diferenca.total_seconds() <= 0:
        return None

    total_segundos = int(diferenca.total_seconds())

    dias = total_segundos // 86400
    horas = (total_segundos % 86400) // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    return dias, horas, minutos, segundos


# =========================
# RENDER DA PÁGINA
# =========================
def render():
    
    # APLICANDO A IMAGEM DA VIRGEM MARIA NO BACKGROUND
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("💒 Nosso Casamento")
    st.markdown(
        "> *“O amor humano, o amor aqui em baixo na terra, quando é verdadeiro, ajuda-nos a saborear o amor divino.”*  \n"
        "<small>É Cristo que passa, Ponto 166</small>",
        unsafe_allow_html=True
    )

    st.divider()

    # ---------- INFORMAÇÕES ----------
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📅 Data & Local")
        st.write(f"**Data:** 05 de dezembro de 2026")
        st.write(f"**Local:** {LOCAL}")
        st.write(f"**Endereço:**")
        st.write(ENDERECO)

    with col2:
        st.subheader("⛪ Um dia preparado por Deus")
        st.write(
            "Com alegria no coração e confiantes na providência divina, "
            "convidamos você para celebrar conosco o início da nossa família, "
            "sob o olhar amoroso de Deus, da Sagrada Família e da Virgem Maria 🤍"
        )

    st.divider()

    # ---------- CONTAGEM REGRESSIVA ----------
    st.subheader("⏳ Falta pouco para o grande dia")

    # 🔁 Atualiza o cronômetro a cada 1 segundo 
    st_autorefresh(interval=1000, key="contador_casamento")

    tempo = calcular_tempo_restante(DATA_CASAMENTO)

    if tempo is None:
        st.success("🎉 Chegou o grande dia! Deus seja louvado!")
        return

    dias, horas, minutos, segundos = tempo

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Dias", dias)
    c2.metric("Horas", horas)
    c3.metric("Minutos", minutos)
    c4.metric("Segundos", segundos)

    st.divider()

    # ---------- GALERIA DA IGREJA (PLACEHOLDER) ----------

    st.subheader("📸 O lugar onde tudo acontecerá")

    st.write(
        "Em breve, algumas imagens especiais da igreja onde celebraremos "
        "nosso matrimônio 💙"
    )

    col_img1, col_img2, col_img3 = st.columns(3)

    igreja_externa = get_base64_image("assets/images/Igreja_Externa.png") 
    igreja_interior = get_base64_image("assets/images/Igreja_Interior.jpg") 
    igreja_altar = get_base64_image("assets/images/Igreja_Altar.jpg")

    with col_img1:
        st.markdown(
            f"""
            <div class="galeria-img">
                <img src="data:image/jpeg;base64,{igreja_externa}">
                <p style="text-align:center; font-size: 0.9em; color: #666;">
                    Paróquia - Visão externa
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_img2:
        st.markdown(
            f"""
            <div class="galeria-img">
                <img src="data:image/jpeg;base64,{igreja_interior}">
                <p style="text-align:center; font-size: 0.9em; color: #666;">
                    Paróquia - Visão interna
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_img3:
        st.markdown(
            f"""
            <div class="galeria-img">
                <img src="data:image/jpeg;base64,{igreja_altar}">
                <p style="text-align:center; font-size: 0.9em; color: #666;">
                    Altar da igreja
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # ---------- MAPA ----------
    
    st.subheader("📍 Como chegar")

    st.write(
        "A Paróquia Nossa Senhora das Graças está localizada em Carapicuíba – SP. "
        "Abaixo você pode visualizar o mapa e traçar sua rota com facilidade."
    )

    mapa_html = """
    <iframe 
        src="https://www.google.com/maps?q=Paróquia+Nossa+Senhora+das+Graças+Carapicuíba+SP&output=embed"
        width="100%" 
        height="450" 
        style="border:0; border-radius: 12px;"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade">
    </iframe>
    """

    components.html(mapa_html, height=470)
