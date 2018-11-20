# -*- coding:utf-8 -*-
import unittest
import requests
from parameterized import parameterized, param
diffApis = [
    # diff apis
    {
        "oldapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v1/demo",
        "newapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v2/demo"
    },
    {
        "oldapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v1/hello",
        "newapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v2/hello"
    },
    {
        "oldapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v1/user",
        "newapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v2/user"
    },
    {
        "oldapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v1/1/list",
        "newapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v2/1/list"
    },
    {
        "oldapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v1/2/list",
        "newapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v2/2/list"
    },
    {
        "oldapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v1/3/list",
        "newapi":"https://easy-mock.com/mock/5b6b06f9a40bfb27425bbb6a/jsondiff/v2/3/list"
    },
]


class BatchDiffTest(unittest.TestCase):
    @parameterized.expand(
        [param("diff test",kv) for kv in diffApis])
    def test_batchdiff(self, _, kv):
        self.maxDiff = None
        oldRes = requests.get(kv["oldapi"])
        newRes = requests.get(kv["newapi"])
        self.assertDictEqual(oldRes.json(), newRes.json())


if __name__ == '__main__':
    unittest.main(verbosity=2)
