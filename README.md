# Gerador de Declarações em PDF

Este é um sistema em Python que gera declarações personalizadas em PDF para estudantes, com base em um modelo `.docx`. Ele também realiza o backup automático dos arquivos gerados.

---

## 🚀 Funcionalidades

* Gera declarações em `.docx` preenchidas com dados de estudantes
* Converte automaticamente para `.pdf`
* Salva arquivos em uma pasta organizada
* Realiza backup das declarações e dados em pastas separadas por data

---

## ⚖️ Requisitos

* Python 3.12 instalado
* Linux (ou Windows com adaptações)

### Pacotes Python:

* `python-docx`
* `pypandoc`

### Dependências externas:

* **Linux:** `libreoffice`, `pandoc` e `texlive-xetex`
* **Windows:** `pandoc` e LaTeX (com `MiKTeX` ou `TeX Live`)

---

## ♻️ Configuração do Ambiente Virtual (Linux)

1. Instale o venv (se ainda não estiver instalado):
   ```bash
   sudo apt install python3.12-venv
   ```
2. Crie o ambiente virtual:
   ```bash
   python3 -m venv venv
   ```
3. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Instale as dependências externas:
   ```bash
   sudo apt install libreoffice pandoc texlive-xetex
   ```

---

## 📁 Estrutura esperada do projeto

```
./gerador_declaracoes/
├── venv/                     # ambiente virtual
├── declaracoes_geradas/     # pasta onde são salvos os arquivos .docx e .pdf
├── dados/                   # arquivos CSV temporários
├── backup/                  # pastas com backup por data
├── utils/                   # módulos python separados (ex: gerar_pdf.py)
├── modelo.docx              # modelo base da declaração
├── requirements.txt         # dependências
└── main.py                  # arquivo principal para execução
```

---

## ▶️ Como Executar o Projeto

1. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```
2. Execute o script principal:
   ```bash
   python main.py
   ```

---

## 🚧 Observações

* O arquivo `estudantes_temp.csv` é usado temporariamente para gerar os dados das declarações.
* Após o backup, o CSV é excluído automaticamente.
* O LibreOffice é usado no Linux para converter `.docx` em `.pdf`, garantindo compatibilidade.

---

## 🎓 Autora

Projeto desenvolvido pela estudante Isadora de Souza Martins, para o desafio de automação de documentos usando Python.
