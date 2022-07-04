import pytest


@pytest.fixture(scope='function', autouse=True, params='aaa')
def my_fixture(request):
    print('这是前置方法')
    yield request.param #return和yeild都表示返回的意思，但是return后面不能有代码，而yield后面可以跟代码
    print('这是后置方法')
