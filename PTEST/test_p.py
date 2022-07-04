import pytest

#scope是使用范围，autouse是表示是否自动使用，默认是false





class TestP():

    # def setup_class(cls) -> None:
    #     print('测试每个类之前的准备工作')
    #
    # def setup(self) -> None:
    #     print('测试每个用例之前的准备工作')


    #@pytest.mark.skip
    def test01(self):
        print('测试知了')
        #assert 1 == 2

    #age = 18
    #@pytest.mark.skipif(age>16, reason = '微微已经16周岁，跳过')
    #@pytest.mark.smoke
    #@pytest.mark.run(order=1)
    def test02(self):
        print("测试微微")
        #assert 1 == 2

    #@pytest.mark.username#指定执行pytest.ini配置文件中markers标记的用例
    #@pytest.mark.run(order=2)
    def test03(self):
        print("测试百里")

    # def teardown(self) -> None:
    #     print('测试每个用例之后的收尾工作')
    #
    #
    # def teardown_class(cls) -> None:
    #      print('测试每个类之后的收尾工作')