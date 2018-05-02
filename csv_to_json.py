# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 01:41:13 2018

@author: kaushikp
"""


import pandas as pd
import json
from bson import json_util

df1 = pd.read_csv('C:/Users/hp/Desktop/Airbnb-Database/Tables/Availabilty Table.csv')
rec = json_util.loads(json.dumps(df1.to_dict(orient='records')))

with open('C:/Users/hp/Desktop/Airbnb-Database/MongoDbCollections/Availabilty Table.json', 'w') as outfile:
    json.dump(rec, outfile)


df2 = pd.read_csv('C:/Users/hp/Desktop/Airbnb-Database/Tables/facebook_feed.csv')
rec = json_util.loads(json.dumps(df2.to_dict(orient='records')))

with open('C:/Users/hp/Desktop/Airbnb-Database/MongoDbCollections/facebook_feed.json', 'w') as outfile:
    json.dump(rec, outfile)

df3 = pd.read_csv('C:/Users/hp/Desktop/Airbnb-Database/Tables/facebook_pages.csv')
rec = json_util.loads(json.dumps(df3.to_dict(orient='records')))

with open('C:/Users/hp/Desktop/Airbnb-Database/MongoDbCollections/facebook_pages.json', 'w') as outfile:
    json.dump(rec, outfile)


df4 = pd.read_csv('C:/Users/hp/Desktop/Airbnb-Database/Tables/facebook_tags.csv')
rec = json_util.loads(json.dumps(df4.to_dict(orient='records')))

with open('C:/Users/hp/Desktop/Airbnb-Database/MongoDbCollections/facebook_tags.json', 'w') as outfile:
    json.dump(rec, outfile)

df5 = pd.read_csv('C:/Users/hp/Desktop/Airbnb-Database/Tables/Host Table.csv')
rec = json_util.loads(json.dumps(df5.to_dict(orient='records')))

with open('C:/Users/hp/Desktop/Airbnb-Database/MongoDbCollections/Host Table.json', 'w') as outfile:
    json.dump(rec, outfile)

df6 = pd.read_csv('C:/Users/hp/Desktop/Airbnb-Database/Tables/Property Table.csv')
rec = json_util.loads(json.dumps(df6.to_dict(orient='records')))

with open('C:/Users/hp/Desktop/Airbnb-Database/MongoDbCollections/Property Table.json', 'w') as outfile:
    json.dump(rec, outfile)

df7 = pd.read_csv('C:/Users/hp/Desktop/Airbnb-Database/Tables/Reviews.csv')
rec = json_util.loads(json.dumps(df7.to_dict(orient='records')))

with open('C:/Users/hp/Desktop/Airbnb-Database/MongoDbCollections/Reviews.json', 'w') as outfile:
    json.dump(rec, outfile)