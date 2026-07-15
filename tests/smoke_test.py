"""Smoke test do site — rodar antes de qualquer push/deploy.

Uso:
    python tests/smoke_test.py

O que ele faz:
1. Renderiza as 5 páginas e falha se qualquer exceção estourar
   (usa as planilhas Google reais, somente leitura).
2. Exercita a máquina de estados do modal de presente: abrir, validar nome
   vazio, avançar para "tem certeza?", voltar e cancelar.

IMPORTANTE: o botão "Sim, confirmar" NUNCA é clicado aqui — ele escreve na
planilha de produção.
"""

import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
os.chdir(RAIZ_PROJETO)
sys.path.insert(0, str(RAIZ_PROJETO))

from streamlit.testing.v1 import AppTest

PAGINAS = ["Casamento", "Galeria", "Sobre Nós", "Recados", "Presentes"]


def estado(at, chave, padrao=None):
    try:
        return at.session_state[chave]
    except (KeyError, AttributeError):
        return padrao


def testar_paginas():
    falhas = []

    for pagina in PAGINAS:
        at = AppTest.from_file("app.py", default_timeout=60)
        at.run()
        at.button(key=f"menu-{pagina}").click().run()

        if at.exception:
            falhas.append((pagina, [e.value for e in at.exception]))
        else:
            print(f"[ok] página {pagina}")

    return falhas


def testar_fluxo_modal_presente():
    at = AppTest.from_file("app.py", default_timeout=60)
    at.run()
    at.button(key="menu-Presentes").click().run()

    botoes_dar = [b for b in at.button if b.key and b.key.startswith("btn_")]
    assert botoes_dar, "nenhum botão 'Dar' encontrado no grid"

    presente_id = botoes_dar[0].key.removeprefix("btn_")

    # Abre o modal
    botoes_dar[0].click().run()
    assert not at.exception, [e.value for e in at.exception]
    assert estado(at, "presente_selecionado")["id"] == int(presente_id)
    print(f"[ok] modal aberto (presente id {presente_id})")

    rotulos = [b.label for b in at.button]
    rotulo_confirmar = (
        "Confirmar Pix 💠" if "Confirmar Pix 💠" in rotulos else "Confirmar Presente"
    )

    # Confirmar sem nome deve avisar e não avançar
    next(b for b in at.button if b.label == rotulo_confirmar).click().run()
    assert not estado(at, "confirmar_definitivo"), "avançou sem nome!"
    assert any("Informe seu nome" in w.value for w in at.warning)
    print("[ok] confirmação sem nome bloqueada")

    # Com nome, avança para "tem certeza?"
    at.text_input(key=f"nome_{presente_id}").set_value("TESTE SMOKE").run()
    next(b for b in at.button if b.label == rotulo_confirmar).click().run()
    assert estado(at, "confirmar_definitivo") is True
    assert any(b.label == "Sim, confirmar" for b in at.button)
    print("[ok] fase 'tem certeza?' exibida")

    # Voltar retorna à fase do nome
    next(b for b in at.button if b.label == "Voltar").click().run()
    assert estado(at, "confirmar_definitivo") is False
    print("[ok] 'Voltar' funciona")

    # Cancelar fecha o modal e limpa o estado
    next(b for b in at.button if b.label == "Cancelar").click().run()
    assert estado(at, "presente_selecionado") is None
    print("[ok] 'Cancelar' limpa o estado")


if __name__ == "__main__":
    falhas = testar_paginas()

    if falhas:
        print("\n=== FALHAS ===")
        for pagina, erros in falhas:
            print(f"[ERRO] {pagina}: {erros}")
        sys.exit(1)

    testar_fluxo_modal_presente()
    print("\nTudo certo: páginas renderizam e o fluxo do modal está saudável.")
