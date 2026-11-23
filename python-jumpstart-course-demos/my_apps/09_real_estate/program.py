from data_types import Purchase

import csv
import os
# import statistics


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_header():
    clear_screen()
    print('-----------------------------')
    print(' REAL ESTATE DATA MINING APP ')
    print('-----------------------------\n')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')
    data = load_file(filename)
    query_data(data)


def load_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader =  csv.DictReader(fin)
        purchases = []
        for row in reader:
            # print(f'Bed count: {row['beds']}\n\n {row}\n')
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


# Refizemos esta função como uma função lambda de apenas uma linha
# def get_price(el):
#     return el.price


def query_data(data: list[Purchase]):
    # If data was sorted by price:
    data.sort(key=lambda p: p.price)

    # Least expensive house?
    high_purchase = data[-1]
    print(f'The most expensive house is $ {high_purchase.price:,.2f}')

    # Most expensive hose?
    low_purchase = data[0]
    print(f'The least expensive house is $ {low_purchase.price:,.2f}')

    # Average price house?
    prices = [pur.price for pur in data]

    ave_price = 0
    for price in prices:
        ave_price+=price
    ave_price = ave_price / len(prices)

    two_bedroom = [pur for pur in data if pur.beds == 2]
    len_two_bedroom = len(two_bedroom)

    ave_price_two_bedroom = sum((p.price for p in two_bedroom)) / len_two_bedroom
    ave_baths_two_bedroom = sum((p.baths for p in two_bedroom)) / len_two_bedroom
    ave_sqft_two_bedroom = sum((p.sq__ft for p in two_bedroom)) / len_two_bedroom

    # Python has a module called statistics that extract mean too
    # ave_price = statistics.mean(prices)

    print(f'The average home price is: ${ave_price:,.2f}')
    print(f'The average home price 2 bedrooms is: ${ave_price_two_bedroom:,.2f}')
    print(f'The average home baths for 2 bedrooms is: {round(ave_baths_two_bedroom, 1)}')
    print(f'The average home sqft for 2 bedrooms is: {round(ave_sqft_two_bedroom, 1)}')
    print()


def main():
    print_header()
    get_data_file()


if __name__ ==  '__main__':
    main()
