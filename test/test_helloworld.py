import unittest
class TestHelloWorld(unittest.TestCase):
    def test_hello(self):
        assert 'hello'

    def test_world(self):
        assert 'world'

if __name__ == '__main__':
  unittest.main()