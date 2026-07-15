import streamlit as st

from utils.background import apply_virgem_maria_background

# =========================
# CONFIGURAÇÕES DO CASAMENTO
# =========================
# Formato ISO com fuso de Brasília — usado pelo contador no navegador
DATA_CASAMENTO_ISO = "2026-12-05T14:00:00-03:00"
DATA_CASAMENTO_TEXTO = "05 de dezembro de 2026 às 14 horas"

LOCAL = "Paróquia Nossa Senhora das Graças"

ENDERECO = (
    "R. Nova Independência, 9 - Jardim Ana Estela\n"
    "Carapicuíba - SP, 06364-570"
)


# =========================
# CONTAGEM REGRESSIVA (roda no navegador — zero custo pro servidor)
# =========================
def render_contador():
    contador_html = f"""
    <style>
        .contador {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            font-family: Georgia, 'Times New Roman', serif;
        }}
        .contador-item {{
            text-align: center;
            padding: 16px 4px;
            border: 1.5px solid #A7C7E7;
            border-radius: 14px;
            background-color: rgba(255, 255, 255, 0.9);
            box-shadow: 0 6px 18px rgba(167, 199, 231, 0.35);
        }}
        .contador-numero {{
            font-size: clamp(1.4rem, 6vw, 2.4rem);
            font-weight: 600;
            color: #2c2c2c;
            line-height: 1.2;
        }}
        .contador-rotulo {{
            font-size: clamp(0.65rem, 2.5vw, 0.85rem);
            color: #6b6b6b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-top: 4px;
        }}
        .contador-celebracao {{
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 1.3rem;
            color: #2c2c2c;
            text-align: center;
            padding: 24px;
        }}
    </style>

    <div id="contador" class="contador">
        <div class="contador-item">
            <div id="dias" class="contador-numero">–</div>
            <div class="contador-rotulo">Dias</div>
        </div>
        <div class="contador-item">
            <div id="horas" class="contador-numero">–</div>
            <div class="contador-rotulo">Horas</div>
        </div>
        <div class="contador-item">
            <div id="minutos" class="contador-numero">–</div>
            <div class="contador-rotulo">Minutos</div>
        </div>
        <div class="contador-item">
            <div id="segundos" class="contador-numero">–</div>
            <div class="contador-rotulo">Segundos</div>
        </div>
    </div>

    <script>
        const dataCasamento = new Date("{DATA_CASAMENTO_ISO}");

        function atualizar() {{
            const diff = dataCasamento - new Date();

            if (diff <= 0) {{
                document.getElementById("contador").outerHTML =
                    '<div class="contador-celebracao">🎉 Chegou o grande dia! Deus seja louvado!</div>';
                clearInterval(intervalo);
                return;
            }}

            const totalSegundos = Math.floor(diff / 1000);
            document.getElementById("dias").textContent = Math.floor(totalSegundos / 86400);
            document.getElementById("horas").textContent = Math.floor((totalSegundos % 86400) / 3600);
            document.getElementById("minutos").textContent = Math.floor((totalSegundos % 3600) / 60);
            document.getElementById("segundos").textContent = totalSegundos % 60;
        }}

        atualizar();
        const intervalo = setInterval(atualizar, 1000);
    </script>
    """

    st.iframe(contador_html, height=140)


# =========================
# RENDER DA PÁGINA
# =========================
def render():
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
        st.write(f"**Data:** {DATA_CASAMENTO_TEXTO}")
        st.write(f"**Local:** {LOCAL}")
        st.write("**Endereço:**")
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
    render_contador()

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

    st.iframe(mapa_html, height=620)
