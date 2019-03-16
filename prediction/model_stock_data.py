import numpy as np
import os
import pandas as pd
import random
import time

random.seed(time.time())


class StockDataSet(object):
    def __init__(self,
                 stock_sym,
                 input_size=1,
                 num_steps=30,
                 test_ratio=0.1,
                 normalized=False,
                 close_price_only=False):
        self.stock_sym = stock_sym
        self.input_size = input_size
        self.num_steps = num_steps
        self.test_ratio = test_ratio
        self.close_price_only = close_price_only
        self.normalized = normalized

        # Read csv file
        raw_df = pd.read_csv(os.path.join("data", "%s.csv" % stock_sym))

        # Merge into one sequence
        if close_price_only:
            self.raw_seq = raw_df['close'].tolist()
        else:
            self.raw_seq = [price for tup in raw_df[['close', 'open', 'PE', 'PB']].values for price in tup]

        self.raw_seq = np.array(self.raw_seq)
        self.train_X, self.train_y, self.test_X, self.test_y, self.train_y_price, self.test_y_price = self._prepare_data(self.raw_seq)

    def info(self):
        return "StockDataSet [%s] train: %d test: %d" % (
            self.stock_sym, len(self.train_X), len(self.test_y))

    def _prepare_data(self, seq):

        # split into items of input_size
        seq = [np.array(seq[i * self.input_size: (i + 1) * self.input_size])
               for i in range(len(seq) // self.input_size)]

        # original stock price
        ori_price = seq

        if self.normalized:
            seq_np = np.array(seq)
            seq_np = seq_np / seq_np.max(axis=0)
            seq = seq_np.tolist()
            # seq = [seq[0] / seq[0][-1] - 1.0] + [
            #     curr / seq[i][-1] - 1.0 for i, curr in enumerate(seq[1:])]

        # split into groups of num_steps
        X = np.array([seq[i: i + self.num_steps] for i in range(len(seq) - self.num_steps)])
        y = np.array([[seq[i + self.num_steps][0]] for i in range(len(seq) - self.num_steps)])
        y_price = np.array([[ori_price[i + self.num_steps][0]] for i in range(len(ori_price) - self.num_steps)])

        train_size = int(len(X) * (1.0 - self.test_ratio))
        train_X, test_X = X[:train_size], X[train_size:]
        train_y, test_y = y[:train_size], y[train_size:]
        train_y_price, test_y_price = y_price[:train_size], y_price[train_size:]

        # print("train_X")
        # print(train_X[:4])
        # print("train_y")
        # print(train_y[:4])
        # print(train_y_price[:4])

        return train_X, train_y, test_X, test_y, train_y_price, test_y_price

    def generate_one_epoch(self, batch_size):
        num_batches = int(len(self.train_X)) // batch_size
        if batch_size * num_batches < len(self.train_X):
            num_batches += 1

        batch_indices = range(num_batches)
        # random.shuffle(batch_indices)
        for j in batch_indices:
            batch_X = self.train_X[j * batch_size: (j + 1) * batch_size]
            batch_y = self.train_y[j * batch_size: (j + 1) * batch_size]
            assert set(map(len, batch_X)) == {self.num_steps}
            yield batch_X, batch_y


if __name__ == '__main__':
    ss = StockDataSet("AAPL", input_size=3, num_steps=3, test_ratio=0.5)

    for batch_X, batch_y in ss.generate_one_epoch(64):
        print(batch_X)
        print(batch_y)
        break

     # #   test code
     # print(ss.train_y_start)
     # print(ss.test_y_start)
     #
     # print("train: origin y - size :%d" % len(ss.train_y))
     # last_price = ss.train_y_start
     # for y in ss.train_y:
     #     cur_price = (y + 1.0) * last_price
     #     print(cur_price)
     #     last_price = cur_price
     #
     # print("test: origin y - size :%d" % len(ss.test_y))
     # last_price = ss.test_y_start
     # for y in ss.test_y:
     #     cur_price = (y + 1.0) * last_price
     #     print(cur_price)
     #     last_price = cur_price
