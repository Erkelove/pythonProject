import unittest


class unite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('测试每个类之前的准备工作')

    def setUp(self) -> None:
        print('测试每个用例之前的准备工作')

    def tearDown(self) -> None:
        print('测试每个用例之后的收尾工作')

    @classmethod
    def tearDownClass(cls) -> None:
        print('测试每个类之后的收尾工作')