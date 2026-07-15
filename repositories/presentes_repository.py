from utils.google_sheets_presentes import get_presentes_sheet

# A worksheet "presentes" tem o cabeçalho na linha 1; dados começam na linha 2
PRIMEIRA_LINHA_DE_DADOS = 2
COLUNA_ASSUMIDO = 5


def buscar_presentes_disponiveis() -> list[dict]:
    records = get_presentes_sheet().get_all_records()

    return [
        p for p in records
        if str(p.get("assumido", "")).upper() != "TRUE"
    ]


def marcar_como_assumido(presente_id: int) -> None:
    sheet = get_presentes_sheet()
    records = sheet.get_all_records()

    for linha, row in enumerate(records, start=PRIMEIRA_LINHA_DE_DADOS):
        if row["id"] == presente_id:
            sheet.update_cell(linha, COLUNA_ASSUMIDO, "TRUE")
            break
