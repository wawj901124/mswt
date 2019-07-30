import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):
    @ddt.data("App专项测试","自动化","Python")
    def testGet(self,queryword):
        #header 部分的配置
        header_data= {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36',
            'Host': 'm.imooc.com',
            'Referer': 'https://m.imooc.com/',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        #cookies部分的配置
        cookies_data = dict(imooc_uuid='ce990a6b-e1cf-45db-96d3-9749ee068bc0',
                            imooc_isnew_ct= '1562835480',
                            imooc_isnew= '2',
                            page= 'https://m.imooc.com/')

        #get请求的构造
        res = requests.get("https://m.imooc.com/search/?words="+queryword,
                           headers= header_data,
                           cookies = cookies_data)
        print(res.text)
        self.assertTrue(u"共找到" in res.text)

if __name__ =="__main__":
    unittest.main()