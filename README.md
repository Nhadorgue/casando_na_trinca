# 💍 Casando na Trinca

**Casando na Trinca** é um site de casamento desenvolvido em **Python + Streamlit**, criado para ser **informativo, interativo e consultivo**, unindo tecnologia, organização e espiritualidade ✨  
Embora seja um projeto pessoal (meu casamento 😄), ele foi pensado desde o início com **boas práticas de desenvolvimento**, estrutura clara e mentalidade profissional.

O site será o principal canal digital para convidados conhecerem nossa história, acessarem informações do casamento, escolherem presentes e deixarem recados especiais 💙

---

## ✝️ Propósito do Projeto

Mais do que um site, este projeto reflete nossa fé e nosso caminho como casal.  
A linguagem visual e textual do sistema segue uma linha:

- Espiritual (católicos apostólicos romanos)
- Romântica
- Minimalista e elegante
- Profissional

Inspirado na **Sagrada Família**, na devoção à **Virgem Maria**, **São José**, **São Josemaria Escrivá**, **Santa Teresinha do Menino Jesus** e **São Bento** 🙏

---

## 🎯 Objetivos

- Centralizar todas as informações do casamento em um único local
- Facilitar a escolha e confirmação de presentes
- Criar um espaço para interação dos convidados
- Substituir banco de dados tradicional por **Google Sheets**, com dados online e quase em tempo real
- Manter um projeto simples, organizado e sustentável

---

## 🧭 Estrutura do Site (Menu Superior)

O site será dividido em páginas acessadas por um **menu horizontal fixo no topo**, contendo:

### 💒 Casamento
- Data: **123456789**
- Local: **localização**  
  _rua_
- Contador regressivo em tempo real (dias, horas, minutos e segundos)
- Galeria de fotos da igreja em formato de slides
- Endereço e integração com mapa (estilo Google Maps)

---

### 🖼️ Galeria
- Fotos do casal distribuídas de forma elegante
- Animações leves e suaves
- Estrutura flexível para:
  - Pastas locais
  - Integração futura com Google Fotos ou links externos

---

### 💑 Sobre Nós
- História do casal desde o início do relacionamento
- Texto dividido em blocos leves e alternados (esquerda/direita)
- Imagens integradas ao longo do texto  
📌 *Conteúdo em construção*

---

### 💌 Recados
- Página dedicada aos recados deixados pelos convidados
- Funcionalidades:
  - Visualizar recados existentes
  - Deixar um novo recado (nome + mensagem)
  - Armazenamento em Google Sheets (1 recado por linha)
- Linha fixa abaixo do menu exibindo recados em rolagem contínua
- Opção administrativa de exclusão de recados diretamente na planilha

---

### 🎁 Presentes
Página principal do projeto.

- Lista de **101 presentes**
  - 100 produtos físicos
  - 1 opção de presente via **PIX**
- Produtos exibidos em páginas (24 por página)
- Cada produto contém:
  - Imagem
  - Nome
  - Valor aproximado

---

## 📂 Organização do Projeto (visão geral)
casando-na-trinca/
│
├── app.py
├── pages/
│   ├── casamento.py
│   ├── galeria.py
│   ├── sobre_nos.py
│   ├── recados.py
│   └── presentes.py
│
├── assets/
│   ├── imagens/
│   └── estilos/
│
├── services/
│   └── google_sheets.py
│
├── .gitignore
├── requirements.txt
└── README.md

---

## 🚧 Status do Projeto
🛠️ Em desenvolvimento por etapas
Cada página será tratada individualmente, mantendo organização e clareza no avanço do projeto.

---

## 🤝 Contribuições
Este é um projeto pessoal, mas ideias, sugestões e boas práticas são sempre bem-vindas ✨

---
## 💬 Frase Inspiradora
>💡 “Sozinhos podemos fazer pouco; juntos podemos fazer muito." — **Helen Keller**

---
## ▶️ Como executar
```bash
pip install -r requirements.txt
streamlit run app.py