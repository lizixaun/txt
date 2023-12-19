import requests
from bs4 import BeautifulSoup
import re

base_url = 'http://www.m326.com/so.php?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'

response = requests.get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # 使用正则表达式找到所有符合条件的链接
    links = soup.find_all('a', href=re.compile(r'/sing/\w+\.html'), target='_mp3')

    for link in links:
        href = link.get('href')  # 获取链接地址
        title = link.get('title')  # 获取链接标题
        print(f'链接：{href}, 标题：{title}')
else:
    print("页面请求失败")
