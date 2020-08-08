import tweepy
from time import sleep
import sys
import re

#正規表現
rege_pixiv = r'.*pixiv.*'

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#フォロー取得
hataraku_data = api.friends_ids("M1nPy")

#pixiv取得
for following in hataraku_data:
    status_date=api.get_user(following)
    #url欄
    try:
        status_url=status_date.entities["url"]["urls"][0]["expanded_url"]
    except:
        status_url=''
    if re.match(rege_pixiv,status_url) != None:
        print(status_url)
    #プロフィール欄
    else:
        status_des=status_date.entities["description"]["urls"]
        for des_url in status_des:
            status_reurl=des_url["expanded_url"]
            if re.match(rege_pixiv,status_reurl) != None:
                print(status_reurl)
                break
        else:
            print(status_date.name)
    sleep(1)