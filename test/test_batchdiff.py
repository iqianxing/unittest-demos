# -*- coding:utf-8 -*-

import unittest
import requests
from parameterized import parameterized

diffApis = [
    # diff apis
    {
        "oldapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=16&stattime=1527782400",
        "newapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=16&stattime=1527782400"
    },
    {
        "oldapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=16&stattime=1527782400",
        "newapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=4&stattime=1527782400"
    },
    {
        "oldapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=16&stattime=1527782400",
        "newapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=23&stattime=1527782400"
    },
    {
        "oldapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=16&stattime=1527782400",
        "newapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=12&stattime=1527782400"
    },
    {
        "oldapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=16&stattime=1527782400",
        "newapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=2&stattime=1527782400"
    },
    {
        "oldapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=16&stattime=1527782400",
        "newapi":
        "https://mtj.baidu.com/data/mobile/trend?dimension=brand&platformId=0&rankId=15&stattime=1527782400"
    },
    {
        "oldapi":
        "http://wis.qq.com/weather/common?callback=jQuery111105922904533110209_1533657946519&weather_type=observe%7Cforecast_24h%7Cair&source=pc&province=%E5%8C%97%E4%BA%AC%E5%B8%82&city=%E5%8C%97%E4%BA%AC%E5%B8%82&county=&_=1533657946520",
        "newapi":
        "http://wis.qq.com/weather/common?callback=jQuery111105922904533110209_1533657946519&weather_type=observe%7Cforecast_24h%7Cair&source=pc&province=%E5%8C%97%E4%BA%AC%E5%B8%82&city=%E5%8C%97%E4%BA%AC%E5%B8%82&county=&_=1533657946520"
    },
    {
        "oldapi":
        "http://wis.qq.com/weather/common?source=pc&weather_type=observe|alarm&province=%E5%8C%97%E4%BA%AC%E5%B8%82&city=%E5%8C%97%E4%BA%AC%E5%B8%82&county=&callback=jQuery112008061541882788377_1533657948645&_=1533657948647",
        "newapi":
        "http://wis.qq.com/weather/common?source=pc&weather_type=observe|alarm&province=%E5%8C%97%E4%BA%AC%E5%B8%82&city=%E5%8C%97%E4%BA%AC%E5%B8%82&county=&callback=jQuery112008061541882788377_1533657948645&_=1533657948647"
    }
]


class TestParameterized(unittest.TestCase):
    @parameterized.expand(diffApis)
    def test_length(self, oldapi,newapi):
        oldRes = requests.get(oldapi)
        newRes = requests.get(newapi)
        self.assertDictEqual(oldRes.response,newRes.response)

if __name__ == '__main__':
    unittest.main(verbosity=2)
