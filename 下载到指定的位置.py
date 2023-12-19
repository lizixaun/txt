import os
import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://www.fangpi.net/s/%E5%91%A8%E6%9D%B0%E4%BC%A6'

response = requests.get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=re.compile('/music/\d+'))

    save_folder = r'C:\Users\李子煊\Desktop\test'  # 目标文件夹路径

    for link in links:
        music_link = link['href']
        target_url = f'{base_url}{music_link}'

        link_response = requests.get(target_url)

        if link_response.status_code == 200:
            music_filename = music_link.rsplit('/', 1)[-1]
            file_path = os.path.join(save_folder, f'{music_filename}.mp3')  # 完整文件路径

            with open(file_path, 'wb') as file:
                file.write(link_response.content)
            print(f'{music_filename} 下载完成，保存在 {file_path}')
        else:
            print(f'{music_filename} 下载失败')
else:
    print("页面请求失败")
