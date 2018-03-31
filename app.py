# coding=utf-8
import unittest
import os, time
import pytest

from flask import Flask, render_template
from flask import request, make_response, url_for, redirect

app = Flask(__name__, static_folder='static', static_url_path='/public')


@app.route("/")
def index():
    return 'Hello, world!'


@app.route('/test/<name>')
def test(name=None):
    case_path = os.path.join(os.path.dirname(__file__), "test")
    discover = unittest.defaultTestLoader.discover(
        case_path, pattern=('test_%s.py' % name), top_level_dir=None)
    print discover
    runner = unittest.TextTestRunner()
    result = runner.run(discover)

    #生成测试报告
    print "testsRun:%s" % result.testsRun
    print "failures:%s" % len(result.failures)
    print "errors:%s" % len(result.errors)
    print "skipped:%s" % len(result.skipped)

    data = {
        "name": name,
        "testsRun": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "skipped": len(result.skipped),
    }
    return render_template('test.html', data=data)


@app.route('/pytest/<name>')
def runpytest(name=None):
    reportfile = 'py_report_%s.html' % time.time()
    pytest.main(
        ['-x',
         'pytest/test_%s.py' % name,
         '--html=static\%s' % reportfile])
    return redirect('/public/%s' % reportfile)


@app.route("/about")
def about():
    return 'The about page'


if __name__ == "__main__":
    app.run()