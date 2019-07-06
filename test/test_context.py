#!/usr/bin/env Python
# coding=utf-8

import unittest
import os
import json
import logging


class ContextTest(unittest.TestCase):
    context = {"name": "world"}

    def setUp(self):
        envContext = json.loads(os.environ["MOCHACONTEXT"])
        self.context['name'] = envContext['name']

    def test_sayHello(self):
        logging.info('Hello,' + self.context.get("name"))

    def test_process_context(self):
        logging.info(self.context)

    def test_process_context_name(self):
        assert self.context['name']=='world'


if __name__ == '__main__':
    unittest.main(verbosity=2)
