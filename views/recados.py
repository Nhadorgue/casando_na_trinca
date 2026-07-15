import html

import streamlit as st

from utils.background import apply_virgem_maria_background
from utils.datas import agora_brasil
from utils.google_sheets import get_recados_aprovados, get_sheet


def render():
    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("💬 Recados")

    # ---------------------------
    # FORMULÁRIO
    # ---------------------------
    st.subheader("Deixe seu recado para nós 🤍")

    with st.form("form_recado", clear_on_submit=True):
        nome = st.text_input("Seu nome", max_chars=60).upper()
        recado = st.text_area("Seu recado", max_chars=500).upper()
        submitted = st.form_submit_button("Enviar recado")

        if submitted:
            if nome.strip() and recado.strip():
                try:
                    sheet = get_sheet()
                    sheet.append_row([
                        recado.strip(),
                        nome.strip(),
                        agora_brasil().strftime("%d/%m/%Y %H:%M:%S"),
                        "FALSE",
                    ])
                    get_recados_aprovados.clear()
                    st.success("Recado enviado com sucesso! Após aprovação ele aparecerá 🤍")
                except Exception:
                    st.error("Erro ao salvar o recado. Tente novamente em instantes 🙏")
            else:
                st.warning("Preencha todos os campos.")

    st.divider()

    # ---------------------------
    # LISTA DE RECADOS APROVADOS
    # ---------------------------
    st.subheader("Recados aprovados 💌")

    try:
        recados = get_recados_aprovados()
    except Exception:
        st.error("Erro ao carregar recados.")
        return

    if not recados:
        st.info("Ainda não há recados aprovados.")
        return

    for r in reversed(recados):  # mais recente primeiro
        st.markdown(
            f"""
            <div class="recado-card">
                <b>{html.escape(str(r["Nome"]))}</b><br>
                <span>{html.escape(str(r["Recado"]))}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
