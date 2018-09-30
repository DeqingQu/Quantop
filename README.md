# Quantop
Problem: How to predict the stock pricing and generate a portfolio with hedging in a medium time period (longer than one month and shorter than one year)?

Solution: 
The Quantop will apply multiple Machine Learning and statistical models (including linear regression and LSTM networks) to predict the price of stocks and generate portfolios with hedging strategies to achieve higher excess return and lower risk of volatility. The multi-factor model with share prices data and fundamentals data are utilized in generating the portfolio and hedging strategy is used to reduce the beta of the portfolio (which is a measure of systematic risk). The Quantop will also introduce RESTful APIs for automated trades.

Claim1: The portfolio using hedge strategy can achieve higher excess returns than traditional strategies.<br>
Claim2: The portfolio using hedge strategy can achieve lower risk of volatility than traditional strategies.<br>
Claim3: The Quantop can offer RESTful APIs for automated trades. (It will be completed before the end of October)

+ Train a model using RNN on GOOG.csv
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
