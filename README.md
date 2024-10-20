## ttsmaker.cn示例音频数据的提取

从[ttsmaker.cn](https://ttsmaker.cn)中提取一些示例音频数据，用于测试[F5 TTS](https://github.com/SWivid/F5-TTS)的声音克隆效果。

[点击去下载已保存的示例音频（results.zip）>>](https://github.com/Samge0/ttsmaker-download/releases/tag/v0.0.1)


### 拉取仓库
```shell
git clone https://github.com/Samge0/ttsmaker-download.git
```

### 进入项目
```shell
cd ttsmaker-download
```

### 创建环境
```shell
conda create -n ttsmaker-download python=3.10.13 -y
```

### 激活环境
```shell
conda activate ttsmaker-download
```

### 安装依赖包
```shell
pip install -r requirements.txt
``` 

### 配置ChromeDriver路径
复制[config.demo.py](config.demo.py)为`config.py`，并在`config.py`中配置自己的ChromeDriver路径
```shell
cp config.demo.py config.py
```

### 运行
```shell
python crawler.py
```

或者：
```shell
python crawler_js.py
```

### 相关截图
![image](https://github.com/user-attachments/assets/eb69f721-55ee-48ab-935d-2a276f4570ce)

![image](https://github.com/user-attachments/assets/63e3d28b-b19a-4adc-b8bd-43e11fd863ac)

