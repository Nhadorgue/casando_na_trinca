import html
import os
from collections import Counter

import streamlit as st

from services.assumidos_service import confirmar_presente_service
from services.presentes_service import listar_presentes
from utils.background import apply_virgem_maria_background
from utils.session import limpar_estado_presente, reset_confirmacao

COLUNAS_GRID = 4
IMAGEM_FALLBACK = "assets/images/presentes/utensilios.jpg"


# =========================
# MODAL DE CONFIRMAÇÃO
# =========================
# O modal fica aberto enquanto houver "presente_selecionado" no session_state
# (o render() o reabre a cada rerun). Fechar pelo X limpa o estado (on_dismiss).
@st.dialog("🎁 Confirmar Presente", on_dismiss=limpar_estado_presente)
def dialogo_confirmacao():
    presente = st.session_state["presente_selecionado"]

    # ---------- FASE 3 — AGRADECIMENTO ----------
    if st.session_state.get("presente_confirmado"):
        st.success("🎉 Muito obrigado pelo carinho e sua generosidade!")
        st.info(
            "Se quiser, pode deixar um recado para nós 🤍 "
            "Ele ficará visível em todas as páginas, logo abaixo do menu 😉"
        )

        if st.button("💌 Ir para Recados"):
            limpar_estado_presente()
            st.session_state["pagina"] = "Recados"
            st.rerun()

        return

    imagem_path = f"assets/images/presentes/{presente['id']}.jpg"
    st.image(imagem_path if os.path.exists(imagem_path) else IMAGEM_FALLBACK)

    if presente["is_pix"]:
        st.info("💠 Use o QR Code acima para realizar o Pix")

    st.markdown(f"### {presente['produto']}")
    st.markdown(f"**Valor aproximado:** {presente['valor_exibicao']}")

    # ---------- FASE 2 — CONFIRMAÇÃO DEFINITIVA ----------
    if st.session_state.get("confirmar_definitivo"):
        st.markdown("### 🤍 Tem certeza da sua escolha?")
        st.markdown("Este presente ficará reservado em seu nome.")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Voltar"):
                st.session_state["confirmar_definitivo"] = False
                st.rerun()

        with col2:
            if st.button("Sim, confirmar"):
                try:
                    confirmar_presente_service()
                except Exception:
                    st.error("Não conseguimos registrar agora. Tente novamente em instantes 🙏")
                else:
                    st.session_state["presente_confirmado"] = True
                    st.rerun()

        return

    # ---------- FASE 1 — NOME DO CONVIDADO ----------
    nome = st.text_input("Seu nome 🤍", max_chars=60, key=f"nome_{presente['id']}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Cancelar"):
            limpar_estado_presente()
            st.rerun()

    with col2:
        texto_botao = "Confirmar Pix 💠" if presente["is_pix"] else "Confirmar Presente"

        if st.button(texto_botao):
            if not nome.strip():
                st.warning("Informe seu nome 🙏")
            else:
                st.session_state["nome_convidado"] = nome.strip()
                st.session_state["confirmar_definitivo"] = True
                st.rerun()


# =========================
# RENDER PRINCIPAL
# =========================
def render():
    st.session_state.setdefault("categoria_selecionada", "Todas")

    # No celular, força os cards a ocuparem 2 por linha
    st.markdown(
        """
        <style>
        @media (max-width: 768px) {
            div[data-testid="column"],
            div[data-testid="stColumn"] {
                width: 50% !important;
                flex: 0 0 50% !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)

    st.title("🎁 Lista de Presentes")

    # Reabre o modal a cada rerun enquanto houver presente em confirmação.
    # Fica antes do grid de propósito: o agradecimento precisa aparecer mesmo
    # depois que o presente confirmado some da lista.
    if st.session_state.get("presente_selecionado"):
        dialogo_confirmacao()

    st.markdown("""
        Com muito carinho, preparamos esta lista para facilitar a vida de quem deseja nos presentear 🤍

        Os valores colocados na lista **são apenas uma média** dos presentes que pesquisamos, não necessariamente
        significa que os presentes devem ser nesses mesmos valores. Inclusive, buscamos tomar cuidado para não abusar
                da boa vontade daqueles que desejam nos presentear.

        Existe também a opção de nos presentear com **Pix**, no final da página, para aqueles casos em que a pessoa não encontre o
                presente ou prefira esse modo de presentear...também será muito bem recebido 😅

        Caso surja qualquer dúvida — sobre os presentes, valores ou formas de contribuição — fiquem totalmente
                à vontade para entrar em contato diretamente conosco.

        As informações sobre os presentes são compartilhadas **apenas com os nubentes**.

        Que Deus abençoe cada gesto de carinho e sua generosidade 🙏
    """)

    # =========================
    # BUSCA DOS PRESENTES
    # =========================
    try:
        presentes = listar_presentes()
    except Exception:
        st.error("Não conseguimos carregar a lista agora. Tente novamente em instantes 🙏")
        return

    if not presentes:
        st.info("Todos os presentes já foram assumidos 🤍")
        return

    # =========================
    # CATEGORIAS
    # =========================
    contador_categorias = Counter(
        p["categoria"] for p in presentes if p.get("categoria")
    )

    categorias = ["Todas"] + sorted(contador_categorias.keys())

    st.markdown("### 🗂️ Categorias")

    cols_cat = st.columns(len(categorias))

    for col, categoria in zip(cols_cat, categorias):
        with col:
            label = (
                f"{categoria} ({contador_categorias[categoria]})"
                if categoria != "Todas"
                else "Todas"
            )

            selecionada = st.session_state["categoria_selecionada"] == categoria

            if st.button(
                label,
                key=f"cat_{categoria}",
                type="primary" if selecionada else "secondary",
            ):
                st.session_state["categoria_selecionada"] = categoria
                st.rerun()

    st.divider()

    # =========================
    # FILTRO POR CATEGORIA
    # =========================
    categoria_ativa = st.session_state["categoria_selecionada"]

    if categoria_ativa != "Todas":
        presentes = [
            p for p in presentes
            if p.get("categoria") == categoria_ativa
        ]

    # =========================
    # GRID DE PRESENTES
    # =========================
    cols = st.columns(COLUNAS_GRID)

    for idx, presente in enumerate(presentes):
        with cols[idx % COLUNAS_GRID]:
            st.markdown(
                f"""
                <div class="presente-card">
                    <strong>{html.escape(str(presente['produto']))}</strong><br>
                    <span>{presente['valor_exibicao']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button("Dar 🤍", key=f"btn_{presente['id']}"):
                reset_confirmacao()
                st.session_state["presente_selecionado"] = presente
                st.rerun()
