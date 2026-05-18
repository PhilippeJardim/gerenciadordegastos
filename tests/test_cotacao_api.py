from gastos.services import buscar_cotacao_dolar


class RespostaMock:
    def raise_for_status(self):
        pass

    def json(self):
        return {
            "USDBRL": {
                "name": "Dólar Americano/Real Brasileiro",
                "bid": "5.20",
                "create_date": "2026-05-17 10:00:00",
            }
        }


def test_buscar_cotacao_dolar(monkeypatch):
    def get_mock(url, timeout):
        return RespostaMock()

    monkeypatch.setattr("requests.get", get_mock)

    resultado = buscar_cotacao_dolar()

    assert resultado["nome"] == "Dólar Americano/Real Brasileiro"
    assert resultado["valor"] == "5.20"
    assert resultado["data"] == "2026-05-17 10:00:00"