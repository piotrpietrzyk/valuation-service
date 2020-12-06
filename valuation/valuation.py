import pandas as pd
import numpy as np


class Valuation(object):
    def __init__(self, data, currencies, matchings):

        self.data = pd.read_csv(data)
        self.currencies = pd.read_csv(currencies)
        self.matchings = pd.read_csv(matchings)
        self.top_products = pd.DataFrame()

