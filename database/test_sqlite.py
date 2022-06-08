import unittest
import sqlite3
from dataminer.miner import Miner
from database.sqlite import Storage

class MyTestCase(unittest.TestCase):
    def test_create_table_if_not_exists(self):
        db = sqlite3.connect('test.db')
        Storage('test.db').create_table_if_not_exists()
        db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='quotes'")
        self.assertGreater(db.cursor().fetchone()[0],0)

    def test_delete_table(self):
        db = sqlite3.connect('test.db')
        Storage('test.db').delete_table()
        db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='quotes'")
        self.assertEqual(db.cursor().fetchone()[0], 0)

    def test_data_has_been_inserted(self):
        db = sqlite3.connect('test.db')
        Storage('test.db').truncate()
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
