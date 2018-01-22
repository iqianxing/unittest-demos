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