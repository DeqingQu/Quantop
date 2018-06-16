# Quantop
Problem: How to predict the high and low share price of a company in a period (longer than one month and shorter than one year)?

Solution: The QuantaTop builds a recurrent neural network with LSTM cells to predict the high and low price of a company based on both the share prices data and the financial statistics. The QuantaTop will also introduce RESTful APIs for automated trades.

Claim1: The QuantaTop can achieve higher accuracy than other algorithms.
Claim2: The QuantaTop can beat the index and achieve higher returns.
Claim3: The QuantaTop can offer RESTful APIs for automated trades.

Related works:
1. Lilian's model only applied the share prices to predict prices. https://lilianweng.github.io/lil-log/2017/07/08/predict-stock-prices-using-RNN-part-1.html
2. Facebook Prophet.  https://research.fb.com/prophet-forecasting-at-scale/
3. ...

Other possible improvements:
1. combining different algorithms to the system (ARIMA model ...)
2. choosing different parameters to get the best performance
