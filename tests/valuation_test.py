import pytest
from valuation import valuation
import pandas as pd


@pytest.fixture
def val():
    val = valuation.Valuation(f'../data/data.csv', f'../data/currencies.csv', f'../data/matching.csv')
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


@pytest.mark.parametrize("matching_id", (1, 2, 3))
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


@pytest.mark.parametrize("column", ("matching_id", "total_price", "avg_price", "currency", "ignored_products_count"))
def test_top_product(val, column):
    val.converse_currency()
    val.total_price()
    val.sort_values()
    val.top_product()
    assert not val.top_products.isnull().values.any()
    assert column in val.top_products.columns


def test_save_csv(val, tmpdir):
    val.converse_currency()
    val.total_price()
    val.sort_values()
    val.top_product()
    temp_file = tmpdir.join('test.csv')
    val.save_csv(temp_file)
    read_temp_file = pd.read_csv(temp_file)
    pd.testing.assert_frame_equal(val.top_products.reset_index(drop=True), read_temp_file.reset_index(drop=True))

