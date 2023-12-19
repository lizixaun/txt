import requests
import os

url = 'https://sy-sycdn.kuwo.cn/97e1968035ded62173b23574eb8659ea/65813597/resource/n2/70/55/756351052.mp3'
save_path = r'C:\Users\李子煊\Desktop\test'  # 目标文件夹路径

response = requests.get(url)

if response.status_code == 200:  # 确保请求成功
    file_name = os.path.join(save_path, url.split('/')[-1])  # 提取文件名作为保存的文件名
    with open(file_name, 'wb') as file:
        file.write(response.content)  # 写入文件内容到指定路径
    print(f'文件已保存至：{file_name}')  # 打印保存成功信息
else:
    print("无法下载文件")  # 请求失败的情况下打印失败信息
