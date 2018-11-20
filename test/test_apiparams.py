# -*- coding:utf-8 -*-

import unittest
import requests
from parameterized import parameterized

data = {
    "adtag": "newtab",
    "size": "10",
    "guid": "0e5b2e73aabfedbbf2a21e83cb4bafb9",
    "channel": "98",
    "page": "1",
    "qbShowDocList": [],
    "t": "1514388731574"
}
proxies = {
    # "http": "http://127.0.0.1:8888",
    # "https": "http://127.0.0.1:8888",
}


class TestParameterized(unittest.TestCase):
    @parameterized.expand(data.keys())
    def test_null(self, name):
        newData = data.copy()
        newData[name] = None
        r = requests.get(
            "http://recommend.browser.qq.com/feeds/getRecommendList",
            params=newData,
            proxies=proxies)
        assert r.status_code == 200

    @parameterized.expand(data.keys())
    def test_length(self, name):
        newData = data.copy()
        newData[name] = "长度超过50个字符的字符串：欢迎各位学习mocha，mocha真的很好用。This is just a test 0e5b2e73aabfedbbf2a21e83cb4bafb9：字段长度检查(假设每个字段参数长度不超过50个字符)"
        r = requests.get(
            "http://recommend.browser.qq.com/feeds/getRecommendList",
            params=newData,
            proxies=proxies)
        assert r.status_code == 200


if __name__ == '__main__':
    unittest.main(verbosity=2)
