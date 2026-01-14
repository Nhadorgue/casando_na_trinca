import streamlit as st

def render_footer():
    st.divider()

    st.markdown(
        """
        <div style="text-align:center; color:gray; font-size:14px;">
            🤍 Casando na Trinca · Dezembro de 2026<br>
            “O que Deus uniu, o homem não separe.” (Mt 19,6)
            Grazielle & Gabriel
        </div>
        """,
        unsafe_allow_html=True
    )
