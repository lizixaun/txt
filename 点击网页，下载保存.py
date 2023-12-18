# 导入所需的库
import requests  # 用于发送HTTP请求
from bs4 import BeautifulSoup  # 用于解析HTML内容
import re  # 用于正则表达式匹配

# 目标网站的基础URL
base_url = 'https://www.fangpi.net/s/%E5%91%A8%E6%9D%B0%E4%BC%A6'

# 发送GET请求获取页面内容
response = requests.get(base_url)

# 检查页面请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有<a>标签，提取其中的href属性，该属性包含音乐下载链接
    links = soup.find_all('a', href=re.compile('/music/\d+'))

    # 提取链接并逐个下载音乐文件download_link = f'{base_url}{music_link}'：
    # 将 base_url（网站的基础链接）和 music_link（从链接中提取的特定音乐文件的相对链接）
    # 拼接起来，形成完整的下载链接，存储在 download_link 变量中，以便后续用于下载音乐文件。
    for link in links:
        music_link = link['href']
        download_link = f'{base_url}{music_link}'

        #
        # 哦，抱歉，有点混淆了。music_response = requests.get(download_link)
        # 这一行代码实际上是用来发送HTTP GET请求并获取指定链接（download_link）的响应
        # 内容。它并不是直接进行文件下载，而是获取了链接所指向的资源内容。实际的文件下载
        # 发生在之后的部分，通过将获取到的内容写入文件实现。
        music_response = requests.get(download_link)

        # 检查音乐文件下载请求是否成功
        if music_response.status_code == 200:
            # 保存音乐文件，以链接的最后部分命名文件在这段代码中，rsplit('/', 1) 中的 1 表示最大分割次数。这里使用的是 rsplit() 方法，它是 Python 字符串的一个方法，用于从右边开始分割字符串。rsplit('/', 1) 的意思是从右边开始，以 / 作为分隔符，最多只分割一次。
            #
            # 例如，假设 music_link 是一个链接字符串：'https://www.example.com/music/song.mp3'，使用 rsplit('/', 1) 将其按 / 分割，只分割一次，结果会得到一个列表 ['https://www.example.com/music', 'song.mp3']。
            #
            # [-1] 表示从这个分割后的列表中取最后一个元素，也就是 'song.mp3'，这就是所期望的音乐文件名。这种操作对于从链接中提取文件名是很常见的做法，因为最后一个部分通常是文件名或者资源的标识符。
            music_filename = music_link.rsplit('/', 1)[-1]
            with open(f'{music_filename}.mp3', 'wb') as file:
                #所以，这行代码的作用就是将从网络上下载的音乐文件的二进制内容写入到本地文件中。
                file.write(music_response.content)
            print(f'{music_filename} 下载完成')
        else:
            print(f'{music_filename} 下载失败')
else:
    print("页面请求失败")

