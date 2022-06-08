from cbpro import PublicClient
from .product import Quote
import itertools

class Miner:
    def __init__(self):
        self.client = PublicClient()
        self.quotes = self.load_quotes()
        # currency id tree serves as an index tree to the rates tree
        self.currency_id_tree = {}
        self.rates_tree = {}

    def split_product_id(self, product:str):
        product_array = product.split('-')
        return product_array

    def load_quote(self,product:str) -> Quote:
        product_array = self.split_product_id(product)
        return Quote(product_array[0],product_array[0])

    def load_quotes(self) -> list:
        quotes = []
        for quote in self.client.get_products():
            quotes += Quote(self.split_product_id(quote))


    def construct_tradeup_sequence(self) -> list:
        for quote in self.quotes:


    def parse_quotes_for_database(self) -> list:
        pass

