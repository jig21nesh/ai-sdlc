import unittest
from invoices import get_invoice

class InvoiceTests(unittest.TestCase):
    def test_owner(self):
        record={'id':'i1','account':'a1','amount':10}
        self.assertIs(get_invoice([record], 'i1', 'a1'), record)

    def test_other_account_cannot_receive_invoice(self):
        record={'id':'i1','account':'a1','amount':10}
        self.assertIsNone(get_invoice([record], 'i1', 'a2'))

    def test_missing_invoice(self):
        record={'id':'i1','account':'a1','amount':10}
        self.assertIsNone(get_invoice([record], 'missing', 'a1'))

    def test_empty_invoices(self):
        self.assertIsNone(get_invoice([], 'i1', 'a1'))

if __name__ == '__main__':
    unittest.main()
