import numpy as np
import os
import pandas as pd
import random
import time


class StockData(object):
    def __init__(self,
                 stock_symbol,
                 input_size=1,
                 num_steps=30,
                 test_ratio=0.1,
                 normalized=True,
                 ):
        self.stock_symbol = stock_symbol
        self.input_size = input_size
        self.num_steps = num_steps
        self.test_ratio = test_ratio
        self.normalized = normalized

        #   read csv file
        raw_df = pd.read_csv(os.path.join("../data", "%s.csv" % stock_symbol))

        #   merge data into one sequence
        self.raw_seq = raw_df['Close'].tolist()

        self.raw_seq = np.array(self.raw_seq)
        # self.train_X, self.train_y, self.test_X, self.test_y = self._prepare_data(self.raw_seq)

    def generate_one_epoch(self):
        return self.raw_seq[:10]


if __name__ == '__main__':
    sd = StockData("^GSPC")
    print(sd.generate_one_epoch())