import numpy as np
import pandas as pd

from model_stock_data import StockDataSet


class EvaluationCalculator(object):

    def __init__(self, stock_symbols):
        self.stock_symbols = stock_symbols

    def __load_pred(self, stock_symbol):
        return np.loadtxt("data/" + stock_symbol + "_pred.txt", delimiter=',')

    def calculate_evaluation_quantity(self, top_num, with_hedging=True):

        pred_res, truth_res = {}, {}
        stock_data = StockDataSet("^GSPC", input_size=1, num_steps=30, test_ratio=0.05)
        sp500 = stock_data.test_y

        for stock_symbol in self.stock_symbols:
            pred_res[stock_symbol] = self.__load_pred(stock_symbol)

            stock_data = StockDataSet(stock_symbol, input_size=1, num_steps=30, test_ratio=0.05)
            truth_res[stock_symbol] = stock_data.test_y

        roi = 1.0
        rt_list = []
        for i in range(len(pred_res['AAPL'])):
            d = {}
            for k, v in pred_res.items():
                d[k] = v[i]
            sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
            new_roi = 0.0
            for j in range(top_num):
                key = sorted_d[j][0]
                new_roi += roi / top_num * (1.0 + truth_res[key][j])
            if with_hedging:
                new_roi -= sp500[i]
            rt_list.append(new_roi / roi - 1.0)
            roi = new_roi
            print("echo %d : %f" % (i, roi))

        df = pd.DataFrame()
        df['rt'] = rt_list
        sharpe_ratio = df['rt'].mean() / df['rt'].std()

        return roi - 1.0, sharpe_ratio


if __name__ == '__main__':
    eva_cal = EvaluationCalculator(['AAPL', 'GE', 'GM', 'GOOG', 'JPM', 'KORS', 'MAR', 'MCD', 'MMM', 'TSLA'])
    ret, sharpe = eva_cal.calculate_evaluation_quantity(5, with_hedging=True)
    print("roi = %f, sharpe_ratio = %f" % (ret, sharpe))
