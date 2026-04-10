import os
import json
import requests
import time  
from dotenv import load_dotenv

diretorio_script = os.path.dirname(os.path.abspath(__file__))
diretorio_raiz = os.path.abspath(os.path.join(diretorio_script, "..", ".."))
caminho_env = os.path.join(diretorio_raiz, ".env")

load_dotenv(caminho_env)
API_KEY = os.environ.get("API_FOOTBALL_KEY")

def extrair_copa(cod_liga, cod_temporada):
    pasta_destino = os.path.join(diretorio_raiz, "data", "raw")
    
    url = "https://v3.football.api-sports.io/fixtures"
    
    cabecalho = {
        "x-apisports-key": API_KEY
    }
    
    resposta = requests.get(url, headers=cabecalho, params={
        "league": cod_liga,
        "season": cod_temporada
    })

    if resposta.status_code == 200:
        dados_json = resposta.json()
        
        # CORREÇÃO 1: Nome do arquivo dinâmico baseado no ano
        nome_arquivo = f"api_world_cup_{cod_temporada}.json"
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
        
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_json, arquivo, ensure_ascii=False, indent=4)
            
        print(f"Copa {cod_temporada}: {nome_arquivo}")


if __name__ == "__main__":
    copas_ano = {"2010": 750, "2014": 749, "2018": 1, "2022": 4265}

    for ano, id_liga in copas_ano.items():
        extrair_copa(id_liga, ano)
        
        #Pausa de 2 segundos para não tomar block da API
        time.sleep(2)
        