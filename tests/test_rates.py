import pytest
from unittest.mock import patch, MagicMock
from cbar_currency_rates import rates


@pytest.fixture
def mock_response():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = """<ValCurs Date="27.05.2024" Name="AZN məzənnələri" Description="Azərbaycan Respublikası Mərkəzi Bankının 27.05.2024 tarixdən etibarən xarici valyutaların və bank metallarının Azərbaycan manatına qarşı rəsmi məzənnələri bülleteni">
        <ValType Type="Bank metalları">
        </ValType>
        <ValType Type="Xarici valyutalar">
            <Valute Code="USD">
                <Nominal>1</Nominal>
                <Name>1 ABŞ dolları</Name>
                <Value>1.7</Value>
            </Valute>
            <Valute Code="EUR">
                <Nominal>1</Nominal>
                <Name>1 Avro</Name>
                <Value>1.8442</Value>
            </Valute>
        </ValType>
        </ValCurs>"""
    return mock_response


@patch('cbar_currency_rates.rates.requests.get')
def test_get_rates(mock_get, mock_response):
    mock_get.return_value = mock_response

    # Instantiate CBARRates object
    cbar = rates.CBARRates()

    # Test get_rates method
    result = cbar.get_rates()

    # Assertions
    assert mock_get.called
    assert result == {'USD': 1.7, 'EUR': 1.8442}
