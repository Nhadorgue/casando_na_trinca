import streamlit as st
from pathlib import Path

def load_css():
    if st.session_state.get("css_loaded"):
        return
    # st.session_state["css_loaded"] = True

    css_path = (
        Path(__file__).parent.parent / "assets" / "styles" / "theme.css"
    )

    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True
        )
        # st.session_state["css_loaded"] = True
    else:
        st.error(f"CSS não encontrado em: {css_path}")