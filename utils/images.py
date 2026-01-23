import streamlit as st
from PIL import Image
from pathlib import Path

@st.cache_data(show_spinner=False)
def load_image(path: str):
    return Image.open(Path(path))
