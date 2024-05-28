import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

class CBARRates:
    def __init__(self):
        self.base_url = "https://www.cbar.az/currencies/"
        self.xml_url = None

    def get_xml_url(self, date):
        formatted_date = date.strftime("%d.%m.%Y")
        return f"{self.base_url}{formatted_date}.xml"

    def get_rates(self, date=None):
        if date is None:
            date = datetime.now() - timedelta(days=1)  # Default to 1 day before today

        self.xml_url = self.get_xml_url(date)
        response = requests.get(self.xml_url)
        if response.status_code == 200:
            return self.parse_xml(response.content)
        else:
            print(f"Failed to fetch data from {self.xml_url}. Status code: {response.status_code}")
            return None

    def parse_xml(self, xml_data):
        root = ET.fromstring(xml_data)
        currencies = {}
        for valute in root.findall("./ValType[@Type='Xarici valyutalar']/Valute"):
            code = valute.find("CharCode").text
            value = float(valute.find("Value").text)
            currencies[code] = value
        return currencies
