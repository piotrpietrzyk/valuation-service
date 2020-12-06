import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None


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

    def total_price(self):
        self.data['total_price'] = self.data['price'] * self.data['quantity']

    def sort_values(self):
        self.data = self.data.sort_values(by=['matching_id', 'total_price'], ascending=False)

    def top_product(self):
        copy = self.data.copy()
        for index, row in self.matchings.iterrows():
            self.data[self.data['matching_id'] == row['matching_id']] = self.data[self.data['matching_id'] == row[
                'matching_id']].iloc[0:row['top_priced_count']]
        self.data = self.data.dropna()
        self.data = self.data.reset_index()
        self.top_products['total_price'] = self.data.groupby('matching_id')['total_price'].sum()
        self.top_products['avg_price'] = self.data.groupby('matching_id')['total_price'].mean()
        self.top_products['currency'] = self.data['currency']
        self.top_products.insert(loc=0, column='matching_id', value=self.top_products.index)
        self.top_products['ignored_products_count'] = np.nan
        for index, row in self.top_products.iterrows():
            self.top_products['ignored_products_count'].loc[index] = len(
                copy[copy['matching_id'] == row['matching_id']]) - len(
                self.data[self.data['matching_id'] == row['matching_id']])

    def save_csv(self, path):
        self.top_products.to_csv(path, index=False)