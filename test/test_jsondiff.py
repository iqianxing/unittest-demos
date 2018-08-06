import unittest
import json

class TestDictCompare(unittest.TestCase):
    def test_jsondiff_same(self):
      self.maxDiff=None
      oldJson = json.loads('{"title":"com.tencent.news","fullTitle":"Androbugs report com.tencent.news","timedOut":false,"duration":0,"state":"passed","speed":"fast","pass":true,"fail":false,"pending":false}')
      newJson = json.loads('{"title":"com.tencent.news","fullTitle":"Androbugs report com.tencent.news","timedOut":false,"duration":0,"state":"passed","speed":"fast","pass":true,"fail":false,"pending":false}')
      self.assertDictEqual(oldJson,newJson)

    def test_jsondiff_different(self):
      self.maxDiff=None
      oldJson = json.loads('{"title":"com.tencent.news","fullTitle":"Androbugs report com.tencent.news","timedOut":false,"duration":0,"state":"passed","speed":"fast","pass":true,"fail":false,"pending":false}')
      newJson = json.loads('{"title":"com.tencent.news2","fullTitle":"Androbugs report com.tencent.news","timedOut":false,"duration":0,"state":"passed","speed":"fast","pass":true,"fail":false,"pending":false}')
      self.assertDictEqual(oldJson,newJson)



if __name__ == '__main__':
  unittest.main()