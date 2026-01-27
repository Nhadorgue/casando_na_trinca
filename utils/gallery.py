import streamlit as st
import requests
from typing import List

OWNER = "Nhadorgue"
REPO = "casando_na_trinca_imagens"
BRANCH = "main"
FOLDER_PATH = "images_output/casal"

RAW_BASE_URL = (
    f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{FOLDER_PATH}"
)

GITHUB_API_URL = (
    f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FOLDER_PATH}"
)

@st.cache_data(ttl=3600)
def get_gallery_images() -> List[str]:
    """
    Busca automaticamente todas as imagens JPG da galeria
    diretamente do GitHub.
    """
    response = requests.get(GITHUB_API_URL, timeout=10)
    response.raise_for_status()

    files = response.json()

    images = [
        f"{RAW_BASE_URL}/{file['name']}"
        for file in files
        if file["type"] == "file"
        and file["name"].lower().endswith(".jpg")
    ]

    # Ordena por nome (000.jpg, 001.jpg...)
    images.sort()

    return images
