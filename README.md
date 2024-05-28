# cbar-currency-rates

A Python library for fetching currency rates from the Central Bank of Azerbaijan Republic (CBAR) XML file.

## Installation

You can install the package via pip:

```py
pip install cbar-currency-rates

Usage

python

from cbar_currency_rates import rates

# Instantiate CBARRates object
cbar = rates.CBARRates()

# Get currency rates
rates = cbar.get_rates()

# Print currency rates
for code, value in rates.items():
    print(code, "-", value)
```
License

This project is licensed under the MIT License - see the LICENSE file for details.
