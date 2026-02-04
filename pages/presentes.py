import streamlit as st
from utils.background import apply_virgem_maria_background
from services.presentes_service import listar_presentes

def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("🎁 Lista de Presentes")

    st.markdown("""
    Com muito carinho, preparamos esta lista para facilitar a vida de quem deseja nos presentear 🤍  

    Caso surja qualquer dúvida — sobre os presentes, valores ou formas de contribuição —
    fiquem totalmente à vontade para entrar em contato diretamente conosco.  

    Que Deus abençoe cada gesto de carinho 🙏
    """)

    st.divider()

    presentes = listar_presentes()

    if not presentes:
        st.info("Todos os presentes já foram assumidos 🤍")
        return

    cols = st.columns(4)

    for idx, presente in enumerate(presentes):
        with cols[idx % 4]:

            st.markdown(
                f"""
                <div style="
                    padding: 12px;
                    border-radius: 14px;
                    border: 1px solid #e5e5e5;
                    background-color: rgba(255,255,255,0.85);
                    margin-bottom: 12px;
                ">
                    <strong>{presente['produto']}</strong><br>
                    <span style="color:#555">{presente['valor_exibicao']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )


            
            st.button("Dar 🤍", key=f"btn_{presente['id']}")
