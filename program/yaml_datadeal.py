#读取yaml文件
import os

import yaml

import csv


def read_yaml(yaml_name):
    with open(os.getcwd()+'/'+yaml_name, mode='r', encoding='utf-8') as f:
        value =yaml.load(stream=f, Loader=yaml.FullLoader)
        print(value)
        return(value)
read_yaml('get_data.yaml')