#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-10-18 17:38
# describe：抓取ttsmaker.cn的演示音频-通过解析渲染后的页面标签获取

import json
import os
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin
from urllib.request import urlretrieve
import config

# 保存目录
OUTPUT_DIR = ".cache/output"


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

    # 获取渲染后的页面源代码
    html_content = driver.page_source
    driver.quit()

    audio_list = []  # 初始化列表来存储音频信息

    # 使用Scrapy解析HTML
    selector = scrapy.Selector(text=html_content)
    audio_links = selector.css('a')
    for link in audio_links:
        href = link.css('::attr(example-mp3-url)').get() or ''
        if href.endswith('.mp3') or href.endswith('.wav'):
            full_url = urljoin(url, href)
            title = (link.xpath('parent::*/preceding-sibling::span[1]/text()').get() or href.split('/')[-1].split('.')[0]).strip()
            file_name = f"{title.replace(' ', '').replace('/', '_')}{os.path.splitext(href)[-1]}"
            file_path = os.path.join(OUTPUT_DIR, file_name)

            # 下载并保存音频文件
            urlretrieve(full_url, file_path)
            print(f"Downloaded {file_name} to {OUTPUT_DIR}")
            
            # 添加到列表
            audio_list.append({'title': title, 'url': full_url})

    # 保存列表为JSON文件
    with open(f'{OUTPUT_DIR}/tts.json', 'w', encoding='utf-8') as f:
        json.dump(audio_list, f, ensure_ascii=False, indent=4)

    print("All audio files have been downloaded and saved to music.json")


if __name__ == "__main__":
    download_audio_files('https://ttsmaker.cn/')
    print("Done!")