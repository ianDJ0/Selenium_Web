import unittest

class SignupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is Login TESTS CASES------------------------------------")

    def test_Signup(self):
        print("Simple signup")
        self.assertTrue(True)


    def test_AdvancedSignup(self):
        print("advanced signup")
        self.assertTrue(True)


    def test_ExtraSignup(self):
        print("extra signup")
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
