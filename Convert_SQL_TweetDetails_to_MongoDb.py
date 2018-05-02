# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 20:12:53 2018

@author: kaushikp

"""
import pandas as pd
import json
from bson import json_util

###Code for converting TD.csv
#df = pd.read_csv('C:/Users/hp/Documents/NEU Subjects/Spring 2018/DBMS/Project/Listing Details Table.csv')


df1 = pd.DataFrame(columns=['tweet_id', 'tweet_txt', 'cre_tms', 'user_loc', 
                                   'retweet_cnt', 'fav_cnt', 'user_name', 'hashtags', 'urls'])



"""


df1['tweet_txt'] = df['Text']

df1['cre_tms'] = df['cre_tms']

df1['retweet_cnt'] = df['retweet_cnt']

df1['fav_cnt']=df['fav_cnt']

df1['user_name']=df['user_name']


for i in range(len(df)):
    if df.isnull()['urls'][i]:
        df1['urls'][i]=[]
    else:
        df1['urls'][i]=[df['urls'][i]]
        



for i in range(len(df)):
    t=[]
    for j in range(1,12):
        c = 'tag' + str(j)
        if df.isnull()[c][i]:
            continue;
        else:
            t.append(df[c][i])
    df1['hashtags'][i] = t
    
rec_td = json_util.loads(json.dumps(df1.to_dict(orient='records')))

from pymongo import MongoClient



client = MongoClient()
db = client.airbnb
db.TweetDetils.insert_many(rec_td)
"""