"""Acesso à planilha de recados (Casando_na_Trinca_Recados)."""

import streamlit as st

from utils.google_auth import get_client


@st.cache_resource
def get_sheet():
    return get_client().open("Casando_na_Trinca_Recados").sheet1


@st.cache_data(ttl=30)  # edições feitas direto na planilha levam até 30s para aparecer
def get_recados_aprovados() -> list[dict]:
    records = get_sheet().get_all_records()

    return [
        r for r in records
        if str(r.get("Aprovado", "")).upper() == "TRUE"
    ]
