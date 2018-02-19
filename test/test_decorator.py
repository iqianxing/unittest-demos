#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Filename : test_decorator.py
#Author : qianxing
'test decorator'
import unittest
from time import ctime,sleep

def tsfunc(func):
  def wrappedFunc():
    print '[%s] %s() called' % (ctime(), func.__name__)
    return func()
  
  return wrappedFunc

@tsfunc
def foo():
  pass

class TestDecorator(unittest.TestCase):
  def test_foo(self):
    foo()
    sleep(4)
    for i in range(2):
      sleep(1)
      foo()

if __name__ == '__main__':
  unittest.main()