import requests
import json
import re
import os
import zipfile

# 项目的目录
abs_path = './driver'
# 解压后的文件名,下面是mac的默认路径,其他系统路径不一样需要改动
file_name = 'chromedriver'
session = requests.session()
# 创建文件夹
if not os.path.exists(abs_path): os.mkdir(abs_path)
# 获取chromedriver mapper对象
chrome_mapper = "https://raw.githubusercontent.com/appium/appium-chromedriver/master/config/mapping.json"
result = session.get(chrome_mapper)
result_text = json.loads(result.text)
for key, value in result_text.items():
    sub_path = abs_path + os.sep + key
    # 生成对应的下载文件目录
    if not os.path.exists(sub_path): os.mkdir(sub_path)
    # 获取每个镜像版本中可下载对象
    chrome_info = "https://npm.taobao.org/mirrors/chromedriver/%s/" % (key)
    mac_info_session = session.get(chrome_info)
    mac_info = mac_info_session.text
    # 获取可下载mac版本
    chrome_version = re.search(r"chromedriver_mac(.+?).zip", mac_info).group()
    # 判断文件是否存在，存在就跳过本次下载
    driver_file = sub_path + os.sep + file_name
    if not os.path.exists(driver_file): continue
    # 生成对应的可下载连接
    print("========================================================================================================")
    print("准备下载:%s" % (chrome_version))
    chrome_driver_url = "https://npm.taobao.org/mirrors/chromedriver/%s/%s" % (key, chrome_version)
    print("下载网址:%s" % (chrome_driver_url))
    result = session.get(chrome_driver_url, stream=True)
    # 当前文件下载大小
    size = 0
    # 获取文件总大小
    file_size = int(result.headers['content-length'])
    # 下载文件名
    abs_file_path = sub_path + os.sep + "driver.zip"
    with open(abs_file_path, 'wb') as file:
        # 配置每次下载大小
        for data in result.iter_content(chunk_size=1024):
            file.write(data)
            size += len(data)
            print('\r' + '[下载进度]:%s%.2f%%' % ('>' * int(size * 40 / file_size), float(size / file_size * 100)), end=' ')
    file.close()
    print('')
    print("开始解压文件:%s" % (abs_file_path))
    zip_file = zipfile.ZipFile(abs_file_path, 'r')
    for file in zip_file.namelist():
        zip_file.extract(file, sub_path)
    zip_file.close()
    # 删除文件
    os.remove(abs_file_path)
    print("删除压缩文件:%s" % (abs_file_path))

print("运行完成............................")
