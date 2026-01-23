import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timezone, timedelta
from streamlit_autorefresh import st_autorefresh
from utils.background import apply_virgem_maria_background

FUSO_BRASIL = timezone(timedelta(hours=-3))

DATA_CASAMENTO = datetime(2026, 12, 5, 14, 0, tzinfo=FUSO_BRASIL)

LOCAL = "Paróquia Nossa Senhora das Graças"
ENDERECO = (
    "R. Nova Independência, 9 - Jardim Ana Estela\n"
    "Carapicuíba - SP, 06364-570"
)


def calcular_tempo_restante(data_evento):
    agora = datetime.now(FUSO_BRASIL)
    diferenca = data_evento - agora

    if diferenca.total_seconds() <= 0:
        return None

    total = int(diferenca.total_seconds())
    dias = total // 86400
    horas = (total % 86400) // 3600
    minutos = (total % 3600) // 60
    segundos = total % 60

    return dias, horas, minutos, segundos


def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("💒 Nosso Casamento")

    st.divider()

    st.subheader("⏳ Falta pouco para o grande dia")
    st_autorefresh(interval=1000, key="contador_casamento")

    tempo = calcular_tempo_restante(DATA_CASAMENTO)

    if tempo:
        d, h, m, s = tempo
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Dias", d)
        c2.metric("Horas", h)
        c3.metric("Minutos", m)
        c4.metric("Segundos", s)

    st.divider()

    st.subheader("📸 O lugar onde tudo acontecerá")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "assets/images/igreja_externa.png",
            caption="Paróquia - Visão externa",
            use_container_width=True
        )

    with col2:
        st.image(
            "assets/images/igreja_interior.png",
            caption="Interior da igreja",
            use_container_width=True
        )

    with col3:
        st.image(
            "assets/images/igreja_altar.png",
            caption="Altar",
            use_container_width=True
        )

    st.divider()

    st.subheader("📍 Como chegar")

    st.markdown(
        """
        <div class="mapa-container">
            <iframe 
                src="https://www.google.com/maps?q=Paróquia+Nossa+Senhora+das+Graças+Carapicuíba+SP&output=embed"
                width="100%"
                height="420"
                style="border:0;"
                loading="lazy">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
