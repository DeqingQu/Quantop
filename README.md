# Quantop
Problem: How to predict the hedge ratio for a stock in a medium term (longer than one month and shorter than one year)?

Solution: 
The Quantop will apply multiple Machine Learning and statistical models (including linear regression, RNN with LSTM cells and ARIMA) to predict the optimal hedge ratio of a stock based on both the share prices data and the financial statistics. The Quantop will also introduce RESTful APIs for automated trades.

Claim1: The strategy using the optimal hedge ratio can achieve a higher yearly rate of return than traditional strategies.
Claim2: The strategy using the optimal hedge ratio can achieve a lower maximum drawdown than traditional strategies.
Claim3: The Quantop can offer RESTful APIs for automated trades.

Related works:
1. Lilian's model only applied the share prices to predict prices. https://lilianweng.github.io/lil-log/2017/07/08/predict-stock-prices-using-RNN-part-1.html
2. Facebook Prophet.  https://research.fb.com/prophet-forecasting-at-scale/
3. (TBD)
