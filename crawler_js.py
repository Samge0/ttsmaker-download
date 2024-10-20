#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-10-18 17:38
# describe：抓取ttsmaker.cn的演示音频-从JavaScript变量中提取音频数据并下载

import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from urllib.request import urlretrieve
import config

# 保存目录
OUTPUT_DIR = ".cache/output2"


def download_audio_files(url):
    # 确保文件夹存在
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 设置Selenium WebDriver
    options = Options()
    service = Service(executable_path=config.CHROMEDRIVER_PATH)  # 指定ChromeDriver路径
    driver = webdriver.Chrome(service=service, options=options)

    # 使用WebDriver打开页面
    driver.get(url)
    driver.implicitly_wait(10)  # 等待JavaScript渲染完成

    # 从页面中提取JavaScript变量
    script_text = driver.execute_script("return JSON.stringify(support_language_data);")
    driver.quit()

    # 解析JSON数据
    audio_data = json.loads(script_text)

    # 保存列表为JSON文件
    with open(f'{OUTPUT_DIR}/tts.json', 'w', encoding='utf-8') as f:
        json.dump(audio_data, f, ensure_ascii=False, indent=4)
        
    # 遍历数据并下载音频文件
    for item in audio_data['zh-cn']:
        mp3_url = item['sample_mp3_url']
        title = item['name'].replace(' ', '').replace('/', '_')
        file_name = f"{title}.mp3"
        file_path = os.path.join(OUTPUT_DIR, file_name)

        # 下载并保存音频文件
        urlretrieve(mp3_url, file_path)
        print(f"Downloaded {file_name} to {OUTPUT_DIR}")


if __name__ == "__main__":
    download_audio_files('https://ttsmaker.cn/')
    print("Done!")