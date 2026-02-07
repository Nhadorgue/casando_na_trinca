import streamlit as st

def limpar_estado_presente():
    for key in [
        "processando_confirmacao",
        "abrir_modal_presente",
        "presente_selecionado",
        "confirmar_definitivo",
        "nome_convidado",
        "presente_confirmado",
    ]:
        if key in st.session_state:
            del st.session_state[key]


def reset_confirmacao():
    for key in [
        "confirmar_definitivo",
        "processando_confirmacao",
        "presente_confirmado",
        "nome_convidado",
    ]:
        if key in st.session_state:
            del st.session_state[key]
