import os

import pytest
import requests
import selenium

#接口自动化
from program.yaml_datadeal import read_yaml


class Test_request():
    #将读取的yaml文件的参数传入到datas中
    @pytest.mark.parametrize('datas', read_yaml('get_data.yaml'))
    def test01_tianqi(self, datas, my_function_fixture):
        print(datas+'----------')
        method = datas['request']['method']
        url = datas['request']['url']
        data = datas['request']['data']
        res = requests.request(method=method, url=url, data=data)
        print(res.text)
