import numpy as np
import os
import pandas as pd
import random
import time


class StockData(object):
    def __init__(self,
                 stock_symbol,
                 input_size=3,
                 num_steps=2,
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
        self.train_x, self.train_y, self.test_x, self.test_y = self.__prepare_data(self.raw_seq[:15])

    def __prepare_data(self, seq):
        seq = [np.array(seq[i*self.input_size:(i+1)*self.input_size]) for i in range(len(seq) // self.input_size)]

        if self.normalized:
            seq = [seq[0] / seq[0][0] - 1.0] + [curr / seq[i][-1] - 1.0 for i, curr in enumerate(seq[1:])]

        # split into groups of num_steps
        x = np.array([seq[i: i + self.num_steps] for i in range(len(seq) - self.num_steps)])
        y = np.array([seq[i + self.num_steps] for i in range(len(seq) - self.num_steps)])

        train_size = int(len(x) * (1.0 - self.test_ratio))
        train_x, test_x = x[:train_size], x[train_size:]
        train_y, test_y = y[:train_size], y[train_size:]
        return train_x, train_y, test_x, test_y

    def generate_one_epoch(self, batch_size):
        num_batches = int(len(self.train_x)) // batch_size
        if batch_size * num_batches < len(self.train_x):
            num_batches += 1

        batch_indices = range(num_batches)
        random.shuffle(batch_indices)
        for j in batch_indices:
            batch_x = self.train_x[j * batch_size: (j + 1) * batch_size]
            batch_y = self.train_y[j * batch_size: (j + 1) * batch_size]
            assert set(map(len, batch_x)) == {self.num_steps}
            yield batch_x, batch_y


if __name__ == '__main__':
    sd = StockData("^GSPC")
    # print(sd.generate_one_epoch())
    print(sd.train_x)
    print(sd.train_y)
    print(sd.test_x)
    print(sd.test_y)
