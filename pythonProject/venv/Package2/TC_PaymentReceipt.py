import unittest

class PaymentReceiptTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is Payment Receipt TESTS CASES------------------------------------")

    def test_Receipt(self):
        print("Receipt printed")
        self.assertTrue(True)

    def test_AdvancedReceipt(self):
        print("Advanced Receipt Printed")
        self.assertTrue(True)


    def test_ExtraReceipt(self):
        print('Extra Receipt Printed')
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
