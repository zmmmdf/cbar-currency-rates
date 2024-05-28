import pytest
from cbar_currency_rates.rates import CBARRates
from datetime import datetime

# Fixture to create a CBARRates object
@pytest.fixture
def cbar_rates():
    return CBARRates()

# Test for the get_rates method
def test_get_rates(cbar_rates):
    # Call the get_rates method without specifying a date
    rates = cbar_rates.get_rates()

    # Check if the returned rates dictionary is not empty
    assert rates

# Test for the parse_xml method
def test_parse_xml():
    # Sample XML data
    xml_data = """
    <ValCurs Date="27.05.2024" Name="AZN məzənnələri" Description="Azərbaycan Respublikası Mərkəzi Bankının 27.05.2024 tarixdən etibarən xarici valyutaların və bank metallarının Azərbaycan manatına qarşı rəsmi məzənnələri bülleteni">
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
    </ValCurs>
    """

    # Call the parse_xml method with the sample XML data
    cbar_rates = CBARRates()
    parsed_rates = cbar_rates.parse_xml(xml_data)

    # Check if the parsed rates dictionary contains the expected values
    assert parsed_rates == {"USD": 1.7, "EUR": 1.8442}

# Test for the get_xml_url method
def test_get_xml_url(cbar_rates):
    # Create a date object for testing
    test_date = datetime(2024, 5, 27)

    # Call the get_xml_url method with the test date
    xml_url = cbar_rates.get_xml_url(test_date)

    # Check if the generated XML URL matches the expected format
    assert xml_url == "https://www.cbar.az/currencies/27.05.2024.xml"
