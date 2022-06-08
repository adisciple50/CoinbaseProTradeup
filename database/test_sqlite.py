import unittest
import sqlite3
from dataminer.miner import Miner
from database.sqlite import Storage

class MyTestCase(unittest.TestCase):
    def test_data_has_been_inserted(self):
        db = sqlite3.connect('test.db')
        Storage('test.db').bulk_insert(Miner().parse_quotes_for_database())
        quotes = db.execute('SELECT * FROM quotes')
        self.assertGreater(len(quotes),0)

    def test_data_has_been_truncated(self):
        Storage('test.db').bulk_insert(Miner().parse_quotes_for_database())
        Storage('test.db').truncate()
        db = sqlite3.connect('test.db')
        quotes = db.execute('SELECT * FROM quotes')
        self.assertGreater(len(quotes), 0)

if __name__ == '__main__':
    unittest.main()
