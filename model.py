from transformers import xLSTMConfig, xLSTMModel

# Initializing a xLSTM configuration
configuration = xLSTMConfig()

# Initializing a model (with random weights) from the configuration
model = xLSTMModel(configuration)

# Accessing the model configuration
configuration = model.config