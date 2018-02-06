#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Filename : test_dictremove.py
#Author : qianxing

'测试list comprehension'
import pytest
import sys

def test_lambda():
  data = map(lambda x:x**2,range(6))
  print data

def test_yeild():
  '生成器表达式-磁盘文件样例'
  data = open("./readme.md")
  sum(len(word) for line in data for word in line.split())

def test_pair():
  '交叉配对样例'
  rows=[1,2,3,4,5]

  def cols():
    'test data'
    yield 'hello,world'
    yield '欢迎你'

  pairs = ((x,y) for x in rows for y in cols())
  print pairs
