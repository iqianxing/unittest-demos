import unittest
import json

class TestDictCompare(unittest.TestCase):
    def test_dictEqual(self):
      oldDict = {
            "title": "com.tencent.news",
            "fullTitle": "Androbugs report com.tencent.news",
            "timedOut": False,
            "duration": 0,
            "state": "passed",
            "speed": "fast",
            "pass": True,
            "fail": False,
            "pending": False,
            "code": "addContext(this, androidbugs.information);\nassert.equal(androidbugs.information.analyze_status, \"success\");",
            "err": {},
            "isRoot": False,
            "uuid": "3c53f17b-c0b6-48c0-ab71-bf782ca5bc9d",
            "isHook": False,
            "skipped": False
          }
      newDict = {
            "title": "com.tencent.news",
            "fullTitle": "Androbugs report com.tencent.news",
            "timedOut": False,
            "duration": 0,
            "state": "passed",
            "speed": "fast",
            "pass": True,
            "fail": False,
            "pending": False,
            "code": "addContext(this, androidbugs.information);\nassert.equal(androidbugs.information.analyze_status, \"success\");",
            "err": {},
            "isRoot": False,
            "uuid": "3c53f17b-c0b6-48c0-ab71-bf782ca5bc9d",
            "isHook": False,
            "skipped": False
          }
      self.assertDictEqual(oldDict,newDict)
    
    def test_dictNotEqual(self):
      self.maxDiff=None
      oldDict = {
            "title": "com.tencent.news",
            "fullTitle": "Androbugs report com.tencent.news",
            "timedOut": False,
            "duration": 0,
            "state": "passed",
            "speed": "fast",
            "pass": True,
            "fail": False,
            "pending": False,
            "code": "addContext(this, androidbugs.information);\nassert.equal(androidbugs.information.analyze_status, \"success\");",
            "err": {},
            "isRoot": False,
            "uuid": "3c53f17b-c0b6-48c0-ab71-bf782ca5bc9d",
            "isHook": False,
            "skipped": False
          }
      newDict = {
            "title": "com.tencent.news",
            "fullTitle": "Androbugs report com.tencent.news2",
            "timedOut": False,
            "duration": 0,
            "state": "passed",
            "speed": "fast",
            "pass": True,
            "fail": False,
            "pending": False,
            "code": "HelloaddContext(this, androidbugs.information);\nassert.equal(androidbugs.information.analyze_status, \"success\");",
            "err": {},
            "isRoot": False,
            "uuid": "3c53f17b-c0b6-48c0-ab71-bf782ca5bc9d",
            "isHook": False,
            "skipped": False
          }
      self.assertDictEqual(oldDict,newDict)


if __name__ == '__main__':
  unittest.main()