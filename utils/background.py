import base64
from pathlib import Path

def get_base64_image(path: str) -> str:
    image_path = Path(path)
    return base64.b64encode(image_path.read_bytes()).decode()

def apply_virgem_maria_background():
    img_base64 = get_base64_image("assets/images/virgem_maria.png")

    css = f"""
    <style>
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
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.80);
        z-index: -1;
    }}

    /* Ajuste para telas menores */
    @media (max-width: 768px) {{
        .stApp {{
            background-size: 45%;
            background-position: bottom center;
        }}
    }}

    </style>
    """

    return css
