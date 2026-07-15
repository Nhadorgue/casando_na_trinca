import base64
from pathlib import Path

import streamlit as st


@st.cache_data(show_spinner=False)
def get_base64_image(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode()


@st.cache_data(show_spinner=False)
def apply_virgem_maria_background() -> str:
    img_base64 = get_base64_image("assets/images/virgem_maria.png")

    return f"""
    <style>

    /* ===============================
       BACKGROUND
    =============================== */
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-repeat: no-repeat;
        background-position: bottom right;
        background-size: 15%;
        background-attachment: fixed;
        z-index: -2;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background-color: rgba(255,255,255,0.85);
        z-index: -1;
    }}

    /* ===============================
       IMAGENS (st.image)
    =============================== */
    div[data-testid="stImage"] {{
        border-radius: 18px;
        border: 2px solid var(--serenity-blue);
        box-shadow: 0 10px 28px rgba(167,199,231,0.45);
        overflow: hidden;
        transition: transform 0.3s ease;
    }}

    div[data-testid="stImage"]:hover {{
        transform: scale(1.02);
    }}

    @media (max-width: 768px) {{
        .stApp {{
            background-size: 45%;
            background-position: bottom center;
        }}
    }}

    </style>
    """
