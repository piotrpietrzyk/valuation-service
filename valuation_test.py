import pytest
import os
from valuation import valuation
import pandas as pd

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


@pytest.mark.parametrize("matching_id",
                         (1, 2, 3))
def test_sort_values(val, matching_id):
    val.converse_currency()
    val.total_price()
    val.sort_values()
    values_list = []
    assert pd.Index(val.data['matching_id']).is_monotonic_decreasing
    for index, row in val.data.iterrows():
        if row['matching_id'] == matching_id:
            values_list.append(row['total_price'])

    assert values_list == sorted(values_list, reverse=True)


def test_top_product():
    pass
