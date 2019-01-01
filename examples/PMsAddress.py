# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 04:28:21 2018

@author: milli

Generating a wordcloud with map of Ethiopia from Ethiopias PM 2018 Inaugural Address taken from 
http://www.allthingsethiopia.com/ethiopia-breaking-news/2753/.
"""
import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from pdfParser import clean_text

text = open('data\PMs Inaugural Address.txt', encoding='utf-8').read()

stop_words = open('data\stopwords.txt', encoding='utf-8').read().split()


ethiopia_mask = np.array(Image.open('data\\ethiopia_map.jpg'))

#removing stop words
filtered_text_list = [val for val in clean_text(text) if val not in stop_words]

#replace ager with hager
filtered_text_list = ['ሀገር' if x == 'አገር' else x for x in filtered_text_list]
filtered_text = ' '.join(filtered_text_list)

#generat ethe word cloud
wordcloud = WordCloud(font_path='fonts\jiretsl.ttf',
                      relative_scaling = 0.0,
                      min_font_size=4,
                      background_color="white",
                      width=1024,
                      height=768,
                      scale=3,
                      font_step=1,
                      collocations=False,
                      margin=2,
                      mask= ethiopia_mask
                      ).generate(filtered_text)

#plot and save
plt.imshow(wordcloud, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
#plt.savefig('example\\PMsAddress.png',dpi=1200)