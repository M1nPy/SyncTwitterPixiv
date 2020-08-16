from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import sys
import os
from time import sleep
import pandas as pd


# 環境変数ロード
load_dotenv()

# csv読み込み
df_pixivlinks = pd.read_csv(os.getcwd()+'/pixivlink.csv')

option = webdriver.ChromeOptions()
option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36')
# chormedriverのpath
driver_path = "SyncTwitterPixiv/chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path, options=option)

driver.get("https://accounts.pixiv.net/login")
inputfield = driver.find_elements_by_tag_name("input")
inputfield[6].send_keys(os.getenv("pixiv_mailaddress"))
inputfield[7].send_keys(os.getenv("pixiv_password"))
inputfield[7].send_keys(Keys.ENTER)

sleep(2)

for p_link in df_pixivlinks.itertuples():
    # urlの有無
    if p_link.url != "False":
        driver.get(p_link.url)
        sleep(2)
        try:
            # フォローボタン探索
            followbutton = driver.find_element_by_css_selector("button[type='submit']")
            followbutton.click()
            sleep(2)
        except selenium_exceptions.NoSuchElementException:
            print(p_link.name+" is already followed")
        except Exception:
            print(Exception)
            sys.exit()
    else:
        print(p_link.name+" haven't pixivlink")

driver.close()
driver.quit()
