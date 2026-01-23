import base64
from pathlib import Path


def get_base64_image(path: str) -> str:
    image_path = Path(path)
    return base64.b64encode(image_path.read_bytes()).decode()


def apply_virgem_maria_background():
    img_base64 = get_base64_image("assets/images/virgem_maria.png")

    return f"""
    <style>

    :root {{
        --serenity-blue: #A7C7E7;
    }}

    /* ===============================
       BACKGROUND
    =============================== */
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-repeat: no-repeat;
        background-position: bottom right;
        background-size: 15%;
        background-attachment: fixed;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background-color: rgba(255,255,255,0.85);
        z-index: -1;
    }}

    /* ===============================
       GALERIA (st.image)
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

    /* ===============================
       MAPA
    =============================== */
    .mapa-container {{
        border-radius: 18px;
        border: 2px solid var(--serenity-blue);
        box-shadow: 0 10px 28px rgba(167,199,231,0.45);
        overflow: hidden;
    }}

    @media (max-width: 768px) {{
        .stApp {{
            background-size: 45%;
            background-position: bottom center;
        }}
    }}

    </style>
    """
