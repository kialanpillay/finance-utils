from forex_python.converter import CurrencyRates, CurrencyCodes
import sys
import math

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def main():
    r = CurrencyRates()
    c = CurrencyCodes()
    transaction_amount = float(sys.argv[1])
    base_currency = 'ZAR'
    quote_currency = 'ZAR'
    if len(sys.argv) >= 3:
        base_currency = sys.argv[2]
    if len(sys.argv) == 4:
        quote_currency = sys.argv[3]
    converted_amount = r.convert(base_currency, quote_currency, transaction_amount)
    fees = converted_amount * 0.02
    print('Transaction Amount', c.get_symbol(quote_currency), '{:.2f}'.format(converted_amount))
    print('Transaction Fees  ', c.get_symbol(quote_currency), truncate(fees, 2))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 fees.py [transaction_amount] <base_currency> <quote_currency>')
    else:
        main()
