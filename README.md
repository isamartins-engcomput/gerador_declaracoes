# 📄 Gerador de Declarações em PDF

Este é um projeto em Python desenvolvido para automatizar a geração de declarações complementares a partir de um modelo `.docx` e uma lista de estudantes em arquivo `.csv`. As declarações são geradas em PDF, com backup automático dos dados e controle de status para evitar duplicações.

---

## ✅ Funcionalidades

- Leitura de estudantes a partir de `dados/estudantes.csv`
- Geração automática de arquivos `.docx` preenchidos
- Conversão dos arquivos `.docx` para `.pdf`
- Backup completo das declarações geradas e do arquivo CSV
- Controle de status de cada estudante: `PENDENTE` ou `GERADA`

---

## ⚙️ Pré-requisitos

- Python 3.12
- LibreOffice (Linux) **ou** Pandoc + LaTeX (Windows/Linux)

### Linux - LibreOffice:

```bash
sudo apt install python3.12-venv libreoffice
```

### Windows:

- Instale o [Pandoc] (https://pandoc.org/installing.html)
- Instale o MikTeX ou outro compilador LaTeX

---

## 📥 Clonando o Projeto via Git

Para baixar o projeto do GitHub:

```bash
git clone https://github.com/isamartins-engcomput/gerador_declaracoes.git
cd gerador_declaracoes
```

---

## ♻️ Configuração do Ambiente Virtual (recomendado)

Dentro do repositório clonado, siga os passos:

1. Instale o venv (se ainda não estiver instalado):
`sudo apt install python3.12-venv`

2. Crie o ambiente virtual:
`python3 -m venv venv`

3. Ative o ambiente virtual:
`source venv/bin/activate`       # Linux/macOS
`venv\Scripts\activate`          # Windows

4. Instale as dependências:
`pip install -r requirements.txt`

---

## 📁 Estrutura de Diretórios

```
gerador_declaracoes/
├── backup/                  # backups com PDFs e CSVs por data
├── dados/                   # arquivo CSV dos estudantes
│   └── estudantes.csv
├── declaracoes_geradas/     # arquivos .pdf gerados
├── utils/                   # funções auxiliares do sistema
├── venv/                    # ambiente virtual
├── main.py                  # script principal de execução
├── modelo_declaracao.docx   # modelo da declaração
├── README.md                # este arquivo
└── requirements.txt         # dependências do projeto
```

---

## 📝 Formato do CSV (`dados/estudantes.csv`)

O cabeçalho do CSV deve conter:

```csv
NOME_ESTUDANTE,CPF,EMAIL,RESUMO_ATIVIDADE,DATA_INICIAL,DATA_FINAL,CARGA_HORARIA,DATA_EMISSAO,NOME_RESPONSAVEL,STATUS
João da Silva,12345678900,joao@email.com,"Participação em palestra",2024-06-01,2024-06-02,4,2024-06-05,Prof. Maria,PENDENTE
```

⚠️ Apenas estudantes com `STATUS = PENDENTE` (em qualquer capitalização) terão declarações geradas. O campo `STATUS` será atualizado automaticamente para `GERADA` após a emissão.

---

## ▶️ Execução

Com o repositório clonado, o ambiente virtual ativado e o arquivo CSV contendo os dados dos estudantes completo, execute o programa:

```bash
python main.py
```

---

## 🚧 Observações

- O arquivo `estudantes.csv` deve estar dentro da pasta `dados/` com o cabeçalho exato indicado acima.
- Não deixe linhas em branco ou campos sem preencher no CSV.
- Os modelos `.docx` devem conter os placeholders como `{{NOME_ESTUDANTE}}`, `{{EMAIL}}`, etc.
- Após o backup, você deve encontrar uma pasta com o dia atual (`backup/YYYY-MM-DD/`) contendo todos os `.pdf` gerados na pasta `declaracoes_geradas`, além de uma cópia de `estudantes.csv` com status atualizados.

---

## 🛡️ Licença

Este projeto é livre para uso acadêmico, educacional ou pessoal. Para usos comerciais, entre em contato com a autora.

---

## 🎓 Autora

Projeto desenvolvido por **Isadora de Souza Martins**, estudante de Engenharia de Computação (2° semestre) no IFMS Campus Três Lagoas, como parte de um desafio de automação de documentos com Python.
