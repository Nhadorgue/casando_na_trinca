import streamlit as st


def render_footer():
    st.divider()

    st.markdown(
        """
        <div class="footer-casamento">
            🤍 Casando na Trinca · Dezembro de 2026<br>
            “O amor humano, o amor aqui em baixo na terra, quando é verdadeiro,
            ajuda-nos a saborear o amor divino.”<br>
            (É Cristo que passa, Ponto 166)<br>
            Grazielle &amp; Gabriel
        </div>
        """,
        unsafe_allow_html=True,
    )
