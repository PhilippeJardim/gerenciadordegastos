import requests


def buscar_cotacao_dolar():
    """Busca a cotação atual do dólar."""

    # URL da API
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    # Faz a requisição
    resposta = requests.get(url, timeout=10)

    # Verifica se houve erro
    resposta.raise_for_status()

    # Converte JSON para dicionário Python
    dados = resposta.json()

    # Pega os dados do dólar
    dolar = dados["USDBRL"]

    # Retorna os dados organizados
    return {
        "nome": dolar["name"],
        "valor": dolar["bid"],
        "data": dolar["create_date"],
    }