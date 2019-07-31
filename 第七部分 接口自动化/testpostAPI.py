import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):
    @ddt.data(
        ("15977778888","9999"),
        ("15977778889", "9998")
    )
    @ddt.unpack
    # @unittest.skip("testPost*")
    def testPost(self,username_data,password_data):
        formdata = {
            "phone":username_data,
            "code":password_data,
            "remember":"0",
            "referer": "https://m.imooc.com",
            "auto_register":"1"
        }
        #headers 部分的配置
        headers_data = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36',
            'Host': 'm.imooc.com'
        }

        #cookies部分的配置
        cookies_data = dict(imooc_uuid='ce990a6b-e1cf-45db-96d3-9749ee068bc0',
                            imooc_isnew_ct= '1562835480',
                            imooc_isnew= '2',
                            page= 'https://m.imooc.com/')

        res = requests.post("https://m.imooc.com/passport/user/phonelogin",
                            data = formdata,
                            headers= headers_data,
                            cookies = cookies_data
                            )

        print(res.json())


    @ddt.data(
        ("15977778888","123456"),
        ("15977778889", "123455")
    )
    @ddt.unpack
    def testLoginPost(self,username_data,password_data):
        formdata = {
            "username":username_data,
            "password":password_data,
            "verify":"",
            "pwencode": "1",
            "referer": "https://m.imooc.com"
        }
        #headers 部分的配置
        headers_data = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36',
            'Host': 'm.imooc.com'
        }

        #cookies部分的配置
        cookies_data = dict(imooc_uuid='ce990a6b-e1cf-45db-96d3-9749ee068bc0',
                            imooc_isnew_ct= '1562835480',
                            imooc_isnew= '2',
                            page= 'https://m.imooc.com/')

        res = requests.post("https://m.imooc.com/passport/user/login",
                            data = formdata,
                            headers= headers_data,
                            cookies = cookies_data
                            )
        print(res.text)
        print(res.json())





