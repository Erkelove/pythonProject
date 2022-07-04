import pytest
from selenium import webdriver


@pytest.fixture(scope='class', autouse=True)
def my_class_fixture():
    print('，打开日志')
    yield
    print('关闭日志')


@pytest.fixture(scope='function', autouse=True)
def my_function_fixture():
    print('准备好请求数据')
    yield
    print('写入请求数据')
