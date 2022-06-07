import unittest
from dataminer.product import Quote


class MyTestCase(unittest.TestCase):
    def test_get_bid(self):
        # returns float
        quote = Quote('BTC','GBP').get_bid()
        self.assertGreater(quote,1,"quote was not greater than one for BTC-GBP. Price was: " + float(quote))
        self.assertIsInstance(quote,float)

    def test_get_ask(self):
        # returns float
        quote = Quote('BTC','GBP').get_ask()
        self.assertGreater(quote, 1, "quote was not greater than one for BTC-GBP. Price was: " + float(quote))
        self.assertIsInstance(quote, float)

    def test_get_ask(self):
        # returns float
        quote = Quote('BTC','GBP').get_ask()
        self.assertGreater(quote, 1, "quote was not greater than one for BTC-GBP. Price was: " + float(quote))
        self.assertIsInstance(quote, float)

    def test_buy_price(self):
        # returns float
        quote = Quote('BTC','GBP').get_buy_price()
        self.assertGreater(quote, 1, "quote was not greater than one for BTC-GBP. Price was: " + float(quote))
        self.assertIsInstance(quote, float)

    def test_get_sell_price(self):
        # returns float
        quote = Quote('BTC','GBP').get_sell_price()
        self.assertLess(quote, 1, "quote was not less than one for BTC-GBP. Price was: " + float(quote))
        self.assertIsInstance(quote, float)

    def test_to_gbp(self):
        # this gets the gbp worth of the trade by getting the amount recieved
        # (Quote(currency to trade,currency recieved and to then be converted to GBP)
        # and then converting it to gbp
        # returns float
        quote = Quote('BTC', 'GBP').to_gbp()
        self.assertGreater(quote, 1, "quote was not more than one for BTC-GBP. Price was: " + float(quote))
        self.assertIsInstance(quote, float)

    def test_investment_quote(self):
        #       this is how much it costs to buy the first currency in a currency pair. returns float in GBP
        quote = Quote('BTC', 'GBP').to_gbp()
        self.assertGreater(quote, 1, "result was not more than one for BTC-GBP. Price was: " + float(quote))
        self.assertIsInstance(quote, float)

if __name__ == '__main__':
    unittest.main()
