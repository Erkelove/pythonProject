from HTMLTestRunner import HTMLTestRunner
import os
import unittest
import time

if __name__ == '__main__':
    #TestSuite是unittest的套件，可以将所有用例放入该套件内
    suite = unittest.TestSuite()
    #defaultTestLoader是unittest默认的测试加载器，加载指定目录下的所有用例
    testcase = unittest.defaultTestLoader.discover(os.getcwd(), pattern='U01.py')
    suite.addTests(testcase)
    # verbosity=0表示测试只展示结果，1表示测试结果前面会有.E,F,S,2表示测试结果有详细信息，会显示哪个模块哪个类的用例
    #TextTestRunner是unittest的文本运行器，将套件运行起来执行所有用例
    unittest.TextTestRunner(verbosity=2).run(suite)
    # nowtime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    # filename = open(os.getcwd()+"/"+nowtime+"_report.html", "wb")
    # runner = HTMLTestRunner(stream=filename, verbosity=2, title='测试报告', description='输入输出的测试')
    # runner.run(suite)