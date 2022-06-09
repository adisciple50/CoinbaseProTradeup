from cbpro import PublicClient
from product import Quote
import itertools

class Miner:
    def __init__(self):
        self.client = PublicClient()
        # self.quotes = self.load_quotes()
        # currency id tree serves as an index tree to the rates tree
        self.currency_id_tree = self.construct_currency_tree()
        self.rates_tree = {}

    def split_product_id(self, product:str) -> list:
        product_array = product.split('-')
        return product_array

    def load_quote(self,product:str) -> Quote:
        product_array = self.split_product_id(product)
        return Quote(product_array[0],product_array[0])

    def load_quotes(self) -> list:
        quotes = []
        for quote in self.client.get_products():
            quotes += Quote(self.split_product_id(quote))
        return quotes

    def construct_currency_tree(self) -> list:
        mapped_currencies = []
        for currency in self.client.get_currencies():
            if currency['convertible_to'] != []:
                mapped_currencies.append({currency['id']: currency['convertible_to']})
        return mapped_currencies

    def deconstruct_currency_tree(self,tree):
        for node in tree:
            for exchange in node:
                for coin in node[exchange]:
                    yield ['GBP', exchange, coin, 'GBP']

    def parse_quotes_for_database(self) -> list:
        quotes = []
        for chain in self.deconstruct_currency_tree(self.currency_id_tree):
            initial = Quote(chain[0], chain[1])
            exchange1 = initial.get_sell_price()
            exchange2 = Quote(chain[1],chain[2]).get_sell_price()
            exchange3 = Quote(chain[2],chain[3]).get_sell_price()
            product = exchange1 * exchange2 * exchange3
            profit = product - initial.investment_quote()
            quotes.append(('GBP',exchange1,chain[1],exchange2,chain[2],exchange3,'GBP',profit))
        return quotes


