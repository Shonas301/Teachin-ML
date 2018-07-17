from alpha_vantage.timeseries import TimeSeries
import configparser
from pprint import pprint

class SaveData():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        if 'AlphaVantage' in config:
            self.key = config['AlphaVantage']['key']
        else:
            raise FileNotFoundError('Config file contining Alpha Vantage key not found')

    def scrapeTicker(self, ticker, scope=0):
        """Function which calls the Alpha Vantage api wrapper and saves it

        The function calls the api is called with the specific ticker given and
        the scope given as an integer and it proceeds to save it to a csv given
        that the api returns a pandas dataframe. The data is saved as a csv
        under $ticker.csv. 

        Args: 
            self: The SaveData object
            ticker (str): The ticker tag which specifies the stock intended.
            scope (int, optional): The timeframe under which we want the ticker
                data.
                0 = daily
                1 = weekly
                2 = monthly 
        Returns:
            None.
        """
        ts = TimeSeries(key=self.key, output_format='pandas')
        if scope > 2 or scope < 0:
            raise ValueError('Scope is not within valid range, check documentation')
        data, meta_data = {
                0: ts.get_daily,
                1: ts.get_weekly,
                2: ts.get_monthly
                }[scope](symbol=ticker, outputsize='full')
        file_name = ticker+'.csv'
        data.to_csv(file_name)

