from transformers import xLSTMConfig, xLSTMModel
import torch.nn as nn
import get_data

# Initializing a xLSTM configuration
configuration = xLSTMConfig(
    hidden_size=64,  # Embedding dim for sequence features
    num_layers=1,     # Number of xLSTM blocks
    num_attention_heads=1,  # For parallel processing
    intermediate_size=128,  # Feedforward dim
    vocab_size=1,     # Set to 1 for regression (or larger for tokenized data)
    use_cache=True,   # For efficient inference
)


class stock_forecaster(nn.Module):
    def __init__(self):
        self.model = xLSTMModel(configuration)

    def get_data(ticker:str, start_date:str, end_date:str):
        stock_df = get_data.download_stock(ticker, start_date, end_date)
        close_df = stock_df['close']
        print(close_df.head(n=10)) 

    
stock_forecaster = stock_forecaster()
stock_forecaster.get_data('NVDA', '2015-01-01', '2025-08-01')
