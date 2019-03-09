#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:20:59 2019

@author: hectorramirez
"""


import tweepy
import time


CONSUMER_KEY = 'mQK4euWb5M7rgDPeLrzvATAQS'
CONSUMER_SECRET = 'eje4mXFXTdkfcR53BdoakjfqWW8s6oJ6qrTTKiF5ot9h84GUzN'
ACCESS_KEY = '1104151780726845440-mYifJpRD1w2tgELSs8za3DMUDfUzjv'
ACCESS_SECRET = 'SNahgYnuiREJ5gWlegiTBXuV9gTMIdTAYaDOFkwIWLS33'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply():
    print("replying...")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id)
    
    
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.text.lower():
            print('found #helloworld!')
            print('responding back...')
            api.update_status('@'+mention.user.screen_name + ' Right back at you! #HelloWorld', mention.id)
            api.retweet(mention.id)
    
    
while True:
    reply()
    time.sleep(15)


