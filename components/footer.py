import streamlit as st

def render_footer():
    st.divider()

    st.markdown(
        """
        <div style="text-align:center; color:gray; font-size:14px;">
            🤍 Casando na Trinca · Dezembro de 2026<br>
            "O amor humano, o amor aqui em baixo na terra, quando é verdadeiro, ajuda-nos a saborear o amor divino.” \n(É Cristo que passa, Ponto 166)
            \nGrazielle & Gabriel
        </div>
        """,
        unsafe_allow_html=True
    )
