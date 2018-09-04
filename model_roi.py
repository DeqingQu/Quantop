import numpy as np
import os
import random

from model_stock_data import StockDataSet


class ROICalculator(object):

    def __init__(self, stock_symbols):
        self.stock_symbols = stock_symbols

    def __load_pred(self, stock_symbol):
        return np.loadtxt("data/" + stock_symbol + "_pred.txt", delimiter=',')

    def calculate_roi(self):
        for stock_symbol in self.stock_symbols:
            print(stock_symbol)
            pred = self.__load_pred(stock_symbol)
            print(pred)

            stock_data = StockDataSet(stock_symbol, input_size=1, num_steps=30, test_ratio=0.05)
            print(stock_data.test_y)


if __name__ == '__main__':
    roi_cal = ROICalculator(['GOOG'])
    roi_cal.calculate_roi()