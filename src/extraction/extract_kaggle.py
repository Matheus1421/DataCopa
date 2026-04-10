import os
import zipfile
from dotenv import load_dotenv

diretorio_script = os.path.dirname(os.path.abspath(__file__))
diretorio_raiz = os.path.abspath(os.path.join(diretorio_script, "..", ".."))
caminho_env = os.path.join(diretorio_raiz, ".env")

load_dotenv(caminho_env)

from kaggle.api.kaggle_api_extended import KaggleApi

def extrair_dados_historicos():
    pasta_destino = os.path.join(diretorio_raiz, "data", "raw")
    os.makedirs(pasta_destino, exist_ok=True)

    print("🔐 Autenticando na API do Kaggle...")
    api = KaggleApi()
    api.authenticate()

    
    dataset_slug = "abecklas/fifa-world-cup" 

    api.dataset_download_files(dataset_slug, path=pasta_destino)
    
    nome_zip = dataset_slug.split('/')[-1] + ".zip"
    caminho_zip = os.path.join(pasta_destino, nome_zip)

    if os.path.exists(caminho_zip):
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.extractall(pasta_destino)
            
        os.remove(caminho_zip)

if __name__ == "__main__":
    extrair_dados_historicos()