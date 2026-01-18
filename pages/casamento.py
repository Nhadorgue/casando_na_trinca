import streamlit as st
from datetime import datetime
# from streamlit_autorefresh import st_autorefresh

def render():
    st.title("💒 Nosso Casamento")
    st.write("Em breve todas as informações sobre o grande dia 🤍")


# # =========================
# # CONFIGURAÇÕES DO CASAMENTO
# # =========================
# DATA_CASAMENTO = datetime(2026, 12, 5, 14, 0) 

# LOCAL = "Paróquia Nossa Senhora das Graças"
# ENDERECO = (
#     "R. Nova Independência, 9 - Jardim Ana Estela\n"
#     "Carapicuíba - SP, 06364-570"
# )

# # =========================
# # FUNÇÕES AUXILIARES
# # =========================
# def calcular_tempo_restante(data_evento):
#     agora = datetime.now()
#     diferenca = data_evento - agora

#     if diferenca.total_seconds() <= 0:
#         return None

#     dias = diferenca.days
#     horas, resto = divmod(diferenca.seconds, 3600)
#     minutos, segundos = divmod(resto, 60)

#     return dias, horas, minutos, segundos


# # =========================
# # RENDER DA PÁGINA
# # =========================
# def render():
#     st.title("💒 Nosso Casamento")
#     st.markdown(
#         "> *“O amor humano, o amor aqui em baixo na terra, quando é verdadeiro, ajuda-nos a saborear o amor divino.”*  \n"
#         "<small>É Cristo que passa, Ponto 166</small>",
#         unsafe_allow_html=True
#     )

#     st.divider()

#     # ---------- INFORMAÇÕES ----------
#     col1, col2 = st.columns([1, 1])

#     with col1:
#         st.subheader("📅 Data & Local")
#         st.write(f"**Data:** 05 de dezembro de 2026")
#         st.write(f"**Local:** {LOCAL}")
#         st.write(f"**Endereço:**")
#         st.write(ENDERECO)

#     with col2:
#         st.subheader("⛪ Um dia preparado por Deus")
#         st.write(
#             "Com alegria no coração e confiantes na providência divina, "
#             "convidamos você para celebrar conosco o início da nossa família, "
#             "sob o olhar amoroso de Deus, da Sagrada Família e da Virgem Maria 🤍"
#         )

#     st.divider()

#     # ---------- CONTAGEM REGRESSIVA ----------
#     # st.subheader("⏳ Falta pouco para o grande dia")

#     # # 🔁 Atualiza a página a cada 1 segundo caso seja o primeiro rerun do streamlit, se for para outra pagina o cronometro morre
#     # if st.session_state.get("pagina") == "casamento":
#     #     st_autorefresh(interval=1000, key="contador_casamento")

#     # tempo = calcular_tempo_restante(DATA_CASAMENTO)

#     # if tempo is None:
#     #     st.success("🎉 Chegou o grande dia! Deus seja louvado!")
#     #     return

#     # dias, horas, minutos, segundos = tempo

#     # c1, c2, c3, c4 = st.columns(4)
#     # c1.metric("Dias", dias)
#     # c2.metric("Horas", horas)
#     # c3.metric("Minutos", minutos)
#     # c4.metric("Segundos", segundos)

#     # st.divider()

#     # ---------- GALERIA DA IGREJA (PLACEHOLDER) ----------
#     # st.subheader("📸 O lugar onde tudo acontecerá")

#     # st.write(
#     #     "Em breve, algumas imagens especiais da igreja onde celebraremos "
#     #     "nosso matrimônio 💙"
#     # )

#     # col_img1, col_img2, col_img3 = st.columns(3)

#     # with col_img1:
#     #     st.image(
#     #         "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620",
#     #         caption="Paróquia - Visão externa"
#     #     )

#     # with col_img2:
#     #     st.image(
#     #         "https://images.unsplash.com/photo-1505842465776-3bf7c6d32a8a",
#     #         caption="Interior da igreja"
#     #     )

#     # with col_img3:
#     #     st.image(
#     #         "https://images.unsplash.com/photo-1508599589929-30c2a37aa3f1",
#     #         caption="Altar"
#     #     )
