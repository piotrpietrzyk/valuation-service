import pytest
import os
from valuation import valuation

cwd = os.getcwd()


@pytest.fixture
def val():
    val = valuation.Valuation(f'{cwd}/data/data.csv', f'{cwd}/data/currencies.csv', f'{cwd}/data/matching.csv')
    return val


def test_valuation_initialization(val):
    assert val


def test_converse_currency(val):
    val.converse_currency()
    for index, row in val.data.iterrows():
        assert row['currency'] == 'PLN'


def test_total_price(val):
    val.converse_currency()
    val.total_price()
    for index, row in val.data.iterrows():
        assert row['total_price'] == row['price'] * row['quantity']



