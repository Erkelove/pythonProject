import os

import pytest
import pytest_html

if __name__ == '__main__':
    #-n=2表示2个线程同时进行测试
    #--reruns=2 表示有失败的用例多执行两次
    #--maxfail=2 表示出现两个用例错误就直接终止测试
    #--html=./report/report.html生成测试报告放入指定文件夹中
    #pytest.main(['-vs', './PTEST', '-n=2', '--reruns=2', '--maxfail=2'])
    #pytest.main(['-vs', './PTEST', '--html=./report/report.html'])
    pytest.main()
    #执行系统命令，生成allure报告
    #os.system('allure generate ./temp -o ./report --clean')
