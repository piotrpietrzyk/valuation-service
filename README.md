# Valuation-service

## Description

Read the input data. From products with particular matching_id take those with the highest total price (price * quantity), limit data set by top_priced_count and aggregate prices.

Application requires version of Python 3.7 or higher.

#### Input

In the input there are three files containing:
    
 • _data/data.csv_ - product representation with price,currency,quantity,matching_id
 
 • _data/currencies.csv_ - currency code and ratio to PLN, ie. GBP,2.4 can be converted to PLN as follows 1 PLN * 2.4
 
 • _data/matching.csv_ - matching data matching_id,top_priced_count

#### Output

Saving the results to the  _data/top_products.csv_ . 

## Usage

0. Activate virtual environment:

        virtualenv venv
        source venv/bin/activate

1. Install requirements:

        pip install -r requirements.txt

2. Run application:

        python app.py -c data/currencies.csv -d data/data.csv -m data/matching.csv

## Testing

0. Run tests:

        cd tests
        pytest valuation_test.py

1. Run tests with coverage and reporting:

        cd tests
        pytest --cov valuation --cov-report annotate
        