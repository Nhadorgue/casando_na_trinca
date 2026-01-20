import base64
from pathlib import Path


def get_base64_image(path: str) -> str:
    image_path = Path(path)
    return base64.b64encode(image_path.read_bytes()).decode()


def apply_virgem_maria_background():
    img_base64 = get_base64_image("assets/images/virgem_maria.png")

    css = f"""
    <style>

    /* ===============================
       VARIÁVEIS DE COR
    =============================== */
    :root {{
        --serenity-blue: #A7C7E7;
    }}

    /* ===============================
       BACKGROUND PRINCIPAL
    =============================== */
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-repeat: no-repeat;
        background-position: bottom right;
        background-size: 15%;
        background-attachment: fixed;
        z-index: -2;

    }}

    /* Camada branca para suavizar a imagem */
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background-color: rgba(255, 255, 255, 0.85);
        z-index: -1;
    }}
    
    /* ===============================
       GALERIA DE IMAGENS
    =============================== */
    .galeria-img img {{
        width: 100%;
        border-radius: 18px;
        border: 2px solid var(--serenity-blue);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.10);
        filter: blur(0.6px) saturate(1.05);
        transition: all 0.35s ease;
    }}

    .galeria-img img:hover {{
        filter: blur(0px) saturate(1.1);
        transform: scale(1.03);
    }}

    .galeria-img p {{
        margin-top: 8px;
        text-align: center;
        font-size: 0.9em;
        color: #666;
    }}

    /* ===============================
       RESPONSIVIDADE
    =============================== */
    @media (max-width: 768px) {{
        .stApp {{
            background-size: 45%;
            background-position: bottom center;
        }}

        .galeria-img img {{
            border-radius: 14px;
        }}
    }}

    </style>
    """

    return css
