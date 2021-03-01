from flask import flash
import yfinance as yf
from urllib.error import HTTPError, URLError
from app.services.user_svc import UserService

class TickerService:
    
    def ticker_data(symbols):
        print('Fetching ticker data...')

        if symbols == None:
            return None

        ticker_data = []
        for s in symbols:
            s = s.upper()
            # Check for symbols short enough to exist
            if(len(s) <= 5):
                try:
                    # Try to retrieve ticker data
                    ticker = yf.Ticker(s)
                    name = ticker.info['shortName']
                    current_price = ticker.info['bid']
                    high = ticker.info['regularMarketDayHigh']
                    low = ticker.info['regularMarketDayLow']
                    open = ticker.info['open']
                    close = ticker.info['previousClose']
                except (KeyError, ImportError, HTTPError, URLError) as e:
                    # Print the problem ticker to console and delete it from the user's followed tickers
                    flash(f'Ticker {s} is not a valid entry. ', 'alert')
                    UserService.delete_ticker(UserService.get_symbols(), s.lower())
                    ticker = None
                    pass
                
                # If the ticker was found, finish getting the data
                if ticker:
                    stock_data = {}
                    stock_data['symbol'] = s
                    stock_data['name'] = name
                    stock_data['current_price'] = current_price
                    stock_data['high'] = high
                    stock_data['low'] = low
                    stock_data['open'] = open
                    stock_data['close'] = close
                    ticker_data.append(stock_data)

            else:
                # Ticker is too long to exist and will be deleted
                flash(f'Ticker symbol {s} was too long.', 'alert')
                UserService.delete_ticker(UserService.get_symbols(), s.lower())

        return ticker_data