from utils.google_sheets_presentes import get_presentes_sheet

def buscar_presentes_disponiveis():
    sheet = get_presentes_sheet()
    records = sheet.get_all_records()

    presentes = [
        p for p in records
        if str(p["assumido"]).upper() != "TRUE"
    ]

    return presentes


def marcar_como_assumido(presente_id):
    sheet = get_presentes_sheet()
    records = sheet.get_all_records()

    for idx, row in enumerate(records, start=2):
        if row["id"] == presente_id:
            sheet.update_cell(idx, 5, "TRUE")  # coluna assumido
            break