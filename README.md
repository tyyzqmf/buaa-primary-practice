# buaa-primary-practice

北航一级工程实践作业

## 依赖包安装
```
pip install -r requirements.txt -i https://pypi.douban.com/simple
```

## 作业1：计算器

### 运行
```
python work01/main.py
```

![](work01/images/wi01.png)

### 打包成exe

注意：需要在windows环境执行以下命令，在mac打包的产物无法在windows下（跨平台）运行
```
pyinstaller -F work01/main.py
```

![](work01/images/wi02.png)