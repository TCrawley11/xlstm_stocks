import yfinance as yf

# Define the ticker symbol
ticker_symbol = "NVDA"

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical market data
historical_data = ticker.history(period="1y")  # data for the last year
print("Historical Data:")
print(historical_data)

# Fetch basic financials
financials = ticker.financials
print("\nFinancials:")
print(financials)

# Fetch stock actions like dividends and splits
actions = ticker.actions
print("\nStock Actions:")
print(actions)

def download(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)

    # Save to CSV
    data.to_csv(f"{ticker}_historical_data.csv")
    print(data.head())

# denoise and remove NULL values
def preprocess():
    pass

download(ticker=ticker, start_date="2020-01-01", end_date="2025-08-31")