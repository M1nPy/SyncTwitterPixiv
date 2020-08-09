import tweepy
from time import sleep
import sys
import re
import os
from dotenv import load_dotenv
import pandas as pd
from tweepy.error import RateLimitError

#正規表現
rege_pixiv = r'.*pixiv.*'

#.envロード
load_dotenv()
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
#認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#フォロー取得
hataraku_data = api.friends_ids("M1nPy")

list_pixivlinks=[]
#pixiv取得
n=0
for following in hataraku_data:
    i=0
    while True:
        #制限かかったら1分に一回try、20回で終了
        try:
            i+=1
            status_date=api.get_user(following)
            break
        except RateLimitError:
            print(str(i)+"RateLimitError")#debug
            if i>20:
                sys.exit()
            sleep(60)
    print(str(n)+":"+status_date.name)#debug
    #url欄
    try:
        status_url=status_date.entities["url"]["urls"][0]["expanded_url"]
        if not status_url:
            status_url=status_date.entities["url"]["urls"][0]["url"]
            if not status_url:
                status_url=''
    except:
        status_url=''
    if re.match(rege_pixiv,status_url) != None:
        list_pixivlinks.append((status_date.name,status_url))
    #プロフィール欄
    else:
        status_des=status_date.entities["description"]["urls"]
        for des_url in status_des:
            status_reurl=des_url["expanded_url"]
            if re.match(rege_pixiv,status_reurl) != None:
                list_pixivlinks.append((status_date.name,status_reurl))
                break
        else:
            list_pixivlinks.append((status_date.name,None))
    sleep(1)
    n+=1

#データフレームに変換してcsv出力
df_pixivlinks=pd.DataFrame(list_pixivlinks,columns=["name","url"]).fillna(False)
df_pixivlinks.to_csv(os.getcwd()+'/pixivlink.csv')