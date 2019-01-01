# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 17:49:24 2018

@author: milli

Generating a square wordcloud from text extracted from public Amharic comments 
from 17 youtube videos taken from channels with Ethiopian conetent.
"""
import pandas as pd
import commentsParser as cp
from pdfParser import clean_text
import matplotlib.pyplot as plt



#raw comments
comments = pd.read_csv('data\yt_comments.csv')

#remove non-amharic comments
comments_filtered = cp.filter_latin(comments)

#clean for numbers and special characters and convert to list
comment_words_list = clean_text(' '.join(comments_filtered.comment.tolist()))

#stop words
stop_words = open('data\stopwords.txt', encoding='utf-8').read().split()

#removing stop words
filtered_text_list = [val for val in comment_words_list if val not in stop_words]

comment_text = ' '.join(filtered_text_list)

from wordcloud import WordCloud
wordcloud = WordCloud(font_path='fonts\jiretsl.ttf',
                      relative_scaling = 1.0,
                      min_font_size=4,
                      background_color="white",
                      width=1024,
                      height=768,
                      scale=3,
                      font_step=1,
                      collocations=True,
                      #regexp=r"[\u0E00-\u0E7Fa-zA-Z']+",
                      margin=2
                      ).generate(comment_text)

plt.imshow(wordcloud, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('examples\\comments1.png',dpi=600)