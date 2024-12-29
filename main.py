import requests
import time
import sqlite3
import pandas as pd

def get_bitcoin_price_binance():
    # Endpoint da API da Binance para obter o preço atual do BTC/USDT
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": "BTCUSDT"} 

    # Envia a requisição GET para a API
    response = requests.get(url, params=params)

    # Registra o momento de aquisição do valor
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        price = round(float(data["price"]), 2)
        return {'timestamp': timestamp, 
                'symbol': "BTC/USDT",
                'price': price}
    else:
        return None

def create_connection(db_name='bitcoin_history.db'):
    """Cria uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(db_name)
    return conn

def setup_database(conn):
    """Cria a tabela bitcoin_prices se ela não existir."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            symbol TEXT, 
            price REAL
        )
    ''')
    conn.commit()

def save_to_database(conn, data):
    """Salva uma linha de dados no banco de dados SQLite usando pandas."""
    df = pd.DataFrame([data])  # Converte o dicionário em um DataFrame de uma linha
    df.to_sql('bitcoin_prices', conn, if_exists='append', index=False)  # Salva no banco de dados

# Chama a função para registro dos preços no banco de dados
if __name__  == "__main__":
    conn = create_connection()
    setup_database(conn)

    while True:
        # Faz a aquisição do valor de bitcoin retornando {'timestamp', 'symbol', 'price'}
        result = get_bitcoin_price_binance()
        save_to_database(conn, result)
        print("Dados salvos no banco: ", result)

        # Aguarda 10 segundo para o próximo registro
        time.sleep(10)