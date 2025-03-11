import pytest
from currency_converter import converter_moeda, obter_taxas_cambio

@pytest.fixture
def taxas_mock():
    """Simula taxas de câmbio fixas para testes."""
    return {
        "USD": 1.0,
        "BRL": 5.0,
        "EUR": 0.85,
    }

def test_converter_moeda_basico(taxas_mock):
    """Testa conversão básica com valores conhecidos."""
    assert converter_moeda(10, "USD", "BRL", taxas_mock) == 50.0
    assert converter_moeda(50, "BRL", "USD", taxas_mock) == 10.0
    assert converter_moeda(10, "USD", "EUR", taxas_mock) == 8.5

def test_converter_moeda_valores_extremos(taxas_mock):
    """Testa conversão com valores pequenos e grandes."""
    assert converter_moeda(0.01, "USD", "BRL", taxas_mock) == 0.05
    assert converter_moeda(1000000, "BRL", "USD", taxas_mock) == 200000.0

def test_converter_moeda_negativos(taxas_mock):
    """Testa conversão com valores negativos."""
    assert converter_moeda(-10, "USD", "BRL", taxas_mock) == -50.0

def test_converter_moeda_mesma_moeda(taxas_mock):
    """Testa conversão entre a mesma moeda."""
    assert converter_moeda(10, "USD", "USD", taxas_mock) == 10.0

def test_converter_moeda_taxa_ausente(taxas_mock):
    """Testa conversão quando a taxa de uma moeda não está disponível."""
    with pytest.raises(KeyError):
        converter_moeda(10, "GBP", "USD", taxas_mock)

def test_obter_taxas_cambio_mock(mocker):
    """Simula uma resposta da API e testa a função."""
    mock_response = {
        "result": "success",
        "conversion_rates": {"USD": 1.0, "BRL": 5.0, "EUR": 0.85}
    }
    mocker.patch("requests.get", return_value=mocker.Mock(json=lambda: mock_response))
    assert obter_taxas_cambio() == mock_response["conversion_rates"]
