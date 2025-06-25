import csv
import os

def ler_estudantes_csv():
    
    caminho_csv = os.path.join("dados", "estudantes.csv")

    if not os.path.exists(caminho_csv):
        print("\nArquivo CSV não encontrado.")
        return []

    estudantes = []

    with open(caminho_csv, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)

        for linha in leitor:
            estudante = {chave.strip().upper(): valor.strip() for chave, valor in linha.items()}
            estudante["STATUS"] = estudante.get("STATUS", "").upper()
            estudantes.append(estudante)

    return estudantes