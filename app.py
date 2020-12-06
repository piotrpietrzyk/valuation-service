from valuation import valuation
import os


cwd = os.getcwd()
valuation = valuation.Valuation(cwd+'/data/data.csv', cwd+'/data/currencies.csv', cwd+'/data/matching.csv')
valuation.converse_currency()
valuation.total_price()
valuation.sort_values()

