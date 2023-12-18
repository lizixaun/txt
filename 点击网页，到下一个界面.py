import requests  # 导入requests库，用于发送HTTP请求
from bs4 import BeautifulSoup  # 从bs4库中导入BeautifulSoup类，用于解析HTML内容
import re  # 导入re库，用于正则表达式匹配

base_url = 'https://www.fangpi.net/s/%E5%91%A8%E6%9D%B0%E4%BC%A6'  # 定义目标网页链接

response = requests.get(base_url)  # 发送GET请求到目标链接，并将响应存储在response变量中

if response.status_code == 200:  # 检查响应的状态码是否为200（成功）
    soup = BeautifulSoup(response.text, 'html.parser')  # 使用BeautifulSoup解析HTML内容
    # 查找所有带有特定链接格式的<a>标签
    links = soup.find_all('a', href=re.compile('/music/\d+'))

    for link in links:  # 遍历找到的链接
        music_link = link['href']  # 获取链接地址
        target_url = f'{base_url}{music_link}'  # 构建完整的链接地址

        link_response = requests.get(target_url)  # 访问链接

        if link_response.status_code == 200:  # 检查访问链接的响应状态码是否成功
            print(f'成功访问链接：{target_url}')  # 打印成功信息
        else:
            print(f'无法访问链接：{target_url}')  # 打印失败信息
else:
    print("页面请求失败")  # 若初始请求失败（状态码非200），则打印出"页面请求失败"
