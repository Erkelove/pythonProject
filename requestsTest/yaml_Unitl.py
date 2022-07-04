import os

import yaml

import csv

#读取yaml文件
def read_yaml(key):
    with open(os.getcwd()+'/extract.yaml', mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value(key)

#写入yaml文件
def write_yaml(data):
    with open(os.getcwd()+'/extract.yaml',mode='a',encoding='utf-8') as f:
        yaml.dump(data, stream=f, allow_unicode=True)

#清空
def clear_yaml():
    with open(os.getcwd()+'/extract.yaml',mode='w',encoding='utf-8') as f:
        f.truncate()

#读取测试用例
def read_testcase(yaml_name):
    with open(os.getcwd()+'/'+yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        print(value)
        return value
read_testcase('get_token.yaml')