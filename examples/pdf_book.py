# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 14:39:35 2018

@author: milli

script to generate a wordcloud a free ebook
"""

import pdfParser as pp
import matplotlib.pyplot as plt
from wordcloud import WordCloud
plt.figure(figsize=(15,10))

#book can be from dounloadded path or from url
book_url = 'http://www.alemayehu.org/wp-content/uploads/2016/09/Web-%E1%8B%A8%E1%8C%88%E1%89%A0%E1%89%B3-%E1%8B%88%E1%8C%8E%E1%89%BD.pdf'

text = pp.parse_pdf(book_url)
#removing stop words
stop_words = open('data\stopwords.txt', encoding='utf-8').read().split()
filtered_text_list = [val for val in text if val not in stop_words]
filtered_text = ' '.join(filtered_text_list)

wordcloud = WordCloud(font_path='fonts\jiretsl.ttf',
                      relative_scaling = 1.0,
                      min_font_size=4,
                      background_color="white",
                      width=1024,
                      height=768,
                      scale=3,
                      font_step=1,
                      collocations=False,
                      margin=2
                      ).generate(filtered_text)

plt.imshow(wordcloud, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('examples\\am_book.png',dpi=600)