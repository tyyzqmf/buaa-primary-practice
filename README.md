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

### 效果
![wi01](./work01/images/wi01.png)

### 打包成exe

注意：需要在windows环境执行以下命令，在mac打包的产物无法在windows下（跨平台）运行
```
pyinstaller -F work01/main.py
```

![wi02](./work01/images/wi02.png)

## 作业2：语音识别与合成

### 运行
```
python work02/main.py
```

### 效果
1、先根据百度AI平台的APPID、KEY登陆
![wi03](./work02/images/wi03.png)

2、语音识别
![wi04](./work02/images/wi04.png)

3、语音合成
合成后的文件默认在当前目录下的"audio.mp3"

### 打包成exe
同作业1

