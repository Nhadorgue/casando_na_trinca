# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Sobre o projeto

"Casando na Trinca" — site/convite de casamento construído em **Python + Streamlit**, mantido por um analista de dados (não dev web; preferir soluções simples no ecossistema Streamlit a padrões de web dev tradicionais). Todo o conteúdo, nomes de variáveis e comunicação são em **português brasileiro**. Identidade visual: católica, romântica, minimalista — tema claro, azul serenity (`#91a8d0` / `#A7C7E7`), fonte serifada (ver `.streamlit/config.toml` e `assets/styles/theme.css`).

## Como trabalhar neste projeto

- Atuar com rigor de dev sênior+ — boas práticas, legibilidade e organização tanto no front-end quanto no back-end — e como especialista em UX design.
- O mantenedor é analista de dados em evolução (ainda não sênior): explicar decisões técnicas de forma didática, sem presumir conhecimento prévio de web dev.
- **Antes de qualquer push para o GitHub**, fazer uma revisão criteriosa do que será enviado ("estudar todos os pontos"): código revisado, nenhum segredo/credencial no diff, requirements coerentes com o código, app subindo localmente sem erro. O GitHub é a fonte da produção, mesmo com deploy manual.

### Sistema de design (obrigatório em qualquer mudança de front-end)

Identidade: **católica, romântica, minimalista**. Princípios concretos:

- Consistência de espaçamento (escala única, sem valores mágicos avulsos).
- Tipografia serifada bem pareada.
- Os azuis serenity como **sistema**: tokens CSS definidos no `:root` do `assets/styles/theme.css` (`--serenity-blue`, `--serenity-blue-forte`, `--serenity-blue-escuro`, `--texto-principal` etc.). Nunca repetir a cor hexadecimal avulsa — usar `var(--token)`.
- Transições suaves — movimento discreto, nada chamativo.

## Deploy e produção (Render)

- Repositório GitHub: `https://github.com/Nhadorgue/casando_na_trinca.git` (branch `main`).
- URL de produção: `https://casando-na-trinca.onrender.com/`
- Produção: **Web Service gratuito no Render** — 512 MB RAM, 0.1 CPU. Start Command: `streamlit run app.py`. Variáveis de ambiente configuradas no painel do Render (espelham o `.env` local, incluindo `GOOGLE_CREDENTIALS`).
- **Deploy é MANUAL** pelo painel do Render — push na `main` NÃO publica automaticamente.
- O `requirements.txt` tem **versões fixadas** (pinned) para garantir que o Render instale exatamente o que foi testado localmente. Ao atualizar uma dependência: atualizar local, testar, e só então mudar o pin.
- A instância gratuita hiberna após ~5 min sem tráfego (cold start ao acordar). Para evitar isso, um microserviço externo do usuário ("Pinger Bot", projeto separado) faz um GET em `https://casando-na-trinca.onrender.com/` a cada 120s, 24/7 (`REQUEST_TIMEOUT=30`). O usuário mantém instâncias separadas do mesmo bot para outros projetos (ex.: arte-up).
  - Atenção: manter um serviço acordado 24/7 consome ~730 das 750 instance-hours/mês do plano gratuito do Render.
- Status (julho/2026): site no ar, mas **ainda não divulgado aos convidados** — os acessos atuais são testes do casal + pings do bot. Há liberdade para ajustar sem risco, mas isso muda quando o link for enviado.

## Comandos

```bash
pip install -r requirements.txt
streamlit run app.py
```

Requer `.env` na raiz (gitignorado) com `GOOGLE_CREDENTIALS` contendo o JSON da service account do Google em uma única linha. Fallback: arquivo `utils/archives/google_credentials.json` (pasta também gitignorada). Sem credenciais, Recados, Presentes e a barra de recados quebram.

Não há linter configurado. Smoke test: `python tests/smoke_test.py` — renderiza as 5 páginas via `streamlit.testing.v1.AppTest` (lendo as planilhas reais) e exercita o modal de presente sem confirmar. **Nunca** clicar em "Sim, confirmar" em testes — escreve na planilha de produção. Rodar antes de qualquer push/deploy.

## Arquitetura

### Roteamento manual — NÃO é o multipage nativo do Streamlit

As páginas ficam em `views/` (nome escolhido de propósito: a pasta `pages/` ativaria o multipage automático do Streamlit, com navegação e URLs indesejadas). `app.py` é o único entry point: renderiza o menu horizontal (`components/menu.py`), que grava a página ativa em `st.session_state.pagina`, e despacha pelo dict `PAGINAS` para o `render()` do módulo correspondente.

