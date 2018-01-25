# 环境
python 2.7
# 安装依赖包
```
pip install -r requirements.txt
```
# 生成requirements.txt
python项目中必须包含一个 requirements.txt 文件，用于记录所有依赖包及其精确的版本号。以便新环境部署。
```
pip freeze >requirements.txt
```

# 运行测试用例
1. python运行unittest测试用例
``` python case\test_requests.py ```
2. pytest
``` pytest ```

# pytest
1. Detailed info on failing assert statements (no need to remember self.assert* names);
2. Auto-discovery of test modules and functions;
3. Modular fixtures for managing small or parametrized long-lived test resources;
4. Can run unittest (including trial) and nose test suites out of the box;
5. Python 2.7, Python 3.4+, PyPy 2.3, Jython 2.5 (untested);
6. Rich plugin architecture, with over 315+ external plugins and thriving community;