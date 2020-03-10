import pandas as pd
from alpha_vantage.timeseries import TimeSeries  # Alpha_vantage_wrapper

API_KEY = 'JB22OYP6YRBZYY99'


def getStockdata(symbol):
    try:
        print("Please wait while I look for your data request :) \n")
        timeS = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = timeS.get_intraday(symbol=symbol, interval='1min')

        return str(data.tail(1).iloc[0]['4. close'])

    except:
        return "not found"


def main():
    f = open('japi.out', 'w')
    while 1:
        user_input = input("Type the stock symbol name to get the most recent price: \n").upper()
        if user_input != "QUIT":
            response = 'The current price of {} is {}\n'.format(user_input, getStockdata(user_input))
            print(response)
            f.write(response)
            print("Stock Quotes retrieved successfully!")
        else:
            raise SystemExit


main()
