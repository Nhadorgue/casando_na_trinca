"""Acesso à planilha de presentes (Casando_na_Trinca_Presentes)."""

import streamlit as st

from utils.google_auth import get_client


@st.cache_resource
def get_presentes_sheet():
    return get_client().open("Casando_na_Trinca_Presentes").worksheet("presentes")


@st.cache_resource
def get_assumidos_sheet():
    return get_client().open("Casando_na_Trinca_Presentes").worksheet("assumidos")
