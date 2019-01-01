# -*- coding: utf-8 -*-
"""
#based on:

#this code scraps comments from youtube videos and filters out comments with latin characters

#Dec 13 2018
"""

import time
from selenium import webdriver
from contextlib import closing
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
latin_letters = {}
import unicodedata as ud

chrome_options = Options()  
chrome_options.add_argument("--headless")

def get_comments(url,rng=3):
    comments = []
    #read comments    
    with closing(webdriver.Chrome(ChromeDriverManager().install())) as driver:
        wait = WebDriverWait(driver,10)
        driver.get(url)
    
        for item in range(rng): #by increasing the highest range you can get more content
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(3)
    
        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
            comments.append(comments.text)    
    #return comments as list
    return comments


def run_parser(sources_csv='../data/yt_source.csv', comments_csv='../data/yt_comments.csv'):
    #open source file for url
    yt_source = pd.read_csv(sources_csv)
    yt_comments = pd.read_csv(comments_csv)
    #read comments 
    for i, row in yt_source.iterrows():
        if not row.processed:
            comments = get_comments(row.url,13)
            yt_source.set_value(i,'comments_fetched',len(comments))
            yt_source.set_value(i,'processed',1)
            #update comments file
            tmp = pd.DataFrame(comments, columns=['comment'])
            tmp['id'] = row.id
            yt_comments = yt_comments.append(tmp)

    #save files
    yt_source.to_csv(sources_csv,index=False)
    yt_comments.to_csv(comments_csv,index=False)
    
def filter_latin(comments):
    comments['isLatin'] = [only_roman_chars(thing) for thing in comments.comment]
    filtered = comments.loc[comments.isLatin!=True][['comment','id']]
    return filtered    

def is_latin(uchr):
    try: return latin_letters[uchr]
    except KeyError:
         return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))
     
def only_roman_chars(unistr):
    return all(is_latin(uchr) for uchr in unistr if uchr.isalpha())
    