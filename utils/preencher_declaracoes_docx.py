import os
from docx import Document

def preencher_declaracoes_docx(NOME_ESTUDANTE,CPF,EMAIL,RESUMO_ATIVIDADE,DATA_INICIAL,DATA_FINAL,CARGA_HORARIA,DATA_EMISSAO,NOME_RESPONSAVEL):

    os.makedirs("declaracoes_geradas", exist_ok=True)

    doc = Document("modelo_declaracao.docx")

    for paragrafo in doc.paragraphs:
        for run in paragrafo.runs:
            run.text = run.text.replace("{{NOME_ESTUDANTE}}", NOME_ESTUDANTE)
            run.text = run.text.replace("{{CPF}}", CPF)
            run.text = run.text.replace("{{EMAIL}}", EMAIL)
            run.text = run.text.replace("{{RESUMO_ATIVIDADE}}", RESUMO_ATIVIDADE)
            run.text = run.text.replace("{{DATA_INICIAL}}", DATA_INICIAL)
            run.text = run.text.replace("{{DATA_FINAL}}", DATA_FINAL)
            run.text = run.text.replace("{{CARGA_HORARIA}}", CARGA_HORARIA)
            run.text = run.text.replace("{{DATA_EMISSAO}}", DATA_EMISSAO)
            run.text = run.text.replace("{{NOME_RESPONSAVEL}}", NOME_RESPONSAVEL)

    nome_normalizado = "_".join(NOME_ESTUDANTE.strip().split())
    nome_base = f"Declaracao_{nome_normalizado}"
    caminho_docx = os.path.join("declaracoes_geradas", f"{nome_base}.docx")

    doc.save(caminho_docx)

    print("DOCX gerado:", caminho_docx)