import requests

def get_bitcoin_price_binance():
    # Endpoint da API da Binance para obter o preço atual do BTC/USDT
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": "BTCUSDT"} 

    # Envia a requisição GET para a API
    response = requests.get(url, params=params)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        price = float(data["price"])
        return f"O preço atual do Bitcoin é ${price:.2f} USD"
    else:
        return f"Erro na API: {response.status_code} - {response.text}"


# Chama a função e exibe o preço
if __name__  == "__main__":
    result = get_bitcoin_price_binance()
    print(result)