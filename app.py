# coding=utf-8
import unittest
import os, time
import re
import pytest

from flask import Flask, render_template
from flask import request, make_response, url_for, redirect

app = Flask(__name__)


@app.route("/")
def index():
    case_path = os.path.join(os.path.dirname(__file__), "test")
    tests = [
        re.match('test_(\w+)\.py', test).group(1)
        for test in os.listdir(case_path) if test.endswith('.py') == True
    ]
    pytest_case_path = os.path.join(os.path.dirname(__file__), "pytest")
    pytests = [
        re.match('test_(\w+)\.py', test).group(1)
        for test in os.listdir(pytest_case_path)
        if test.endswith('.py') == True
    ]
    report_path = os.path.join(os.path.dirname(__file__), "static")
    reports = [
        report for report in os.listdir(report_path)
        if report.endswith('.html') == True
    ]

    return render_template("index.html", tests=tests, pytests=pytests, reports=reports)


@app.route('/test/<name>')
def test(name=None):
    reportname = 'report_{name}_{time}.html'.format(
        name=name, time=time.time())
    testname = "test_" + name + ".py"
    pytest.main([
        '-x', 'test{sep}{testname}'.format(sep=os.sep, testname=testname),
        '--html=static{sep}{report}'.format(sep=os.sep, report=reportname)
    ])
    return redirect('/static/{report}'.format(report=reportname))


@app.route('/pytest/<name>')
def runpytest(name=None):
    reportname = 'report_{name}_{time}.html'.format(
        name=name, time=time.time())
    testname = "test_" + name + ".py"
    pytest.main([
        '-x', 'pytest{sep}{testname}'.format(sep=os.sep, testname=testname),
        '--html=static{sep}{report}'.format(sep=os.sep, report=reportname)
    ])
    return redirect('/static/{report}'.format(report=reportname))


@app.route("/about")
def about():
    return 'The about page'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False, threaded=True)
