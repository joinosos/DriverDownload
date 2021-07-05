### start
1、获取chromedriver mapper <br>
    ```
    https://raw.githubusercontent.com/appium/appium-chromedriver/master/config/mapping.json
    ```
    <br>
2、从淘宝镜像中获取对应的chromedriver <br>
    ```
    https://npm.taobao.org/mirrors/chromedriver
    ```
    <br>
3、下载对应系统的驱动,下面下载的是mac电脑驱动,可修改成win、linux <br>
    ```
    re.search(r"chromedriver_mac(.+?).zip", mac_info).group()
    ```
   <br>
4、使用zipfile解压文件 <br>
5、mac解压后的文件名是chromedriver,windows解压后是chromedriver.exe <br>
    ```
    file_name = 'chromedriver'
    ```
    <br>
6、zipfile解压后权限是-rw-r--r--,配置成-rwxrwxrwx 
    ```
    os.chmod(abs_file_path, stat.S_IRWXU+stat.S_IRWXG+stat.S_IRWXO)
    ```
    <br>
7、下载路径当前工程的driver目录下 <br>
### end


