# Quantop
Problem: How to predict the hedge ratio for a stock in a medium time period (longer than one month and shorter than one year)?

Solution: 
The Quantop will apply multiple Machine Learning and statistical models (including linear regression, RNN with LSTM cells and ARIMA) to predict the optimal hedge ratio of a stock based on both the share prices data and the financial statistics. The Quantop will also introduce RESTful APIs for automated trades.

Claim1: The strategy using the optimal hedge ratio can achieve a higher yearly rate of return than traditional strategies.
Claim2: The strategy using the optimal hedge ratio can achieve a lower maximum drawdown than traditional strategies.
Claim3: The Quantop can offer RESTful APIs for automated trades.

+ Train a model only on GOOG.csv
```
python3 stock_prediction.py --stock_symbol=GOOG --train=True --input_size=1 --lstm_size=128 --max_epoch=50
```
+ Load a model trained by GOOG.csv
```
python3 stock_prediction.py --stock_symbol=GOOG --train=False --input_size=1 --lstm_size=128 --max_epoch=50
```
+ Calculate the ROI and sharpe ratio of the portfolio
```
python3 model_evaluation.py --with_hedging=True --top_num=5
```