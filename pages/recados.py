import streamlit as st
from utils.background import apply_virgem_maria_background

def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)
    
    st.title("💬 Recados")
    st.write("Em breve todas as informações sobre o grande dia 🤍")
