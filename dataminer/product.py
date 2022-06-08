from cbpro import PublicClient




class Quote:
    def __init__(self,currency_from:str,currency_to:str,amount:float = 1.0):
        self.client = PublicClient()
        self.product_id = currency_from + '-' + currency_to
        self.data = self.client.get_product_ticker(product_id=self.product_id)
        self.amount = amount
        self.currency_from = currency_from
        self.currency_to = currency_to


    def get_buy_price(self) -> float:
        return self.get_ask()

    def get_amount(self) -> float:
        return float(self.amount)

    def get_ask(self) -> float:
        try:
            return float(self.data['ask'])
        except AttributeError:
            return 0.0  # will bring the whole chain down to 0 profit if not found - here be bug potential!
        except KeyError:
            return 0.0

    def get_bid(self) -> float:
        try:
            return float(self.data['ask'])
        except AttributeError:
            return 0  # will bring the whole chain down to 0 profit if not found - here be bug potential!
        except KeyError:
            return 0.0

    def to_gbp(self) -> float:
        try:
            return self.get_bid() * (1/(Quote(self.currency_to,'GBP').get_buy_price()))
        except ZeroDivisionError:
            return 0.0

    def investment_quote(self):
        return float(Quote(self.currency_from,'GBP' ).get_buy_price())

    def get_sell_price(self):
        return 1/self.get_bid()


