import streamlit as st
from datetime import datetime
from utils.background import apply_virgem_maria_background
from utils.google_sheets import get_sheet, get_recados_aprovados

def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("💬 Recados")

    # ---------------------------
    # FORMULÁRIO
    # ---------------------------
    st.subheader("Deixe seu recado para nós 🤍")

    with st.form("form_recado"):
        nome = st.text_input("Seu nome").upper()
        recado = st.text_area("Seu recado").upper()
        submitted = st.form_submit_button("Enviar recado")

        if submitted:
            if nome and recado:
                try:
                    sheet = get_sheet()
                    sheet.append_row([
                        recado,
                        nome,
                        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        "FALSE"
                    ])
                    get_recados_aprovados.clear()
                    st.success("Recado enviado com sucesso! Após aprovação ele aparecerá 🤍")
                except Exception as e:
                    st.error("Erro ao salvar recado.")
            else:
                st.warning("Preencha todos os campos.")

    st.divider()

    # ---------------------------
    # LISTA DE RECADOS APROVADOS
    # ---------------------------
    st.subheader("Recados aprovados 💌")

    try:
        recados = get_recados_aprovados()

        if not recados:
            st.info("Ainda não há recados aprovados.")
        else:
            for r in reversed(recados):  # mais recente primeiro
                st.markdown(
                    f"""
                    <div style="
                        background-color:#f8f6f4;
                        padding:15px;
                        border-radius:12px;
                        margin-bottom:10px;
                    ">
                        <b>{r["Nome"]}</b><br>
                        <span>{r["Recado"]}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    except:
        st.error("Erro ao carregar recados.")