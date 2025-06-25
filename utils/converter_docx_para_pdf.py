import os
import platform
import shutil
from subprocess import run, PIPE

try:
    import pypandoc
except ImportError:
    pypandoc = None

def converter_docx_para_pdf():

    print("\n")
    
    pasta_entrada = "declaracoes_geradas"
    os.makedirs(pasta_entrada, exist_ok=True)

    arquivos_encontrados = os.listdir(pasta_entrada)

    for arquivo in arquivos_encontrados:

        if arquivo.endswith(".docx") and arquivo.startswith("Declaracao_"):
            
            caminho_docx = os.path.join(pasta_entrada, arquivo)
            nome_base = os.path.splitext(arquivo)[0]
            caminho_pdf = os.path.join(pasta_entrada, nome_base + ".pdf")
            sistema = platform.system()

            if sistema == "Windows" and pypandoc:
                
                try:
                    pypandoc.convert_file(
                        source_file=caminho_docx,
                        to="pdf",
                        outputfile=caminho_pdf,
                        extra_args=["--pdf-engine=xelatex"]
                    )
                    print("PDF gerado com pypandoc no Windows:", caminho_pdf)
                except Exception as e:
                    print("\nErro ao converter com pypandoc no Windows:", e)

            elif sistema != "Windows" and shutil.which("libreoffice"):
                
                resultado = run([
                    "libreoffice",
                    "--headless",
                    "--convert-to", "pdf",
                    "--outdir", pasta_entrada,
                    caminho_docx
                ], stdout=PIPE, stderr=PIPE, text=True)
                pdf_temp = os.path.join(pasta_entrada, nome_base + ".pdf")

                if resultado.returncode == 0 and os.path.exists(caminho_pdf):
                    print("PDF gerado no Linux com LibreOffice:", caminho_pdf)
                else:
                    print(f"\nFalha na conversão com LibreOffice. Saída:\n{resultado.stderr}")


            elif pypandoc:
 
                try:
                    pypandoc.convert_file(
                        source_file=caminho_docx,
                        to="pdf",
                        outputfile=caminho_pdf,
                        extra_args=["--pdf-engine=xelatex"]
                    )
                    print("\nPDF gerado com pypandoc:", caminho_pdf)
                    
                except Exception as e:
                    print("\nErro ao converter com pypandoc:", e)

            else:
                print("\nErro: Nenhum método de conversão disponível. Dê uma olhada no README.md ou instale LibreOffice ou pypandoc + LaTeX.")

            if os.path.exists(caminho_pdf):
                os.remove(caminho_docx)
