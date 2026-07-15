import streamlit as st

from repositories.assumidos_repository import inserir_assumido
from repositories.presentes_repository import marcar_como_assumido


def confirmar_presente_service() -> None:
    presente = st.session_state["presente_selecionado"]
    nome = st.session_state["nome_convidado"]

    inserir_assumido(
        presente_id=presente["id"],
        nome_convidado=nome.upper(),
    )

    if not presente.get("is_pix"):
        marcar_como_assumido(presente["id"])
