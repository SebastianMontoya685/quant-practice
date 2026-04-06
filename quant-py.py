import numpy as np
import pandas as pd

rng = np.random.default_rng(42);

n = 500;

# Calculating the daily log returns in decimal form.
daily_returns = rng.normal(loc=0.002, scale=0.01, size=n);

# Calculating the true dollar-value equity curve:
equity = 100 * np.exp(np.cumsum(daily_returns));

idx = pd.date_range("2020-01-05", periods=n, freq="B");
ret = pd.Series(daily_returns, index=idx, name="returns");

vol_20d = ret.rolling(20).std() * np.sqrt(252);

print(ret.describe());
print(round(equity[-1], 4));
print(round(vol_20d.iloc[-1], 4));

