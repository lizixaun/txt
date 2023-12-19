import requests
from bs4 import BeautifulSoup
import re
import os

base_url = 'http://www.m326.com/so.php?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'

response = requests.get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=re.compile(r'/sing/\w+\.html'), target='_mp3')

    for link in links:
        music_link = link['href']
        title = link.get('title')
        target_url = 'http://www.m326.com' + music_link

        print(target_url)
        responses = requests.get(target_url)

        if responses.status_code == 200:
            soups = BeautifulSoup(responses.text, 'html.parser')
            linksssss = soups.find_all('a', href=re.compile(r'.+\.mp3$'))

            save_path = r'C:\Users\李子煊\Desktop\zjl'

            for link in linksssss:
                music_linksss = link['href']
                music_responses = requests.get(music_linksss)

                if music_responses.status_code == 200:
                    filename = os.path.join(save_path, os.path.basename(music_linksss))

                    with open(filename, 'wb') as file:
                        file.write(music_responses.content)
                        print(f'{filename} 下载完成')
                else:
                    print(f'{music_linksss} 下载失败')

        else:
            print("页面请求失败")
else:
    print("页面请求失败")
