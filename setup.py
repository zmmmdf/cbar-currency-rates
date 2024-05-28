from setuptools import setup, find_packages

setup(
    name='cbar-currency-rates',
    version='1.1.0',
    description='A Python library for fetching currency rates from the Central Bank of Azerbaijan Republic (CBAR) XML file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zmmmdf/cbar-currency-rates',
    author='Ziya Mammadov',
    author_email='ziyamm08@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    py_modules=['cbar_currency_rates.rates'],
    install_requires=[
        'requests',
        'xmltodict',
    ],
    python_requires='>=3.6',
)
