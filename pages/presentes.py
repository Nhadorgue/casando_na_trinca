import streamlit as st
from utils.background import apply_virgem_maria_background

def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)
    
    st.title("🎁 Lista de Presentes")
    st.markdown("""
    Com muito carinho, preparamos esta lista para facilitar a vida de quem deseja nos presentear 🤍  

    Caso surja qualquer dúvida — sobre os presentes, valores ou formas de contribuição — fiquem totalmente à vontade para entrar em contato diretamente conosco.  
    Que Deus abençoe cada gesto de carinho 🙏
    """)

    st.divider()
