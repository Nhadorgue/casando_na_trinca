"""Datas e horários no fuso do Brasil.

O servidor de produção (Render) roda em UTC — usar datetime.now() puro
gravaria horários 3h à frente do horário de Brasília nas planilhas.
"""

from datetime import datetime, timedelta, timezone

FUSO_BRASIL = timezone(timedelta(hours=-3))


def agora_brasil() -> datetime:
    return datetime.now(FUSO_BRASIL)
