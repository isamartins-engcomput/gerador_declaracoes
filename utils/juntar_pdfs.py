import os
from pypdf import PdfWriter

def juntar_pdfs():
    
    pasta = "declaracoes_geradas"
    arquivos_pdf = sorted([f for f in os.listdir(pasta) if f.endswith(".pdf")])
    
    if not arquivos_pdf:
        print("\nNenhum PDF encontrado para juntar.")
        return

    escritor = PdfWriter()

    for arquivo in arquivos_pdf:

        caminho_arquivo = os.path.join(pasta, arquivo)

        with open(caminho_arquivo, "rb") as f:
            escritor.append(f)

    caminho_saida = os.path.join(pasta,"Declarações_Unificadas.pdf")

    with open(caminho_saida, "wb") as saida:
        escritor.write(saida)
    
    print(f"\nPDF único gerado em: {caminho_saida}")