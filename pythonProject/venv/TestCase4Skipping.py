import unittest


class searchEngineTest(unittest.TestCase):

    def test_search(self):
        print(f"This is simple search")

    @unittest.SkipTest
    def test_advancedSearch(self):
        print(f"This is advanced search")

    # @unittest.skip("Not done")
    @unittest.skipIf(0 == 0, "Zero is equal to zero")
    def test_imageSearch(self):
        print(f"This is image Search")


if __name__ == '__main__':
    unittest.main()
