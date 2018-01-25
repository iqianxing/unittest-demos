import unittest
import requests


class TestHttpbin(unittest.TestCase):
    def test_get(self):
        r = requests.get('https://api.github.com/events')
        assert r.status_code == 200

    def test_put(self):
        r = requests.put('http://httpbin.org/put', data={'key': 'value'})
        assert r.status_code == 200

    def test_delete(self):
        r = requests.delete('http://httpbin.org/delete')
        assert r.status_code == 200

    def test_head(self):
        r = requests.head('http://httpbin.org/get')
        assert r.status_code == 200

    def test_options(self):
        r = requests.options('http://httpbin.org/get')
        assert r.status_code == 200


if __name__ == '__main__':
    unittest.main()