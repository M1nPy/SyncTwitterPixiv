from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import sys
import os
from time import sleep


#環境変数ロード
load_dotenv()

option=webdriver.ChromeOptions()
option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36')
#chormedriverのpath
driver_path="SyncTwitterPixiv/chromedriver.exe"

driver=webdriver.Chrome(executable_path=driver_path,options=option)

driver.get("https://accounts.pixiv.net/login")
inputfield=driver.find_elements_by_tag_name("input")
inputfield[6].send_keys(os.getenv("pixiv_mailaddress"))
inputfield[7].send_keys(os.getenv("pixiv_password"))
inputfield[7].send_keys(Keys.ENTER)

sleep(3)#debug
driver.close()
driver.quit()