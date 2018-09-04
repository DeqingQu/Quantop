import numpy as np
import os
import random


class roi_calculator(object):

    def __init__(self, stock_symbols):
        self.stock_symbols = stock_symbols

    def load_pred(self, stock_symbol):
        return np.loadtxt("data/" + stock_symbol + "_pred.txt", delimiter=',')

    def calculate_ROI(self):
        for stock_symbol in self.stock_symbols:
            print(stock_symbol)
            pred = self.load_pred(stock_symbol)
            print(pred)

if __name__ == '__main__':
    roi_cal = roi_calculator(['GOOG'])
    roi_cal.calculate_ROI()