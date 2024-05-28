# CBAR Currency Rates

Certainly! Here's the README.md file with the purpose, usage, installation, testing, and contribution guidelines in both Azerbaijani and English:


### Purpose

cbar-currency-rates serves the purpose of providing easy access to currency exchange rates from the Central Bank of Azerbaijan Republic (CBAR) XML file. It enables developers to integrate up-to-date currency rates into their applications, facilitating financial calculations and analysis.

### Installation

You can install cbar-currency-rates via pip:

```bash
pip install cbar-currency-rates
```

### Usage

```python
from cbar_currency_rates import rates

# Instantiate CBARRates object
cbar = rates.CBARRates()

# Get currency rates
rates = cbar.get_rates()

# Print currency rates
for code, value in rates.items():
    print(code, "-", value)
```

### Testing

cbar-currency-rates includes comprehensive test coverage to ensure reliability and accuracy. To run the tests, you can use pytest:

```bash
pip install pytest
pytest
```

### Contribution Guidelines

Contributions to cbar-currency-rates are welcome and encouraged! To contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -am 'Added some feature'`).
4. Push your changes to your branch (`git push origin feature/my-feature`).
5. Submit a pull request with a clear description of your changes.