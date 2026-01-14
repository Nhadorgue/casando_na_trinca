import streamlit as st

def render_recados_barra():
    st.markdown(
        """
        <marquee behavior="scroll" direction="left" scrollamount="4">
        🤍 "Que Deus abençoe essa união!" — Maria &nbsp;&nbsp; | &nbsp;&nbsp;
        🙏 "Rezando por vocês!" — João &nbsp;&nbsp; | &nbsp;&nbsp;
        💐 "Todo amor do mundo!" — Família Silva
        </marquee>
        """,
        unsafe_allow_html=True
    )

    st.divider()
