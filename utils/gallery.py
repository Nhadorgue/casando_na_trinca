import json
import requests

RAW_BASE = (
    "https://raw.githubusercontent.com/"
    "Nhadorgue/casando_na_trinca_imagens/main/images_output/casal/"
)

JSON_URL = RAW_BASE + "images.json"


def get_gallery_images():
    try:
        response = requests.get(JSON_URL, timeout=10)
        response.raise_for_status()

        filenames = json.loads(response.text)

        return [RAW_BASE + name for name in filenames]

    except Exception as e:
        print("Erro ao carregar galeria:", e)
        return []
