import streamlit as st
from utils.google_sheets import get_recados_aprovados

def render_recados_barra():
    try:
        recados = get_recados_aprovados()

        if recados:
            mensagens = " | ".join(
                [f'🤍 "{r["Recado"]}" — {r["Nome"]}' for r in recados]
            )

            st.markdown(
                f"""
                <marquee behavior="scroll" direction="left" scrollamount="4">
                {mensagens}
                </marquee>
                """,
                unsafe_allow_html=True
            )

    except:
        st.markdown("🤍 Em breve mais recados!")

    st.divider()