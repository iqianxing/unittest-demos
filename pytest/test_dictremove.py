#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Filename : test_dictremove.py
#Author : qianxing
'测试dict remove'
import pytest

urls = ["www.qq.com","http://www.jd.com","http://www.baidu.com"]
def test_remove():
  'list remove test'
  for url in urls:
    if not url.startswith("http://"):
      urls.remove(url)
  assert urls ==  ["http://www.jd.com","http://www.baidu.com"]

def test_dict_remove():
  'dictionary remove test'
  data = {
    "qq":"www.qq.com",
    "jd":"http://www.jd.com",
    "baidu":"http://wwww.baidu.com"
  }
  for key in data:
    print key,data[key]
    del data[key]

def test_dict_remove_by_keys():
  'dictionary remove test'
  data = {
    "qq":"www.qq.com",
    "jd":"http://www.jd.com",
    "baidu":"http://wwww.baidu.com"
  }
  for key in data.keys():
    print key,data[key]
    del data[key]