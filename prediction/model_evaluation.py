import numpy as np
import pandas as pd
import argparse
from distutils.util import strtobool

from model_stock_data import StockDataSet
import matplotlib.pyplot as plt


class EvaluationCalculator(object):

    def __init__(self, stock_symbols):
        self.stock_symbols = stock_symbols

    def __load_pred(self, stock_symbol):
        return np.loadtxt("data/" + stock_symbol + "_pred.txt", delimiter=',')

    def calculate_evaluation_quantity(self, top_num, with_hedging=True):

        print(with_hedging)

        pred_res, truth_res = {}, {}
        stock_data = StockDataSet("^GSPC", input_size=1, num_steps=30, test_ratio=0.05)
        sp500 = stock_data.test_y

        for stock_symbol in self.stock_symbols:
            pred_res[stock_symbol] = self.__load_pred(stock_symbol)

            stock_data = StockDataSet(stock_symbol, input_size=1, num_steps=30, test_ratio=0.05)
            truth_res[stock_symbol] = stock_data.test_y

            # print("-----pred------")
            # print(pred_res)
            # print("-----truth------")
            # print(truth_res)

        roi = 1.0
        hedge_ratio = 1.0
        rt_list = []
        cu_rt_list = []
        for i in range(1, len(pred_res['AAPL'])):
            d = {}
            for k, v in pred_res.items():
                d[k] = v[i] - v[i-1]
            sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
            # print(sorted_d)
            new_return = 0
            new_invest = 0
            for j in range(top_num):
                key = sorted_d[j][0]
                # new_roi += roi / top_num * (1.0 + truth_res[key][j])
                new_return += truth_res[key][i] - truth_res[key][i - 1]
                new_invest += truth_res[key][i]
                print("%s : %f - %f" % (key, truth_res[key][i], truth_res[key][i-1]))
            if with_hedging:
                new_return -= (sp500[i] - sp500[i - 1]) * hedge_ratio
                new_invest += sp500[i] * hedge_ratio
            new_roi = new_return / new_invest
            roi *= new_roi + 1
            rt_list.append(new_roi)
            cu_rt_list.append(sum(rt_list)[0] + 1)
            print("echo %d : %f, cumulated_roi : %f" % (i, new_roi, roi))

        print(cu_rt_list)

        self.plot_samples(cu_rt_list, sp500[:-1]/sp500[0])

        df = pd.DataFrame()
        df['rt'] = rt_list
        sharpe_ratio = df['rt'].mean() / df['rt'].std()

        return sum(rt_list), sharpe_ratio

    def plot_samples(self, roi, sp500):

        days = [i+1 for i in range(len(roi))]

        plt.figure(figsize=(12, 6))
        plt.plot(days, roi, label='ROI')
        plt.plot(days, sp500, label='S\&P500')
        plt.legend(loc='upper left', frameon=False)
        plt.xlabel("day")
        plt.ylabel("ROI")
        plt.ylim(0.8, 1.2)
        plt.grid(ls='--')
        plt.title("ROI of the portfolio")

        plt.savefig("roi.png", format='png', bbox_inches='tight', transparent=True)
        plt.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Evaluate the ROI and sharpe ratio of the portfolio')
    parser.add_argument("--top_num", help="number of stocks selected in the portfolio (default=5)", type=int,
                        default=5)
    parser.add_argument("--with_hedging", help="with hedging or not (default=True)",
                        type=lambda x: bool(strtobool(x)),
                        default=False)
    args = parser.parse_args()

    eva_cal = EvaluationCalculator(['AAPL','AMZN', 'MSFT', 'GE', 'GM', 'GOOG', 'JPM', 'KORS', 'MCD', 'MMM'])
    ret, sharpe = eva_cal.calculate_evaluation_quantity(args.top_num, with_hedging=args.with_hedging)
    print("roi = %f, sharpe_ratio = %f" % (ret, sharpe))
