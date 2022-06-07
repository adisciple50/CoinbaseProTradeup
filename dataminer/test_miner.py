import unittest
from dataminer.miner import Miner
from dataminer.product import Quote
from cbpro import PublicClient

class MyTestCase(unittest.TestCase):

    def test_load_quote(self):
        self.assertIsInstance(Miner().load_quote('BTC-GBP'),Quote)

    def test_load_quotes(self):
        quotes = Miner().load_quotes()
        self.assertIsInstance(quotes, list)
        self.assertEqual(len(quotes), len(PublicClient.get_products()))

    def test_construct_tradeup_sequence(self):
        sequence = Miner().construct_tradeup_sequence()
        self.assertEqual(len(sequence), 4)
        for item in sequence:
            self.assertIsInstance(item,str)

    def get_tradeup_sequences(self):
        self.assertIsInstance(Miner().get_tradeup_sequence(),list)

    def test_parse_for_database(self):
        self.assertIsInstance(Miner().parse_for_dateabase(), list)
        self.assertIsInstance(Miner().parse_for_dateabase()[0], tuple)


if __name__ == '__main__':
    unittest.main()
