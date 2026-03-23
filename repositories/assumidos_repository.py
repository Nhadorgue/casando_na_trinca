from datetime import datetime
from utils.google_sheets_presentes import get_assumidos_sheet

def inserir_assumido(presente_id, nome_convidado):
    sheet = get_assumidos_sheet()
    records = sheet.get_all_records()

    novo_id = len(records) + 1

    sheet.append_row([
        novo_id,
        presente_id,
        nome_convidado,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])