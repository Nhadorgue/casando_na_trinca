"""Autenticação única no Google (service account) para todas as planilhas.

Ordem de busca das credenciais:
1. Variável de ambiente GOOGLE_CREDENTIALS (JSON em uma linha) — usada no Render.
2. Arquivo local utils/archives/google_credentials.json (gitignorado) — fallback de dev.
"""

import json
import os

import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

CAMINHO_CREDENCIAIS_LOCAL = "utils/archives/google_credentials.json"


def get_credentials() -> Credentials:
    credenciais_env = os.getenv("GOOGLE_CREDENTIALS")

    if credenciais_env:
        info = json.loads(credenciais_env)
        # A private_key vem com "\n" literal quando colada em uma linha só
        info["private_key"] = info["private_key"].replace("\\n", "\n")
        return Credentials.from_service_account_info(info, scopes=SCOPE)

    return Credentials.from_service_account_file(
        CAMINHO_CREDENCIAIS_LOCAL, scopes=SCOPE
    )


@st.cache_resource
def get_client() -> gspread.Client:
    """Cliente gspread único e compartilhado por todo o app (cacheado)."""
    return gspread.authorize(get_credentials())
