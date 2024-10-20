## ttsmaker.cn示例音频数据的提取

从[ttsmaker.cn](https://ttsmaker.cn)中提取一些示例音频数据，用于测试[F5 TTS](https://github.com/SWivid/F5-TTS)的声音克隆效果。


### 拉取仓库
```shell
git clone https://github.com/Samge0/ttsmaker-download.git
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
在[config.py](config.py)中配置自己的ChromeDriver路径
```shell
cp config.demo.py config.py
```

### 运行
```shell
python crawler.py
```

或者：
```shell
python crawler.py
```