import fire
import pandas as pd
from pandas_datareader import data
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def preview_stock(symbol, plot="Volume"):
    """
    Utility function to show the last 1 week of stock performance
    for any stock. Optionally plot the historical performance
    with a line chart. 
    """
    source = "yahoo"
    today = pd.Timestamp.today()
    start_date = today - pd.Timedelta(365, unit="d")
    end_date = today
    stock = data.DataReader(symbol, source, start_date, end_date)
    print(stock.tail(7))
    if plot:
        try:
            stock[plot].plot()
            plt.show(block=True)
        except KeyError:
            return "The value for plot must be one of 'High', 'Low', 'Open', 'Close', 'Volume' or 'Adj Close'"


if __name__ == "__main__":
    fire.Fire(preview_stock)
