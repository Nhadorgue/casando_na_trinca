import streamlit as st
from utils.background import apply_virgem_maria_background
from services.presentes_service import listar_presentes
from services.assumidos_service import confirmar_presente_service
from utils.session import limpar_estado_presente, reset_confirmacao


# =========================
# CONFIRMAÇÃO DEFINITIVA
# =========================
def confirmar_definitivo():
    st.markdown("### 🤍 Tem certeza da sua escolha?")

    with st.container(border=True):

        # =========================
        # FASE 1 — CONFIRMAÇÃO
        # =========================
        if not st.session_state.get("presente_confirmado"):

            st.markdown("Este presente ficará reservado em seu nome.")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Voltar"):
                    st.session_state["confirmar_definitivo"] = False
                    st.rerun()

            with col2:
                if st.button(
                    "Sim, confirmar",
                    disabled=st.session_state.get("processando_confirmacao", False)
                ):
                    # EXECUTA A CONFIRMAÇÃO AQUI
                    confirmar_presente_service()
                    st.session_state["presente_confirmado"] = True

        # =========================
        # FASE 2 — AGRADECIMENTO
        # =========================
        if st.session_state.get("presente_confirmado"):
            st.success("🎉 Muito obrigado pelo carinho e sua generosidade!")
            st.info("Se quiser pode deixar um recado para nós... 🤍")
            st.info("Esse ficará visível em todas as páginas após o menu na parte de cima 😉")

            if st.button("💌 Ir para Recados"): ######  AINDA ESTA COM BUG
                st.session_state["pagina"] = "Recados"
                # limpar_estado_presente()
                # st.rerun()


# =========================
# PAINEL DE CONFIRMAÇÃO
# =========================
def painel_confirmacao_presente(presente):
    with st.container(border=True):
        st.markdown("## 🎁 Confirmar Presente")

        st.image("assets/images/presentes/utensilios.jpg")
        st.markdown(f"### {presente['produto']}")
        st.markdown(f"**Valor aproximado:** {presente['valor_exibicao']}")

        nome = st.text_input(
            "Seu nome 🤍",
            key=f"nome_{presente['id']}"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Cancelar", key=f"cancelar_{presente['id']}"):
                limpar_estado_presente()
                st.rerun()

        with col2:
            if st.button("Confirmar Presente", key=f"confirmar_{presente['id']}"):
                if not nome.strip():
                    st.warning("Informe seu nome 🙏")
                else:
                    st.session_state["nome_convidado"] = nome
                    st.session_state["confirmar_definitivo"] = True

        if st.session_state.get("confirmar_definitivo"):
            confirmar_definitivo()


# =========================
# RENDER PRINCIPAL
# =========================
def render():
    # Estados base
    st.session_state.setdefault("abrir_modal_presente", False)
    st.session_state.setdefault("processando_confirmacao", False)

    st.markdown(apply_virgem_maria_background(), unsafe_allow_html=True)
    st.title("🎁 Lista de Presentes")

    st.markdown("""
        Com muito carinho, preparamos esta lista para facilitar a vida de quem deseja nos presentear 🤍 
        
        Os valores colocados na lista **são apenas uma média** dos presentes que pesquisamos, não necessariamente 
                significa que os presentes devem ser nesses mesmos valores 
                
        Existe também a opção de nos presentear com **Pix** para aqueles casos em que a pessoa não encontre o 
                presente ou prefira esse modo de presentear...também será muito bem recebido 😅 
                
        Caso surja qualquer dúvida — sobre os presentes, valores ou formas de contribuição — fiquem totalmente 
                à vontade para entrar em contato diretamente conosco. 
                
        As informações sobre os presentes é, e estão sendo, compartilhadas **apenas com os nubentes**. 
        
        Que Deus abençoe cada gesto de carinho e sua generosidade 🙏
    """)

    st.divider()

    presentes = listar_presentes()

    if not presentes:
        st.info("Todos os presentes já foram assumidos 🤍")
        return

    cols = st.columns(4)

    for idx, presente in enumerate(presentes):
        with cols[idx % 4]:

            # CARD DO PRESENTE
            st.markdown(
                f"""
                <div style="
                    padding: 12px;
                    border-radius: 14px;
                    border: 1px solid #e5e5e5;
                    background-color: rgba(255,255,255,0.85);
                    margin-bottom: 12px;
                ">
                    <strong>{presente['produto']}</strong><br>
                    <span style="color:#555">{presente['valor_exibicao']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button("Dar 🤍", key=f"btn_{presente['id']}"):
                reset_confirmacao()
                st.session_state["presente_selecionado"] = presente
                st.session_state["abrir_modal_presente"] = True
                st.rerun()

            # 👇 CONFIRMAÇÃO ABAIXO DO CARD CORRETO
            if (
                st.session_state.get("abrir_modal_presente")
                and st.session_state.get("presente_selecionado")
                and st.session_state["presente_selecionado"]["id"] == presente["id"]
            ):
                painel_confirmacao_presente(presente)

