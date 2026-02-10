import streamlit as st
from datetime import datetime
from repositories.presentes_repository import marcar_como_assumido
from repositories.assumidos_repository import inserir_assumido
from utils.session import limpar_estado_presente

def confirmar_presente_service():
    presente = st.session_state["presente_selecionado"]
    nome = st.session_state["nome_convidado"]

    inserir_assumido(
        presente_id=presente["id"],
        nome_convidado=nome.upper()
        )

    if not presente.get("is_pix"):
        marcar_como_assumido(presente["id"])

    # limpar_estado_presente()
    # st.rerun()
