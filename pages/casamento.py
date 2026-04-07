import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timezone, timedelta
from streamlit_autorefresh import st_autorefresh
from utils.background import apply_virgem_maria_background

# =========================
# CONFIGURAÇÕES DO CASAMENTO
# =========================
DATA_CASAMENTO = datetime(2026, 12, 5, 14, 00)  # ajuste o horário depois se quiser

LOCAL = "Paróquia Nossa Senhora das Graças"

ENDERECO = (
    "R. Nova Independência, 9 - Jardim Ana Estela\n"
    "Carapicuíba - SP, 06364-570"
)

FUSO_BRASIL = timezone(timedelta(hours=-3))

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
        st.write(f"**Data:** 05 de dezembro de 2026 às 14 horas")
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

    # 🔁 Atualiza a página a cada 1 segundo
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


    # ---------- MAPA ----------
    st.subheader("📍 Como chegar")

    st.write(
        "A Paróquia Nossa Senhora das Graças está localizada em Carapicuíba – SP. "
        "Abaixo você pode visualizar o mapa e traçar sua rota com facilidade."
    )

    mapa_html = """
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.135185317928!2d-46.84380660000001!3d-23.5635878!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94cf00155cba7f8d%3A0xbc298f4f0dff0a46!2sR.%20Nova%20Independ%C3%AAncia%2C%209%20-%20Jardim%20Ana%20Estela%2C%20Carapicu%C3%ADba%20-%20SP%2C%2006364-570!5e0!3m2!1spt-BR!2sbr!4v1775562186173!5m2!1spt-BR!2sbr"
        width="100%" 
        height="600" 
        style="border:0; border-radius: 12px;"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade">
    </iframe>
    """

    components.html(mapa_html, height=620)
