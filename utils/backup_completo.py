import os
import shutil
from datetime import datetime

def backup_completo():

    pasta_origem_pdfs = "declaracoes_geradas"

    if not os.path.exists(pasta_origem_pdfs):
        print("\nErro: Nenhuma declaração encontrada para backup.")
        return

    os.makedirs("backup",exist_ok=True)

    data = datetime.now().strftime("%Y-%m-%d")
    pasta_destino = os.path.join("backup", data)
    os.makedirs(pasta_destino, exist_ok=True)

    for raiz, _, arquivos in os.walk(pasta_origem_pdfs):
        for arquivo in arquivos:
            if arquivo.endswith(".pdf"):
                origem = os.path.join(raiz, arquivo)
                destino = os.path.join(pasta_destino, arquivo)
                shutil.copy2(origem, destino)

    caminho_csv = os.path.join("dados", "estudantes.csv")

    origem = os.path.join("dados", "estudantes.csv")
    destino = os.path.join(pasta_destino, "estudantes_backup.csv")
    
    if os.path.exists(origem):
        shutil.copy2(origem, destino)
    else:
        print("\nNenhum dado encontrado para backup.")

    print(f"\nBackup completo concluído em: {pasta_destino}")