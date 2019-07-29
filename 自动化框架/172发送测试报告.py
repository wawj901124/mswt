import unittest
import time
from 自动化框架.HTMLTestRunner import HTMLTestRunner
from 自动化框架.SendReport import send_mail

class MyTestCase(unittest.TestCase):

    #每条用例初始化
    def setUp(self):
        self.initdata  = "hello imooc"

    #测试用例，以test开头
    def test_something(self):
        self.assertEqual("hello imooc", self.initdata)

    #每条用例执行完后释放资源
    def tearDown(self):
        pass

if __name__ == "__main__":
    #声明一个suite
    suite = unittest.TestSuite()

    #从类加载用例集
    cases = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

    #添加用例到suite
    suite.addTests(cases)

    # #声明TestRunner
    # myTestRunner = unittest.TextTestRunner(verbosity=2)

    #生成HTML TestReport
    #以时间戳来定义报告名称
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    HtmlFile = "report/" + now + "_Reprt.html"
    fp = open(HtmlFile, "wb")
    myTestRunner = HTMLTestRunner(
        stream=fp,
        title=u"测试报告",
        description= u"用例测试情况"
    )

    #执行Runner
    myTestRunner.run(suite)
    fp.close()

    #发送测试报告
    send_mail(["xiangkaizheng@iapppay.com"],"TestResult",HtmlFile)
