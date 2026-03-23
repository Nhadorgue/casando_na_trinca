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
        info["private_key"] = info["private_key"].replace("\\n", "\n")
        credentials = Credentials.from_service_account_info(info, scopes=SCOPE)
    else:
        credentials = Credentials.from_service_account_file(
            "utils/archives/google_credentials.json",
            scopes=SCOPE
        )
    return credentials


@st.cache_resource
def get_client():
    credentials = get_credentials()
    return gspread.authorize(credentials)


def get_presentes_sheet():
    client = get_client()
    return client.open("Casando_na_Trinca_Presentes").worksheet("presentes")


def get_assumidos_sheet():
    client = get_client()
    return client.open("Casando_na_Trinca_Presentes").worksheet("assumidos")