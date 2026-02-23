import os
import json
import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_credentials():
    if os.getenv("GOOGLE_CREDENTIALS"):
        info = json.loads(os.getenv("GOOGLE_CREDENTIALS"))

        # Corrige possíveis problemas de quebra de linha
        info["private_key"] = info["private_key"].replace("\\n", "\n")

        credentials = Credentials.from_service_account_info(info, scopes=SCOPE)
    else:
        credentials = Credentials.from_service_account_file(
            "utils/archives/google_credentials.json",
            scopes=SCOPE
        )

    return credentials

@st.cache_resource
def get_sheet():
    credentials = get_credentials()
    client = gspread.authorize(credentials)
    sheet = client.open("Casando_na_Trinca_Recados").sheet1
    return sheet


@st.cache_data(ttl=30)  # atualiza a cada 30 segundos
def get_recados_aprovados():
    sheet = get_sheet()
    records = sheet.get_all_records()

    recados = [
        r for r in records
        if str(r["Aprovado"]).upper() == "TRUE"
    ]

    return recados