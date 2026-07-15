from utils.datas import agora_brasil
from utils.google_sheets_presentes import get_assumidos_sheet


def inserir_assumido(presente_id: int, nome_convidado: str) -> None:
    sheet = get_assumidos_sheet()
    novo_id = len(sheet.get_all_records()) + 1

    sheet.append_row([
        novo_id,
        presente_id,
        nome_convidado,
        agora_brasil().strftime("%Y-%m-%d %H:%M:%S"),
    ])
