import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://www.fangpi.net/s/%E5%91%A8%E6%9D%B0%E4%BC%A6'

response = requests.get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # 找到所有<a>标签，提取其中的href属性，该属性包含音乐下载链接
    links = soup.find_all('a', href=re.compile('/music/\d+'))

    # 提取链接并逐个下载音乐文件
    for link in links:
        music_link = link['href']
        download_link = f'{base_url}{music_link}'

        # 下载音乐文件
        music_response = requests.get(download_link)

        if music_response.status_code == 200:
            # 保存音乐文件，以链接的最后部分命名文件
            music_filename = music_link.rsplit('/', 1)[-1]
            with open(f'{music_filename}.mp3', 'wb') as file:
                file.write(music_response.content)
            print(f'{music_filename} 下载完成')
        else:
            print(f'{music_filename} 下载失败')
else:
    print("页面请求失败")
