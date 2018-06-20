from unittest import TestCase

import os, sys

try:
    from query_morningstar import QueryKeyRatios
except ImportError:
    insert_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(insert_dir)
    sys.path.insert(0, insert_dir)
    from query_morningstar import QueryKeyRatios

class TestQueryKeyRatios(TestCase):
    def test_query_key_ratios(self):
        key_ratios = QueryKeyRatios.query_key_ratios("TSLA")
        self.assertIsNotNone(key_ratios)
