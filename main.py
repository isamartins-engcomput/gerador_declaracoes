import os
from utils.ler_estudantes_csv import ler_estudantes_csv
from utils.preencher_declaracoes_docx import preencher_declaracoes_docx
from utils.converter_docx_para_pdf import converter_docx_para_pdf
from utils.backup_completo import backup_completo
from utils.atualizar_status_csv import atualizar_status_csv

try:
    largura_terminal = os.get_terminal_size().columns
except OSError:
    largura_terminal = 80

print("\n")
texto = "|============================<<<<< ~ GERADOR DE DECLARAÇÕES ~ >>>>>============================|"
print(texto.center(largura_terminal))
print("\n")

def main():
    
    estudantes = ler_estudantes_csv()

    houve_geracao = False

    if not estudantes:
        print("\nNenhum estudante encontrado.\n")
        return

    for i, estudante in enumerate(estudantes):
       
        if estudante["STATUS"] != "GERADA":
            print(f"\nGerando declaração do estudante {i + 1}...")

            preencher_declaracoes_docx (
                estudante["TITULO_ATIVIDADE"],
                estudante["NOME_ESTUDANTE"],
                estudante["CPF"],
                estudante["RESUMO_ATIVIDADE"],
                estudante["DATA_INICIAL"],
                estudante["DATA_FINAL"],
                estudante["CARGA_HORARIA"],
                estudante["DATA_EMISSAO"],
                estudante["NOME_RESPONSAVEL"],
            )
            atualizar_status_csv(estudante["NOME_ESTUDANTE"])
            houve_geracao = True

        else:
            print(f"Pulando estudante {i + 1} - Declaração com status 'GERADA'.")
    
    if houve_geracao:
        converter_docx_para_pdf()
        backup_completo()
    else:
        print("\nNenhuma declaração com status 'PENDENTE' foi encontrada.")

if __name__ == "__main__":
    main()

print("\n")
texto = "|===============================<<<<< ~ FIM DO PROGRAMA! ~ >>>>>===============================|"
print(texto.center(largura_terminal))
print("\n")