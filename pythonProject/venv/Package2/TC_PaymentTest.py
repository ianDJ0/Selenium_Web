import unittest

class PaymentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is Payment TESTS CASES------------------------------------")

    def test_Payment(self):
        print("Simple Payment")
        self.assertTrue(True)

    def test_AdvancedPayment(self):
        print("advanced Payment")
        self.assertTrue(True)


    def test_ExtraPayment(self):
        print("extra Payment")
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
