import html

import streamlit as st

from utils.google_sheets import get_recados_aprovados

# Velocidade da rolagem: segundos por caractere (quanto maior, mais lento)
SEGUNDOS_POR_CARACTERE = 0.18
DURACAO_MINIMA = 20  # segundos


def render_recados_barra():
    try:
        recados = get_recados_aprovados()
    except Exception:
        st.markdown("🤍 Em breve mais recados!")
        st.divider()
        return

    if recados:
        mensagens = "&nbsp;&nbsp;|&nbsp;&nbsp;".join(
            f'🤍 "{html.escape(str(r["Recado"]))}" — {html.escape(str(r["Nome"]))}'
            for r in recados
        )

        # Duração proporcional ao tamanho do texto → velocidade constante
        duracao = max(DURACAO_MINIMA, int(len(mensagens) * SEGUNDOS_POR_CARACTERE))

        st.markdown(
            f"""
            <div class="recados-marquee">
                <span style="animation-duration: {duracao}s;">{mensagens}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
