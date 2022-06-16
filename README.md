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

## 作业3：自然语言处理演示

### 运行
```
python work03/main.py
```

### 效果
1、先根据百度AI平台的APPID、KEY登陆
![wi03](./work02/images/wi03.png)

2、自然语言处理演示
![wi04](./work03/images/wi05.png)

### 打包成exe
同作业1

## 作业4：人脸识别演示

### 运行
```
python work04/main.py
```

### 效果
人脸识别演示
![wi06](./work04/images/wi06.png)

### 打包成exe
同作业1

## 作业5：文字识别演示

### 运行
```
python work05/main.py
```

### 效果
人脸识别演示
![wi07](./work05/images/wi07.png)

### 打包成exe
同作业1


## 作业6：图片识别演示

### 运行
```
python work06/main.py
```

### 效果
人脸识别演示
![wi08](./work06/images/wi08.png)

### 打包成exe
同作业1

