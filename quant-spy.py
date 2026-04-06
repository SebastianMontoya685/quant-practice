import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Downloading the SPY data:
ticker = "SPY";
raw = yf.download(ticker, start="2020-01-05", end="2024-01-05", auto_adjust=False, progress=False);

adj_close = raw["Adj Close"].squeeze();
adj_close.name = "adj_close";
plt.tight_layout();
adj_close.plot();
plt.show();


