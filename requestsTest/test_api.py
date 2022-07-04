import pytest
import requests

from requestsTest.yaml_Unitl import read_testcase


class TestRequest():

    #get请求，获取接口统一鉴权码token接口
    #@pytest.mark.parametrize('args_name', read_testcase('get_token.yaml'))
    def test_get_token(self, args_name):
        #print(args_name)
        url = args_name['request']['url'] #'http://api.wpbom.com/api/daygas.php'
        data = args_name['request']['data']
        method=args_name['request']['method']
        #res = requests.get(url=url, params=data)
        res = requests.request(method=method, url=url, params=data)
        #返回数据如果是text格式，需要使用text方法来获取返回数据并打印
        print(res.text)
        print(res.status_code)
if __name__ == '__main__':
    TestRequest().test_get_token()
