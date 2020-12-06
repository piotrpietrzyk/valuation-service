from valuation import valuation
import os
import argparse
cwd = os.getcwd()

parser = argparse.ArgumentParser()
parser.add_argument('--currencies', '-c', type=os.path.abspath, help='path to currencies csv')
parser.add_argument('--data', '-d', type=os.path.abspath, help='path to data csv')
parser.add_argument('--matching', '-m', type=os.path.abspath, help='path to matching csv')
args = parser.parse_args()

if __name__ == '__main__':
    valuation = valuation.Valuation(args.data, args.currencies, args.matching)
    valuation.converse_currency()
    valuation.total_price()
    valuation.sort_values()
    valuation.top_product()
    valuation.save_csv(f'{cwd}/data/top_products.csv')

