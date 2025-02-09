import requests
import time
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import BitcoinPrice, Base
import os
from dotenv import load_dotenv
from flask import Flask, jsonify  
import threading 

# Carrega as variáveis de ambiente
load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

DATABASE_URL = (f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
               f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

app = Flask(__name__)  

@app.route('/health', methods=['GET'])  
def health_check():  
    return jsonify({"status": "running"}), 200  

def run_app():  
    app.run(host='0.0.0.0', port=5000)  

# Função para criar a tabela bitcoin_prices
def criar_tabela():
    """Cria a tabela bitcoin_prices se ela não existir."""
    Base.metadata.create_all(engine)
    print("Tabela criada com sucesso!")

# Função para registro dos preços no banco de dados
def salvar_dados_no_banco(dados):
    """Salva os dados no banco de dados PostgreSQL."""
    session = Session()
    novo_registro = BitcoinPrice(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")

# Função para obter o preço atual do Bitcoin
def get_bitcoin_price_binance():
    # Endpoint da API da Binance para obter o preço atual do BTC/USDT

    url = "https://api.binance.com/api/v3/ticker/price"

    params = {"symbol": "BTCUSDT"} 

    # Envia a requisição GET para a API
    response = requests.get(url, params=params)

    # Registra o momento de aquisição do valor
    timestamp = datetime.now()

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        price = round(float(data["price"]), 2)
        return {'timestamp': timestamp, 
                'symbol': "BTC/USDT",
                'price': price}
    else:
        print(f"Erro ao obter o preço do Bitcoin: {response.status_code}")
        return None

if __name__  == "__main__":
    criar_tabela()
    print("Iniciando a coleta de dados...")

    # Inicia o servidor Flask em uma thread separada  
    threading.Thread(target=run_app).start()  

    while True:
        try: 
            dados = get_bitcoin_price_binance()
            if dados:
                salvar_dados_no_banco(dados)
            else:
                print("Nenhum dado disponível. Aguardando 15 segundos...")
            time.sleep(15)
        except Exception as e:
            print(f"Erro ao coletar dados: {e}")
            time.sleep(15)