Consequências práticas:
- Cada arquivo em `views/` é um módulo comum que expõe uma função `render()`; não colocar código Streamlit em nível de módulo (todos são importados no boot do app).
- Para navegar via código: `st.session_state["pagina"] = "<Nome da Página>"` (nomes: Casamento, Galeria, Sobre Nós, Recados, Presentes) seguido de `st.rerun()` quando fora do fluxo natural.
- Ordem de renderização em `app.py`: `load_css()` → menu → barra de recados (letreiro CSS) → página ativa → footer.

### Dados: Google Sheets no lugar de banco de dados

Todo dado dinâmico vive em duas planilhas Google acessadas via `gspread` + service account. A autenticação é única e compartilhada: `utils/google_auth.py` (credenciais + `get_client()` cacheado); os módulos de acesso apenas abrem as worksheets:

| Planilha | Worksheet | Módulo de acesso | Conteúdo |
|---|---|---|---|
| `Casando_na_Trinca_Recados` | sheet1 | `utils/google_sheets.py` | Recados (Recado, Nome, data, Aprovado) |
| `Casando_na_Trinca_Presentes` | `presentes` | `utils/google_sheets_presentes.py` | Catálogo de presentes |
| `Casando_na_Trinca_Presentes` | `assumidos` | `utils/google_sheets_presentes.py` | Quem assumiu cada presente |

O domínio de **presentes** segue camadas: `views/presentes.py` → `services/` (regras de negócio: formatação de valor em `presentes_service.py`, fluxo de confirmação em `assumidos_service.py`, `ID_PRESENTE_PIX = 50`) → `repositories/` (leitura/escrita nas worksheets) → `utils/google_sheets_presentes.py` (worksheets) → `utils/google_auth.py` (client/credenciais). **Recados** não segue essas camadas — a página e a barra falam direto com `utils/google_sheets.py`.

Convenções das planilhas:
- Booleanos são strings `"TRUE"`/`"FALSE"` — comparar com `str(x).upper() == "TRUE"`.
- Recados só aparecem no site com `Aprovado = TRUE` (moderação manual, feita direto na planilha).
- Presente assumido = coluna 5 (`COLUNA_ASSUMIDO` em `repositories/presentes_repository.py`) = `"TRUE"` na worksheet `presentes`; ele some da lista exibida.
- `marcar_como_assumido` localiza a linha pelo `id` iterando a partir da linha 2 (linha 1 é cabeçalho).
- Timestamps gravados nas planilhas usam `utils/datas.py` (`agora_brasil()`, fuso -03:00) — nunca `datetime.now()` puro, porque o Render roda em UTC.

Cache do Streamlit: client e worksheets usam `@st.cache_resource`; a leitura de recados usa `@st.cache_data(ttl=30)` e é invalidada com `get_recados_aprovados.clear()` após inserir. Ou seja, edições feitas direto na planilha demoram até 30s para aparecer no site. Imagens base64 (`utils/background.py`) também são cacheadas com `@st.cache_data`.

### Estado e UI

- O fluxo de confirmação de presente é um `st.dialog` (`dialogo_confirmacao` em `views/presentes.py`) dirigido por estado: o modal reabre a cada rerun enquanto `presente_selecionado` existir no `st.session_state`; o X do modal limpa o estado via `on_dismiss=limpar_estado_presente`. Fases: nome → "tem certeza?" (`confirmar_definitivo`) → agradecimento (`presente_confirmado`). Chaves: `presente_selecionado`, `confirmar_definitivo`, `presente_confirmado`, `nome_convidado`. Os helpers de limpeza estão em `utils/session.py` — ao adicionar chaves novas, atualizar `CHAVES_CONFIRMACAO` lá.
- CSS global em `assets/styles/theme.css` (tokens no `:root`), injetado por `utils/style.py` a cada rerun (sem cache de propósito, para refletir edições no CSS). O menu é estilizado via classe `.st-key-menu_navegacao` (gerada pelo `st.container(key="menu_navegacao")` em `components/menu.py`).
- Conteúdo vindo de convidados (recados, nomes) **sempre** passa por `html.escape()` antes de entrar em `st.markdown(..., unsafe_allow_html=True)` — proteção contra XSS.
- Imagens de presentes seguem o padrão `assets/images/presentes/{id}.jpg`, com fallback `utensilios.jpg`.
- O contador regressivo (`views/casamento.py`) é HTML/JS embutido via `st.iframe` — roda no navegador do convidado, sem reruns no servidor. Data, local e endereço do casamento são constantes no topo desse arquivo (`DATA_CASAMENTO_ISO` alimenta o JS).
- A barra de recados (`components/recados_barra.py`) é um letreiro com animação CSS (`.recados-marquee` no theme.css); a duração é proporcional ao tamanho do texto.
