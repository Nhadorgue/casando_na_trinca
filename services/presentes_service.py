from repositories.presentes_repository import buscar_presentes_disponiveis

def listar_presentes():
    presentes = buscar_presentes_disponiveis()

    for p in presentes:
        p["is_pix"] = (p["id"] == 50)

        if p["is_pix"]:
            p["valor_exibicao"] = "Livre 🤍"
        else:
            try:
                valor = float(p["valor_estimado"])
                p["valor_exibicao"] = f"~R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            except (TypeError, ValueError):
                p["valor_exibicao"] = "—"

    return presentes
