import unittest

def setUpModule():
    print('Setup Module')
def tearDownModule():
    print('Teardown Module')

class searchEngineTest(unittest.TestCase):

    # Setup and teardown Method : Executed before and after the methods
    @classmethod
    def setUp(self):
        print(f'This is Login')
    @classmethod
    def tearDown(self):
        print(f'This is Teardown-----------------------------')


    # setup and teardown Class : Executed once before and after all methods : Origin and End
    @classmethod
    def setUpClass(cls):
        print(f'Opening Application')
    @classmethod
    def tearDownClass(cls):
        print(f'Closing Application')

    def test_search(self):
        print(f"This is simple search")

    def test_advancedSearch(self):
       print(f"This is advanced search")

    def test_imageSearch(self):
       print(f"This is image Search")


if __name__ == '__main__':
    unittest.main()