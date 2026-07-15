from pathlib import Path

import streamlit as st

CSS_PATH = Path(__file__).parent.parent / "assets" / "styles" / "theme.css"


def load_css():
    """Injeta o CSS global. Precisa rodar em todo rerun (o Streamlit
    redesenha a página inteira a cada interação).

    Sem cache de propósito: assim, editar o theme.css reflete no próximo
    rerun, sem precisar reiniciar o servidor.
    """
    try:
        st.markdown(f"<style>{CSS_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS não encontrado em: {CSS_PATH}")
