# coding=utf-8
import json
import unittest

class jsonTestCase(unittest.TestCase):

    def test_jsontest(self):
        jstr='''{
            "code": 200,
            "description": "执行成功!",
            "model": {
                "success": "0",
                "orderLogList": [{
                    "beforeStatus": "xx",
                    "dealDescrip": "xx",
                    "nowStatus": "xx",
                    "dealDate": "yy"
                }]
            },
            "metadata": {
                "type": 0,
                "clazz": "cn.com.hd.mall.web.webservices.entity.response.order.OrderLogResponse"
            }
        }'''

        dic = json.loads(jstr,"utf-8")

        self.assertEqual(dic["model"]["orderLogList"][0]["dealDate"],"yx")
        print dic["model"]["orderLogList"][0]["dealDate"]

if __name__ == "__main__":
    unittest.main()
