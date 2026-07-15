import streamlit as st

# Chaves da máquina de estados do fluxo de presente (modal de confirmação)
CHAVES_CONFIRMACAO = [
    "confirmar_definitivo",
    "presente_confirmado",
    "nome_convidado",
]


def limpar_estado_presente():
    """Encerra o fluxo de presente por completo (fecha o modal)."""
    for chave in CHAVES_CONFIRMACAO + ["presente_selecionado"]:
        st.session_state.pop(chave, None)


def reset_confirmacao():
    """Zera as fases da confirmação ao abrir o modal de um novo presente."""
    for chave in CHAVES_CONFIRMACAO:
        st.session_state.pop(chave, None)
