from repositories.presentes_repository import buscar_presentes_disponiveis

ID_PRESENTE_PIX = 50


def formatar_valor_brl(valor) -> str:
    """Formata no padrão brasileiro: 1234.5 -> '~R$ 1.234,50'."""
    try:
        valor_float = float(valor)
    except (TypeError, ValueError):
        return "—"

    return f"~R$ {valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def listar_presentes() -> list[dict]:
    presentes = buscar_presentes_disponiveis()

    for p in presentes:
        p["id"] = int(p["id"])  # a planilha pode devolver o id como texto
        p["is_pix"] = p["id"] == ID_PRESENTE_PIX
        p["valor_exibicao"] = "Livre 🤍" if p["is_pix"] else formatar_valor_brl(p.get("valor"))

    return presentes
