import yfinance as yf
import pandas as pd


def download_stock(ticker, start_date, end_date) -> pd.DataFrame:
    """
    Download individual stock data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)

    stock_df = pd.DataFrame(data=data)

    # Save to CSV
    stock_df.to_csv(f"{ticker}_historical_data.csv")
    print(stock_df.tail(n=10))
    return stock_df


def download_fund(ticker, start_date, end_date) -> pd.DataFrame:
    """
    Download index fund data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)

    fund_df = pd.DataFrame(data=data)

    # Save to CSV
    fund_df.to_csv(f"{ticker}_historical_data.csv")
    print(fund_df.tail(n=10))
    return fund_df


def download_crypto(ticker, start_date, end_date) -> pd.DataFrame:
    """
    Download crypto data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)

    crypto_df = pd.DataFrame(data=data)

    # Save to CSV
    crypto_df.to_csv(f"{ticker}_historical_data.csv")
    print(crypto_df.tail(n=10))
    return crypto_df

# denoise and remove NULL values
def preprocess():
    pass

# stock ticker symbols
nvda_ticker = "NVDA"
googl_ticker = "GOOGL"
meta_ticker = "META"

# index fund ticker ssymbols
spy_ticker = "SPY"
qqq_ticker = "QQQ"
dia_ticker = "DIA"

# crypto ticker symbols
btc_ticker = "BTC"
eth_ticker = "ETH"
sol_ticker = "SOL"

#download_stock(ticker=nvda_ticker, start_date="2015-01-01", end_date="2025-08-01")
#download_fund(ticker=spy_ticker, start_date="2015-01-01", end_date="2025-08-01")