#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Filename : test_list.py
#Author : qianxing
'测试list分片'

import unittest

data = [1, 2, 3, 4, 5, 6, 7]


class TestList(unittest.TestCase):
    'List 测试类'

    def test_in(self):
        'in'
        assert 2 in data

    def test_not_in(self):
        'not in'
        assert 'a' not in data

    def test_add(self):
        '+'
        print data + data
        assert data + data == [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]

    def test_repeat(self):
        '*'
        print data * 2
        assert data * 2 == [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]

    def test_aspect(self):
        '[]'
        print data[0]
        self.assertEqual(data[0], 1)

        '[:] 不包括结束索引对应的元素'
        print data[0:3]
        self.assertSequenceEqual(data[0:3], [1, 2, 3])

        '[::]'
        print data[0:5:2]
        self.assertSequenceEqual(data[0:5:2], [1, 3, 5])

        '[::-1]'
        print data[::-1]
        assert data[::-1] == [7, 6, 5, 4, 3, 2, 1]

    def test_list_comprehension(self):
        '列表解析'
        print [i for i in data if i % 2 == 0]
        assert [i for i in data if i % 2 == 0] == [2, 4, 6]

        print [i**2 for i in range(8)]
        assert [i**2 for i in range(8)] == [0, 1, 4, 9, 16, 25, 36, 49]


if __name__ == '__main__':
    unittest.main()
