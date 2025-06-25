import csv
import os

def atualizar_status_csv(nome_estudante):
    
    caminho_csv = os.path.join("dados", "estudantes.csv")
    temp_path = os.path.join("dados", "temp.csv")

    with open(caminho_csv, mode='r', encoding='utf-8') as arquivo_original, \
         open(temp_path, mode='w', encoding='utf-8', newline='') as arquivo_temp:

        leitor = csv.DictReader(arquivo_original)
        campos = leitor.fieldnames

        escritor = csv.DictWriter(arquivo_temp, fieldnames=campos)
        escritor.writeheader()

        for linha in leitor:
            
            if linha["NOME_ESTUDANTE"] == nome_estudante and linha["STATUS"].strip().upper() != "GERADA":
                linha["STATUS"] = "GERADA"
                
            escritor.writerow(linha)

    os.replace(temp_path, caminho_csv)