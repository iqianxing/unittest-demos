# coding=utf-8
import unittest
import os, time
import pytest

from flask import Flask, render_template
from flask import request, make_response, url_for, redirect

app = Flask(__name__, static_folder='static', static_url_path='/public')


@app.route("/")
def index():
    case_path = os.path.join(os.path.dirname(__file__), "test")
    tests = [ test for test in os.listdir(case_path) if test.endswith('.py')==True]
    pytest_case_path = os.path.join(os.path.dirname(__file__), "pytest")
    pytests = [ test for test in os.listdir(pytest_case_path) if test.endswith('.py')==True]
    return render_template("index.html",tests = tests, pytests= pytests)


@app.route('/test/<name>')
def test(name=None):
    reportfile = 'py_report_%s.html' % time.time()
    pytest.main(
        ['-x',
         'test/%s' % name,
         '--html=static\%s' % reportfile])
    return redirect('/public/%s' % reportfile)

@app.route('/pytest/<name>')
def runpytest(name=None):
    reportfile = 'py_report_%s.html' % time.time()
    pytest.main(
        ['-x',
         'pytest/%s' % name,
         '--html=static\%s' % reportfile])
    return redirect('/public/%s' % reportfile)


@app.route("/about")
def about():
    return 'The about page'


if __name__ == "__main__":
    app.run()