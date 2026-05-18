"""Serviços externos usados pelo app de gastos."""

import requests


def buscar_cotacao_dolar():
    """Busca a cotação atual do dólar em real usando a AwesomeAPI."""

    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    cotacao = dados["USDBRL"]

    return {
        "nome": cotacao["name"],
        "valor": cotacao["bid"],
        "data": cotacao["create_date"],
    }