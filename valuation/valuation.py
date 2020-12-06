import pandas as pd
import numpy as np


class Valuation(object):
    def __init__(self, data, currencies, matchings):

        self.data = pd.read_csv(data)
        self.currencies = pd.read_csv(currencies)
        self.matchings = pd.read_csv(matchings)
        self.top_products = pd.DataFrame()

    def converse_currency(self):
        for index, row in self.data.iterrows():
            if row['currency'] != 'PLN':
                self.data['price'][index] = row['price'] * self.currencies['ratio'].loc[self.currencies['currency'] == row['currency']]
                self.data['currency'].loc[index] = 'PLN'

